# Python 实战练习集

从零到工程能力的完整练习路径，按难度分三个阶段。每个项目的函数体均为 `raise NotImplementedError`，并附有 `# TODO` 实现提示，自己动手填充即可。

---

## 目录结构

```
python-exercises/
├── 01_beginner/          # 入门级：只用标准库或单一第三方库
│   ├── file_renamer/     # 文件批量重命名工具
│   ├── todo_cli/         # 待办事项 CLI
│   ├── password_generator/  # 密码生成器
│   ├── csv_analyzer/     # CSV 数据分析
│   └── web_scraper/      # 网页数据爬虫
│
├── 02_intermediate/      # 中级：多模块协作，涉及网络/数据库/自动化
│   ├── web_blog/         # Flask 博客系统
│   ├── user_auth/        # 用户注册登录（SQLite + 密码哈希）
│   ├── web_automation/   # 网页自动化（Playwright）
│   ├── email_reminder/   # 定时邮件提醒
│   ├── weather_cli/      # 天气查询 CLI（调用免费 API）
│   └── github_stats/     # GitHub 提交统计
│
└── 03_advanced/          # 进阶级：接近真实工程实践
    ├── data_report/      # pandas + matplotlib 数据分析报告
    └── rest_api/         # FastAPI RESTful 后端
```

---

## 实现计划

### 第一阶段：入门级

建议按顺序完成，每个项目练习不同的核心知识点。

#### 1. 文件批量重命名 `01_beginner/file_renamer/`
| 项目 | 内容 |
|------|------|
| 目标 | 给一批文件统一添加前缀/后缀，支持预览模式 |
| 练习点 | `pathlib`、`argparse`、字符串操作 |
| 完成标志 | `python main.py ./photos --prefix "2024_" --run` 能正确重命名 |

- [x] 实现 `build_parser()` 定义命令行参数
- [x] 实现 `rename_files()` 的预览和实际重命名逻辑
- [x] 扩展：支持只处理指定扩展名（`--ext .jpg`）

#### 2. 待办事项 CLI `01_beginner/todo_cli/`
| 项目 | 内容 |
|------|------|
| 目标 | 带持久化的命令行 Todo 应用 |
| 练习点 | `dataclass`、`enum`、JSON 文件读写、列表操作 |
| 完成标志 | 重启程序后数据不丢失 |

- [x] 实现 `Todo.to_dict()` / `from_dict()`
- [x] 实现 `load()` / `save()`
- [x] 实现 `add()` / `complete()` / `delete()`
- [x] 实现 `show_list()` 格式化输出
- [x] 扩展：支持截止日期和优先级

#### 3. 密码生成器 `01_beginner/password_generator/`
| 项目 | 内容 |
|------|------|
| 目标 | 生成强随机密码，评估密码强度 |
| 练习点 | `secrets`（比 `random` 更安全）、`string` 模块、`argparse` |
| 完成标志 | `python main.py -l 20 -n 5` 输出 5 个不同的 20 位密码 |

- [ ] 实现 `generate_password()` 确保每类字符至少各有一个
- [ ] 实现 `check_strength()` 评估强度
- [ ] 扩展：支持排除易混淆字符（`0Ol1I`）

#### 4. CSV 数据分析 `01_beginner/csv_analyzer/`
| 项目 | 内容 |
|------|------|
| 目标 | 交互式分析任意 CSV 文件 |
| 练习点 | `csv.DictReader`、`collections`、数值统计 |
| 完成标志 | 能对 Kaggle 下载的真实数据集完成分析 |

- [ ] 实现 `load_csv()` 读取文件
- [ ] 实现 `summary()` 数值统计
- [ ] 实现 `frequency()` 频次统计
- [ ] 实现 `group_sum()` 分组汇总
- [ ] 实现 `main()` 的交互选择逻辑

#### 5. 网页爬虫 `01_beginner/web_scraper/`
| 项目 | 内容 |
|------|------|
| 目标 | 爬取 quotes.toscrape.com 的名言并保存为 CSV |
| 练习点 | `requests`、`BeautifulSoup`、`csv`、分页处理 |
| 完成标志 | 爬取 3 页，输出包含文字/作者/标签的 CSV 文件 |

- [ ] 实现 `fetch_page()` 请求并解析页面
- [ ] 实现 `parse_quotes()` 提取名言数据
- [ ] 实现 `get_next_url()` 获取下一页链接
- [ ] 实现 `save_to_csv()` 写出结果

---

### 第二阶段：中级

每个项目都有真实用途，完成后可以直接使用。

#### 6. Flask 博客系统 `02_intermediate/web_blog/`
| 项目 | 内容 |
|------|------|
| 目标 | 可登录、可发文的最小博客 |
| 练习点 | Flask 路由、Jinja2 模板、SQLite、Session |
| 完成标志 | 浏览器能注册/登录/发文/查看文章 |

- [ ] 实现 `index()` 查询并展示文章列表
- [ ] 实现 `post_detail()` 文章详情
- [ ] 实现 `new_post()` 表单处理和数据库插入
- [ ] 实现 `login()` / `logout()` 会话管理
- [ ] 补全 `templates/` 下的 HTML 模板
- [ ] 扩展：文章编辑/删除、Markdown 支持

#### 7. 用户注册登录 `02_intermediate/user_auth/`
| 项目 | 内容 |
|------|------|
| 目标 | 命令行版用户系统，密码安全哈希存储 |
| 练习点 | SQLite、`hashlib`、`secrets`、异常处理 |
| 完成标志 | 密码以哈希形式存储，明文无法从数据库还原 |

- [ ] 实现 `register()` 含 salt + hash
- [ ] 实现 `login()` 验证逻辑
- [ ] 补全 `main()` 的交互逻辑
- [ ] 扩展：改用 `bcrypt` 替代 SHA-256

#### 8. 网页自动化 `02_intermediate/web_automation/`
| 项目 | 内容 |
|------|------|
| 目标 | 自动登录练习网站并截图 |
| 练习点 | Playwright、选择器、等待策略、截图 |
| 完成标志 | 无需手动操作，程序自动完成登录并保存截图 |

- [ ] 安装：`pip install playwright && playwright install chromium`
- [ ] 实现 `login()` 自动填表并点击
- [ ] 实现 `extract_items()` 提取页面数据
- [ ] 扩展：改造为爬取需要登录的网站数据

#### 9. 邮件提醒 `02_intermediate/email_reminder/`
| 项目 | 内容 |
|------|------|
| 目标 | 每天定时发送提醒邮件 |
| 练习点 | `smtplib`、`schedule`、`.env` 环境变量管理 |
| 完成标志 | 程序运行后按设定时间自动发送邮件 |

- [ ] 复制 `.env.example` 为 `.env`，填写真实邮箱配置
- [ ] 实现 `send_email()` SMTP 发送逻辑
- [ ] 实现 `main()` 定时调度
- [ ] 扩展：支持从 JSON 文件读取多条定时任务

#### 10. 天气查询 `02_intermediate/weather_cli/`
| 项目 | 内容 |
|------|------|
| 目标 | 输入城市名，查询实时天气（免费 API，无需 Key） |
| 练习点 | `requests`、JSON 解析、API 调用、错误处理 |
| 完成标志 | 输入"北京"能输出当前温度、天气状况、风速 |

- [ ] 实现 `search_city()` 地理编码
- [ ] 实现 `fetch_weather()` 获取天气数据
- [ ] 实现 `format_weather()` 格式化输出
- [ ] 扩展：支持查询未来 7 天预报

#### 11. GitHub 提交统计 `02_intermediate/github_stats/`
| 项目 | 内容 |
|------|------|
| 目标 | 统计某 GitHub 用户一年内的提交分布 |
| 练习点 | GitHub REST API、分页请求、数据聚合、`Counter` |
| 完成标志 | 输出用户的总提交数、最活跃仓库 Top5、各星期几提交分布 |

- [ ] 实现 `get_user_repos()` 含分页
- [ ] 实现 `get_commits()` 按时间过滤
- [ ] 实现 `analyze()` 统计和输出
- [ ] 扩展：用字符画在终端绘制提交热力图

---

### 第三阶段：进阶级

#### 12. 数据分析报告 `03_advanced/data_report/`
| 项目 | 内容 |
|------|------|
| 目标 | 读取 CSV，生成含图表的 HTML 数据报告 |
| 练习点 | `pandas`、`matplotlib`、`seaborn`、HTML 报告生成 |
| 完成标志 | 打开 `output/report.html` 能看到统计表和可视化图表 |

- [ ] 实现 `load_data()` 含数据清洗
- [ ] 实现 `basic_stats()` 描述性统计
- [ ] 实现 `plot_distribution()` 分布图
- [ ] 实现 `plot_correlation()` 相关性热力图
- [ ] 实现 `generate_html_report()` 生成报告
- [ ] 扩展：用 `Jinja2` 模板渲染报告

#### 13. RESTful API 后端 `03_advanced/rest_api/`
| 项目 | 内容 |
|------|------|
| 目标 | 完整的任务管理 API，含自动文档 |
| 练习点 | FastAPI、Pydantic、SQLite、HTTP 状态码、依赖注入 |
| 完成标志 | 访问 `http://127.0.0.1:8000/docs` 能通过 Swagger UI 测试所有接口 |

- [ ] 实现数据库连接和初始化逻辑（`database.py`）
- [ ] 实现 `routers/tasks.py` 中所有 5 个端点
- [ ] 实现正确的 HTTP 状态码（201 创建、404 不存在、204 删除）
- [ ] 扩展：添加用户认证（JWT Token）

---

## 学习建议

1. **不要跳过入门级**——哪怕看起来简单，每个项目都在训练特定肌肉
2. **先自己写，卡住再查文档**——直接看答案会失去最有价值的练习
3. **完成后尝试扩展**——每个项目末尾的"扩展"任务才是真正的挑战
4. **提交到 GitHub**——让别人看见你的代码，锻炼写 README 和注释的能力
