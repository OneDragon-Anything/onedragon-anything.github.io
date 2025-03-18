import{_ as r}from"./plugin-vue_export-helper-DlAUqK2U.js";import{c as i,a as e,b as d,d as a,e as o,f as n,r as s,o as p}from"./app-PZqzuEQN.js";const h={};function c(m,t){const l=s("RouteLink");return p(),i("div",null,[t[5]||(t[5]=e("p",null,[a("战斗助手目前主要包含 "),e("code",null,"闪避助手"),a(", "),e("code",null,"自动战斗"),a("，其底层都是指令的配置，可以参考以下文档编写适合自己配队的指令。")],-1)),e("ul",null,[e("li",null,[o(l,{to:"/zzz/zh/auto_battle_guide/zhu_yuan/zhu_yuan_01.html"},{default:n(()=>t[0]||(t[0]=[a("朱鸢示例教程(新)(未完成)")])),_:1})]),e("li",null,[o(l,{to:"/zzz/zh/auto_battle_guide/basic/basic_00_yaml.html"},{default:n(()=>t[1]||(t[1]=[a("自定义指令基础(新)(未完成)")])),_:1})]),e("li",null,[o(l,{to:"/zzz/zh/docs/feat_custom_op.html"},{default:n(()=>t[2]||(t[2]=[a("自定义指令介绍(旧)")])),_:1})])]),t[6]||(t[6]=d('<h2 id="_0-使用前需知" tabindex="-1"><a class="header-anchor" href="#_0-使用前需知"><span>0.使用前需知</span></a></h2><p>使用本页说明的功能时，建议进行以下设置：</p><ul><li>游戏中给普通攻击设置一个键盘按键，脚本中使用键盘的按键进行控制。因为默认鼠标左键也是连携按键，可能会打乱自动战斗的连携。</li><li>同理，给特殊技和爆发技设置鼠标侧键，脚本中使用鼠标侧键进行控制，可以避免打乱自动战斗的连携。</li><li>以上按键可根据自己习惯调整，重点是，让脚本使用的按键避免重复，防止在按某个按键时触发了另一个操作。</li><li>游戏中开启 <code>手动连携技</code>，这样才能使用取消连携功能。</li></ul><h2 id="_1-闪避助手" tabindex="-1"><a class="header-anchor" href="#_1-闪避助手"><span>1.闪避助手</span></a></h2><p>主要用于帮助大家日常过剧情、活动、深渊时，可以辅助闪避，降低游戏难度。</p><p>目前结合了 画面识别 和 <a href="https://github.com/ImLaoBJie/ZZZSoundTrigger" target="_blank" rel="noopener noreferrer">声音识别</a></p><p>如果觉得好用，可以给原项目点赞。</p><h3 id="_1-1-默认配置文件" tabindex="-1"><a class="header-anchor" href="#_1-1-默认配置文件"><span>1.1.默认配置文件</span></a></h3><p>闪避助手的配置文件，放置在 <code>config/dodge</code> 文件夹下。</p><table><thead><tr><th>配置文件</th><th>作用</th></tr></thead><tbody><tr><td>本-格挡.sample.yml</td><td><code>本·比格</code> 专用，使用 <code>特殊攻击</code> 进行格挡</td></tr><tr><td>闪避.sample.yml</td><td>闪避之后进行一次普通攻击</td></tr><tr><td>切换角色-下一个.sample.yml</td><td>黄光时切换到<code>下一个</code>角色后进行一次普通攻击；红光时闪避之后进行一次普通攻击</td></tr><tr><td>切换角色-强攻.sample.yml</td><td>黄光时切换到<code>强攻</code>角色后进行一次普通攻击；红光时闪避之后进行一次普通攻击</td></tr><tr><td>闪A切下一个.sample.yml</td><td>黄光时闪避 -&gt; 普通攻击 -&gt; 切换到下一个角色 -&gt; 普通攻击；红光时闪避之后进行一次普通攻击</td></tr><tr><td>闪A切强攻.sample.yml</td><td>黄光时闪避 -&gt; 普通攻击 -&gt; 切换到强攻角色 -&gt; 普通攻击；红光时闪避之后进行一次普通攻击</td></tr></tbody></table><h3 id="_1-2-修改配置文件" tabindex="-1"><a class="header-anchor" href="#_1-2-修改配置文件"><span>1.2.修改配置文件</span></a></h3><p>你可以复制样例文件后进行修改，复制后文件名不要使用 <code>.sample.yml</code> 后缀即可，因为这种会被作者内容覆盖。</p><p>另外：由于作者更新的默认配置无法覆盖你的个人配置，如果你觉得你自己的配置不好用，或者改崩了，想恢复原来的，把自己的配置文件删掉即可，脚本就能读取到默认配置文件。</p><p>通常修改有以下方面</p><ul><li>不同的角色需要的按键间隔不同，所以默认的配置未必适用所有情况。</li><li>可以通过修改使得切换上一个角色或者切换到击破角色。</li><li>判断前台角色是击破或者强攻后只闪避不格挡。</li></ul><h3 id="_1-3-手柄支持" tabindex="-1"><a class="header-anchor" href="#_1-3-手柄支持"><span>1.3.手柄支持</span></a></h3>',16)),e("p",null,[t[4]||(t[4]=a("见 ")),o(l,{to:"/zzz/zh/docs/feat_gamepad.html"},{default:n(()=>t[3]||(t[3]=[a("手柄支持")])),_:1})]),t[7]||(t[7]=d('<h3 id="_1-4-漏判误判" tabindex="-1"><a class="header-anchor" href="#_1-4-漏判误判"><span>1.4.漏判误判</span></a></h3><p>相关情况可以到 <a href="https://github.com/DoctorReid/ZenlessZoneZero-OneDragon/issues/new?assignees=&amp;labels=bug&amp;projects=&amp;template=02-bug-dodge-assistant.yml&amp;title=%5B%E9%97%AE%E9%A2%98%E5%8F%8D%E9%A6%88%5D+%5B%E9%97%AA%E9%81%BF%E5%8A%A9%E6%89%8B%5D+" target="_blank" rel="noopener noreferrer">这里</a> 反馈。请注明副本方便作者复现。</p><p>你也可以使用脚本的【开发工具】-【截图助手】，截取有问题的游戏截图后打包发给作者，截图会保存在 <code>.debug/images</code> 中。</p><ul><li>漏判 ( 出现了黄光/红光，但脚本没有识别到 ) : 可以在出现后手动按钮触发截图保存。</li><li>误判 ( 没有出现黄光/红光，但脚本误认为出现了，造成乱闪避 ) : 打开【闪避检测】，脚本会自动把认为有光的图保存下来。</li></ul><h2 id="_2-自动战斗" tabindex="-1"><a class="header-anchor" href="#_2-自动战斗"><span>2.自动战斗</span></a></h2><p>自动战斗目前作用于一条龙刷本，也可以在【战斗助手】中单独使用。</p><h3 id="_2-1-默认配置" tabindex="-1"><a class="header-anchor" href="#_2-1-默认配置"><span>2.1.默认配置</span></a></h3><p>自动战斗的配置文件存放在 <code>config/auto_battle</code> 文件夹下。</p><p>注意自动战斗配置大部分都有角色站位要求，可以在「战斗助手」-「配置编辑」中选择文件查看。这里出现的配队才有适配的战斗逻辑，使用其他配队可能各种问题。</p><p>默认的「全配队通用」 应该就能应对大部分场景。</p><h3 id="_2-2-自定义指令" tabindex="-1"><a class="header-anchor" href="#_2-2-自定义指令"><span>2.2.自定义指令</span></a></h3><p>目前脚本提供的默认配置较少，你也可以在QQ群里找找其他人的分享。</p><p>如果有自己修改了觉得好用的配置，欢迎提交PR。</p>',13))])}const g=r(h,[["render",c],["__file","feat_battle_assistant.html.vue"]]),f=JSON.parse('{"path":"/zzz/zh/docs/feat_battle_assistant.html","title":"功能-战斗助手","lang":"zh-CN","frontmatter":{"lang":"zh-CN","title":"功能-战斗助手","description":"战斗助手目前主要包含 闪避助手, 自动战斗，其底层都是指令的配置，可以参考以下文档编写适合自己配队的指令。 0.使用前需知 使用本页说明的功能时，建议进行以下设置： 游戏中给普通攻击设置一个键盘按键，脚本中使用键盘的按键进行控制。因为默认鼠标左键也是连携按键，可能会打乱自动战斗的连携。 同理，给特殊技和爆发技设置鼠标侧键，脚本中使用鼠标侧键进行控制，可...","head":[["meta",{"property":"og:url","content":"https://one-dragon.org/zzz/zh/docs/feat_battle_assistant.html"}],["meta",{"property":"og:site_name","content":"一条龙小助手"}],["meta",{"property":"og:title","content":"功能-战斗助手"}],["meta",{"property":"og:description","content":"战斗助手目前主要包含 闪避助手, 自动战斗，其底层都是指令的配置，可以参考以下文档编写适合自己配队的指令。 0.使用前需知 使用本页说明的功能时，建议进行以下设置： 游戏中给普通攻击设置一个键盘按键，脚本中使用键盘的按键进行控制。因为默认鼠标左键也是连携按键，可能会打乱自动战斗的连携。 同理，给特殊技和爆发技设置鼠标侧键，脚本中使用鼠标侧键进行控制，可..."}],["meta",{"property":"og:type","content":"article"}],["meta",{"property":"og:locale","content":"zh-CN"}],["meta",{"property":"og:updated_time","content":"2024-12-26T02:56:53.000Z"}],["meta",{"property":"article:modified_time","content":"2024-12-26T02:56:53.000Z"}],["script",{"type":"application/ld+json"},"{\\"@context\\":\\"https://schema.org\\",\\"@type\\":\\"Article\\",\\"headline\\":\\"功能-战斗助手\\",\\"image\\":[\\"\\"],\\"dateModified\\":\\"2024-12-26T02:56:53.000Z\\",\\"author\\":[{\\"@type\\":\\"Person\\",\\"name\\":\\"DoctorReid\\",\\"url\\":\\"https://one-dragon.org\\"}]}"]]},"headers":[{"level":2,"title":"0.使用前需知","slug":"_0-使用前需知","link":"#_0-使用前需知","children":[]},{"level":2,"title":"1.闪避助手","slug":"_1-闪避助手","link":"#_1-闪避助手","children":[{"level":3,"title":"1.1.默认配置文件","slug":"_1-1-默认配置文件","link":"#_1-1-默认配置文件","children":[]},{"level":3,"title":"1.2.修改配置文件","slug":"_1-2-修改配置文件","link":"#_1-2-修改配置文件","children":[]},{"level":3,"title":"1.3.手柄支持","slug":"_1-3-手柄支持","link":"#_1-3-手柄支持","children":[]},{"level":3,"title":"1.4.漏判误判","slug":"_1-4-漏判误判","link":"#_1-4-漏判误判","children":[]}]},{"level":2,"title":"2.自动战斗","slug":"_2-自动战斗","link":"#_2-自动战斗","children":[{"level":3,"title":"2.1.默认配置","slug":"_2-1-默认配置","link":"#_2-1-默认配置","children":[]},{"level":3,"title":"2.2.自定义指令","slug":"_2-2-自定义指令","link":"#_2-2-自定义指令","children":[]}]}],"git":{"createdTime":1725184952000,"updatedTime":1735181813000,"contributors":[{"name":"DoctorReid","username":"DoctorReid","email":"doctorreid2024@outlook.com","commits":8,"url":"https://github.com/DoctorReid"}]},"readingTime":{"minutes":3.91,"words":1173},"filePathRelative":"zzz/zh/docs/feat_battle_assistant.md","localizedDate":"2024年9月1日","autoDesc":true}');export{g as comp,f as data};
