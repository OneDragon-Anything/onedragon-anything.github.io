import{_ as s}from"./plugin-vue_export-helper-DlAUqK2U.js";import{c as r,b as a,a as i,d as l,e as o,f as n,r as d,o as c}from"./app-PZqzuEQN.js";const h={};function p(u,e){const t=d("RouteLink");return c(),r("div",null,[e[9]||(e[9]=a('<div class="hint-container important"><p class="hint-container-title">重要</p><p>请认真阅读本页面，可以帮助你顺利完成安装，减少浪费时间。</p></div><h2 id="_1-安装" tabindex="-1"><a class="header-anchor" href="#_1-安装"><span>1.安装</span></a></h2><p>脚本请存放在 <span style="color:red;"><strong>全英文的路径</strong></span> 下</p><h3 id="_1-1-使用安装器-推荐" tabindex="-1"><a class="header-anchor" href="#_1-1-使用安装器-推荐"><span>1.1.使用安装器（推荐）</span></a></h3><p>如果你不懂得如何搭建python环境，请使用本方法。</p><p>如果出现安装依赖失败，且你的电脑上曾经安装过anaconda，则可以卸载后anaconda重试本方法，或者使用 1.2 方法。</p>',6)),i("ol",null,[e[3]||(e[3]=i("li",null,[l("从 "),i("a",{href:"https://github.com/DoctorReid/StarRailOneDragon/releases/latest",target:"_blank",rel:"noopener noreferrer"},"最新 Release"),l(" 中下载 "),i("code",null,"StarRailOneDragon-X.Y.Z.zip"),l(" (X.Y.Z 为版本号)")],-1)),i("li",null,[e[1]||(e[1]=l("如果你无法访问Github，或者下载速度慢，可以参考 ")),o(t,{to:"/other/zh/visit_github.html"},{default:n(()=>e[0]||(e[0]=[l("如何访问Github")])),_:1}),e[2]||(e[2]=l("，或者你可以加入 QQ群 743525216，从群文件中下载。"))]),e[4]||(e[4]=i("li",null,[l("下载后解压，运行 "),i("code",null,"OneDragon Installer.exe")],-1)),e[5]||(e[5]=i("li",null,"安装器中，点击一键安装即可。",-1)),e[6]||(e[6]=i("li",null,[l("安装完成后，在安装器上点击"),i("code",null,"启动一条龙"),l("，或运行 "),i("code",null,"OneDragon Launcher.exe")],-1))]),e[10]||(e[10]=a('<h3 id="_1-2-使用安装器-已有的-anaconda-推荐" tabindex="-1"><a class="header-anchor" href="#_1-2-使用安装器-已有的-anaconda-推荐"><span>1.2.使用安装器 + 已有的 anaconda（推荐）</span></a></h3><p>如果你之前因为其它脚本安装了 anaconda，则可以使用本方法</p><ol><li>下载安装器，同 1.1 的前3步。</li><li>打开你的 anaconda prompt，并输入以下命令创建环境，中途提示输入 <code>y</code> 确认即可</li></ol><div class="language-shell line-numbers-mode" data-highlighter="shiki" data-ext="shell" data-title="shell" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34;"><pre class="shiki shiki-themes one-light one-dark-pro vp-code"><code><span class="line"><span style="--shiki-light:#4078F2;--shiki-dark:#61AFEF;">conda</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379;"> create</span><span style="--shiki-light:#986801;--shiki-dark:#D19A66;"> --name</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379;"> sr-od</span><span style="--shiki-light:#50A14F;--shiki-dark:#98C379;"> python=</span><span style="--shiki-light:#986801;--shiki-dark:#D19A66;">3.11</span></span></code></pre><div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0;"><div class="line-number"></div></div></div><ol start="3"><li>安装器中点击 <code>Git-默认安装</code> <code>代码版本-代码同步</code></li><li>Python虚拟环境点击 <code>选择已有</code>，选择刚刚创建环境的 <code>pythonw.exe</code>，目录大概如下</li></ol><div class="language-shell line-numbers-mode" data-highlighter="shiki" data-ext="shell" data-title="shell" style="--shiki-light:#383A42;--shiki-dark:#abb2bf;--shiki-light-bg:#FAFAFA;--shiki-dark-bg:#282c34;"><pre class="shiki shiki-themes one-light one-dark-pro vp-code"><code><span class="line"><span style="--shiki-light:#4078F2;--shiki-dark:#61AFEF;">你的目录\\anaconda\\envs\\sr-od\\pythonw.exe</span></span></code></pre><div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0;"><div class="line-number"></div></div></div><ol start="5"><li>安装器中点击 <code>运行依赖-默认安装</code>，等待完成。</li><li>安装完成后，安装器上点击<code>启动一条龙</code>，或运行 <code>OneDragon Launcher.exe</code></li></ol><h3 id="_1-3-使用源码运行" tabindex="-1"><a class="header-anchor" href="#_1-3-使用源码运行"><span>1.3.使用源码运行</span></a></h3><p>如果你懂得如何搭建python环境(推荐使用 3.11.9)，请使用本方法</p><ol><li>创建你自己的虚拟环境</li><li><code>git clone git@github.com:DoctorReid/StarRailOneDragon.git</code></li><li><code>pip install -r requirements-prod.txt</code></li><li>运行 （以下二选一） <ul><li>复制 <code>env.sample.bat</code>，重命名为 <code>env.bat</code>，并修改内容为你的虚拟环境的 python 路径，使用 <code>OneDragon Launcher.exe</code> 运行。</li><li>将<code>src</code>文件夹加入环境变量<code>PYTHONPATH</code>，执行 <code>python src/sr_od/gui/sr_full_app.py</code> 。</li></ul></li></ol><h2 id="_2-使用前须知" tabindex="-1"><a class="header-anchor" href="#_2-使用前须知"><span>2.使用前须知</span></a></h2><p><strong>第一次运行前请先认真阅读以下内容</strong></p><ol><li>游戏内需要设置成 16:9 的分辨率，即 <code>1920*1080</code> 或 <code>2560*1440</code> 或 <code>3840*2160</code>。使用 <code>1920*1080</code> 以下分辨率可能有问题，暂不打算特殊支持。</li><li>如果游戏使用 <code>全屏模式</code>，则需要 <code>显示器屏幕的分辨率</code>也是 16:9，否则只能使用 <code>窗口模式</code>。</li><li>多屏幕的需要将游戏窗口放在 1 号屏。</li><li>由于使用的是图像识别，请确保游戏画面完整在屏幕内，且游戏画面没有任何遮挡（帧率显示、windows 未激活水印等均有可能导致脚本出错）。 <ul><li>游戏画质越好，脚本出错的几率越低。</li></ul></li><li>同时，请不要开启会改变画面像素值的功能或设置，例如 <ul><li>系统层面 - windows 系统的颜色配置文件、校准显示器颜色、颜色管理、HDR 等。</li><li>驱动层面 - 显卡驱动控制面板里的游戏滤镜等。</li><li>设备层面 - 显示器的护眼模式、色彩模式、色温调节、HDR 等。</li></ul></li><li>脚本运行过程，请勿使用任何输入法，避免按键被输入法吞了。</li><li>脚本运行后会接管键盘和鼠标，游戏窗口需要保证在前台，如果你想进行人工操作，可以先使用 <strong>F9暂停</strong>。</li><li>脚本是按完成所有游戏内容后的状态进行编写的，以下情况有几率导致脚本出错： <ul><li>右上角的角色图标有红点</li><li>大地图未完全开启</li><li>大地图上有通关后图标会消失的内容 （即你未通关，有多余的图标）</li></ul></li><li>第一次运行时，你需要先做完成以下事项 <ul><li>如果游戏中有改键，到脚本的「设置」-「游戏设置」中更改对应按键，</li><li>到脚本的「游戏助手」-「校准」中运行一次，完成鼠标的转向校准。</li></ul></li></ol><h2 id="_3-常见问题" tabindex="-1"><a class="header-anchor" href="#_3-常见问题"><span>3.常见问题</span></a></h2>',14)),i("p",null,[e[8]||(e[8]=l("可以到这里查看 ")),o(t,{to:"/other/zh/common_qa.html"},{default:n(()=>e[7]||(e[7]=[l("安装运行常见问题")])),_:1})]),e[11]||(e[11]=i("p",null,[i("a",{href:"https://www.kdocs.cn/l/cbSJUUNotJ3Z",target:"_blank",rel:"noopener noreferrer"},"常见问题和解决方案")],-1))])}const k=s(h,[["render",p],["__file","quickstart.html.vue"]]),b=JSON.parse('{"path":"/sr/zh/quickstart.html","title":"崩坏：星穹铁道 一条龙 快速开始","lang":"zh-CN","frontmatter":{"lang":"zh-CN","title":"崩坏：星穹铁道 一条龙 快速开始","description":"重要 请认真阅读本页面，可以帮助你顺利完成安装，减少浪费时间。 1.安装 脚本请存放在 全英文的路径 下 1.1.使用安装器（推荐） 如果你不懂得如何搭建python环境，请使用本方法。 如果出现安装依赖失败，且你的电脑上曾经安装过anaconda，则可以卸载后anaconda重试本方法，或者使用 1.2 方法。 从 最新 Release 中下载 St...","head":[["meta",{"property":"og:url","content":"https://one-dragon.org/sr/zh/quickstart.html"}],["meta",{"property":"og:site_name","content":"一条龙小助手"}],["meta",{"property":"og:title","content":"崩坏：星穹铁道 一条龙 快速开始"}],["meta",{"property":"og:description","content":"重要 请认真阅读本页面，可以帮助你顺利完成安装，减少浪费时间。 1.安装 脚本请存放在 全英文的路径 下 1.1.使用安装器（推荐） 如果你不懂得如何搭建python环境，请使用本方法。 如果出现安装依赖失败，且你的电脑上曾经安装过anaconda，则可以卸载后anaconda重试本方法，或者使用 1.2 方法。 从 最新 Release 中下载 St..."}],["meta",{"property":"og:type","content":"article"}],["meta",{"property":"og:locale","content":"zh-CN"}],["meta",{"property":"og:updated_time","content":"2024-11-11T11:07:22.000Z"}],["meta",{"property":"article:modified_time","content":"2024-11-11T11:07:22.000Z"}],["script",{"type":"application/ld+json"},"{\\"@context\\":\\"https://schema.org\\",\\"@type\\":\\"Article\\",\\"headline\\":\\"崩坏：星穹铁道 一条龙 快速开始\\",\\"image\\":[\\"\\"],\\"dateModified\\":\\"2024-11-11T11:07:22.000Z\\",\\"author\\":[{\\"@type\\":\\"Person\\",\\"name\\":\\"DoctorReid\\",\\"url\\":\\"https://one-dragon.org\\"}]}"]]},"headers":[{"level":2,"title":"1.安装","slug":"_1-安装","link":"#_1-安装","children":[{"level":3,"title":"1.1.使用安装器（推荐）","slug":"_1-1-使用安装器-推荐","link":"#_1-1-使用安装器-推荐","children":[]},{"level":3,"title":"1.2.使用安装器 + 已有的 anaconda（推荐）","slug":"_1-2-使用安装器-已有的-anaconda-推荐","link":"#_1-2-使用安装器-已有的-anaconda-推荐","children":[]},{"level":3,"title":"1.3.使用源码运行","slug":"_1-3-使用源码运行","link":"#_1-3-使用源码运行","children":[]}]},{"level":2,"title":"2.使用前须知","slug":"_2-使用前须知","link":"#_2-使用前须知","children":[]},{"level":2,"title":"3.常见问题","slug":"_3-常见问题","link":"#_3-常见问题","children":[]}],"git":{"createdTime":1725171740000,"updatedTime":1731323242000,"contributors":[{"name":"DoctorReid","username":"DoctorReid","email":"doctorreid2024@outlook.com","commits":17,"url":"https://github.com/DoctorReid"},{"name":"idk500","username":"idk500","email":"mr.fc@qq.com","commits":1,"url":"https://github.com/idk500"}]},"readingTime":{"minutes":3.55,"words":1064},"filePathRelative":"sr/zh/quickstart.md","localizedDate":"2024年9月1日","autoDesc":true}');export{k as comp,b as data};
