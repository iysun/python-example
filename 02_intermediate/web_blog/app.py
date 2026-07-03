"""
Flask 博客系统
练习点：Flask、SQLite、Jinja2 模板、表单处理、会话管理
"""

import os
import sqlite3
from contextlib import closing
from functools import wraps

from flask import Flask, abort, g, render_template, request, redirect, url_for, session, flash
from werkzeug.security import check_password_hash, generate_password_hash

from database import get_db

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key-change-me")

POST_LIST_SQL = """
    SELECT
        posts.id,
        posts.title,
        posts.content,
        posts.created_at,
        users.username AS author
    FROM posts
    LEFT JOIN users ON users.id = posts.author_id
    ORDER BY posts.created_at DESC
"""

POST_DETAIL_SQL = """
    SELECT
        posts.id,
        posts.title,
        posts.content,
        posts.created_at,
        users.username AS author
    FROM posts
    LEFT JOIN users ON users.id = posts.author_id
    WHERE posts.id = ?
"""


@app.before_request
def load_current_user():
    g.current_user = None
    user_id = session.get("user_id")
    if user_id is None:
        return

    try:
        user_id = int(user_id)
    except (TypeError, ValueError):
        session.clear()
        return

    with closing(get_db()) as db:
        user = db.execute(
            "select id, username from users where id = ?",
            (user_id,),
        ).fetchone()

    if user is None:
        session.clear()
        return

    session["user_id"] = user["id"]
    g.current_user = user


def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if g.current_user is None:
            return redirect(url_for("login"))
        return view(*args, **kwargs)

    return wrapped_view


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404


@app.route("/")
@login_required
def index():
    """首页：展示所有文章列表。"""
    with closing(get_db()) as db:
        posts = db.execute(POST_LIST_SQL).fetchall()
    return render_template("index.html", posts=posts)


@app.route("/post/<int:post_id>")
@login_required
def post_detail(post_id: int):
    """文章详情页。"""
    with closing(get_db()) as db:
        post = db.execute(POST_DETAIL_SQL, (post_id,)).fetchone()
    if not post:
        abort(404)
    return render_template("post_detail.html", post=post)


@app.route("/new", methods=["GET", "POST"])
@login_required
def new_post():
    """新建文章（需登录）。"""
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()
        if not title:
            flash("标题不能为空")
        if not content:
            flash("内容不能为空")
        if not title or not content:
            return render_template("new_post.html"), 400

        with closing(get_db()) as db:
            db.execute(
                "insert into posts (title, content, author_id) values (?, ?, ?)",
                (title, content, g.current_user["id"]),
            )
            db.commit()
        flash("文章发布成功")
        return redirect(url_for("index"))

    return render_template("new_post.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """用户注册。"""
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()
        if len(username) < 3:
            flash("用户名至少 3 个字符")
            return render_template("register.html"), 400
        if len(password) < 6:
            flash("密码至少 6 个字符")
            return render_template("register.html"), 400

        password_hash = generate_password_hash(password)
        try:
            with closing(get_db()) as db:
                cursor = db.execute(
                    "insert into users (username, password_hash) values (?, ?)",
                    (username, password_hash),
                )
                db.commit()
                session["user_id"] = cursor.lastrowid
        except sqlite3.IntegrityError:
            flash("用户名已存在")
            return render_template("register.html"), 400

        flash("注册成功")
        return redirect(url_for("index"))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """用户登录。"""
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()
        with closing(get_db()) as db:
            user = db.execute(
                "select id, username, password_hash from users where username = ?",
                (username,),
            ).fetchone()

        if user and check_password_hash(user["password_hash"], password):
            session["user_id"] = user["id"]
            flash("登录成功")
            return redirect(url_for("index"))

        flash("用户名或密码错误")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1")
