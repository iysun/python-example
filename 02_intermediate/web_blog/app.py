"""
Flask 博客系统
练习点：Flask、SQLite、Jinja2 模板、表单处理、会话管理
"""
from flask import Flask, render_template, request, redirect, url_for, session, flash
from database import init_db, get_db

app = Flask(__name__)
app.secret_key = "change-this-in-production"


@app.before_request
def setup():
    init_db()


@app.route("/")
def index():
    """首页：展示所有文章列表。"""
    # TODO: 查询数据库获取所有文章，按时间倒序
    # TODO: 返回 render_template("index.html", posts=posts)
    raise NotImplementedError


@app.route("/post/<int:post_id>")
def post_detail(post_id: int):
    """文章详情页。"""
    # TODO: 查询指定 id 的文章，不存在则 404
    raise NotImplementedError


@app.route("/new", methods=["GET", "POST"])
def new_post():
    """新建文章（需登录）。"""
    if "user_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()
        # TODO: 验证输入不为空，插入数据库，重定向到首页
        raise NotImplementedError

    return render_template("new_post.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """用户登录。"""
    if request.method == "POST":
        # TODO: 验证用户名和密码，成功则写入 session
        raise NotImplementedError
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
