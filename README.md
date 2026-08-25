# Marrow Notes — 关卡 4 本地站

12 个页面：1 首页 + 3 导航页 + 8 内页。无外部依赖，无框架，纯静态。

线上地址：<https://kevin-wei-sudo.github.io/marrow-notes/>

## 跑起来

解压后：

```bash
cd site
python3 -m http.server 8080
```

浏览器打开 `http://localhost:8080/`。

也可以直接双击 `site/index.html` —— 所有链接都是相对路径，`file://` 下同样能跑通。
但 **AITDK 检查请务必用 `http://localhost:8080`**，`file://` 下部分插件读不到 meta。

## 改内容

```
site-src/content.py     所有页面文字 + 信源，改这个
site-src/build.py       模板、CSS、mini-markdown 解析器
site-src/seo_check.py   SEO 自检
site-src/make_og.py     og:image 卡片 + favicon 生成器
site-src/static/        生成好的图片，build.py 原样拷进 site/
```

```bash
cd site-src
python3 build.py        # 重新生成 site/
python3 seo_check.py    # 自检，必须 0 errors 0 warnings
```

改了页面标题或信源之后，og 卡片要重新生成一次：

```bash
python3 make_og.py      # 只在 macOS 跑（用 Quick Look 光栅化），产物已提交
```

`build.py` 不生成图片，只拷贝 `static/`，所以 CI 里不需要浏览器或图形库。

### content.py 的写法

| 语法 | 输出 |
|---|---|
| `## 标题` | H2（自动生成锚点 + 右侧目录） |
| `### 标题` | H3 |
| `- 条目` | 无序列表 |
| `\| a \| b \|` | 表格，第一行是表头 |
| `!!Disputed\|文字` | 琥珀色冲突提示块 |
| `!!Unconfirmed\|文字` | 灰色待验证提示块 |
| `[[文字\|/path.html]]` | 内链 |
| `{{t1}}` | 信源标记：Official |
| `{{t2}}` | 信源标记：Tested |
| `{{t3}}` | 信源标记：Unconfirmed |
| `{{ugc}}` | 信源标记：Players |

`sources` 字段填 `(等级, 来源名, 这个来源提供了什么)`，页面底部自动渲染成分级信源列表。

## 站点结构

```
/                          首页（品牌词）
├── /bosses/index.html     导航页 · all bosses in order
│   ├── magdalena.html
│   └── zmey-or-malborn.html
├── /shells/index.html     导航页 · shells tier list / locations
│   ├── best-first-shell.html
│   └── glimpses.html
└── /systems/index.html    导航页 · 机制与 PC 问题
    ├── hardening.html
    ├── stuttering-fix.html
    ├── beta-carry-over.html
    └── gloom-recovery.html
```

每页都有：面包屑向上、正文内链横向跨栏、底部信源列表。

## AITDK 检查步骤

1. `python3 -m http.server 8080`
2. 打开任意页面，点 AITDK 图标 → Overview
3. 应该看到：
   - **Title** 有值，37–58 字符
   - **Description** 有值，132–157 字符
   - **H1** 恰好 1 个
   - **H2** 6–10 个，层级不跳级（无 H1→H3）
   - **Canonical** 有值
   - **OG tags** 7 个

首页和 `/bosses/magdalena.html` 各截一张，作业够用。

## 自检脚本覆盖了什么

`seo_check.py` 检查 12 个页面的：title 长度、description 长度、H1 数量、标题层级跳级、canonical、viewport、og 数量、JSON-LD、内链是否 404、全站 title/description 是否重复。

当前状态：**12 pages | 0 errors | 0 warnings**。

## 响应式自查清单

- [x] `viewport` meta 全站存在
- [x] 桌面端双栏（正文 + 右侧粘性目录），960px 以下自动单栏
- [x] 表格外包 `.tw` 横向滚动容器，窄屏不撑破
- [x] `overflow-wrap:break-word`，长英文词不溢出
- [x] 600px 以下字号、间距、导航独立调整
- [x] 键盘焦点可见（`:focus-visible`）
- [x] Skip to content 链接
- [x] `prefers-reduced-motion` 已处理

手机端验证：Chrome DevTools → 设备工具栏 → iPhone SE（375px，最窄的常见机型）。重点看 `/bosses/magdalena.html` 底部那张「Still dying?」五列表格。

## 部署

push 到 `main` 触发 `.github/workflows/pages.yml`：重跑 `build.py` + `seo_check.py`，把 `site/` 发到 GitHub Pages。

换域名只要改 `content.py` 里的 `SITE["base"]`（影响 canonical / og:url / sitemap / robots），页面之间是相对路径，不受子路径影响。

## 图片

| 文件 | 用途 | 来源 |
|---|---|---|
| `shots/*.jpg` | 7 张页面配图，1400×788 | 发行商截图 |
| `og/*.jpg` | 每页一张 1200×630 分享卡，有配图的页面用截图压暗作底 | 混合 |
| `assets/favicon.svg` | 标签页图标，Marrow 的 M + 站名里那个点 | 自制 |
| `assets/apple-touch-icon.png` | iOS 加到主屏幕，180×180 | 自制 |

### 版权

`shots/` 里的截图取自 Steam 商店页（app 2584270），版权属 **Cold Symmetry / Playstack**，本站不拥有。
每张图的 `figcaption` 都带来源标注，页脚已声明本站为非官方粉丝站。这是粉丝攻略站的通行做法，
但**不是**发行商明确授权 —— 官方没有公开 press kit。收到任何异议就撤图。

### 配图不许编造

发行商没有给任何一张截图标注 boss 名或地点。所以图注只能描述画面里**看得见**的东西，
不能把一张截图说成某场没有确认过的战斗 —— 这个站的立身之本就是不编造。

`content.py` 里 Magdalena 那条图注就是范例：明说那是该区域的官方截图，不是她的战斗场景，
因为官方从未放出那场战斗的图。`shells/index` 那条可以说得具体，因为画面里就印着
Proxima, the Broodseeker 和她的两个技能。

## 还没做的

- 用的是 `github.io` 子路径，没接自有域名
- 正文没有配图（boss 位置图、Shell 外观），需要游戏素材授权
- Hardening 页缺帧数数据，页面里已用 Unconfirmed 块标明
- Magdalena 页的「Still dying?」诊断表是从二手信源推的，需实际游玩验证
