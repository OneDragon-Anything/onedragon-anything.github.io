import { navbar } from "vuepress-theme-hope";

export const zhNavbar = navbar([
  "/",
  {
    text: "崩坏：星穹铁道",
    icon: "train",
    prefix: "/sr/zh",
    children: [
      {
        text: "简介",
        icon: "home",
        link: "home"
      },
      {
        text: "快速安装",
        icon: "rocket",
        link: "quickstart"
      },
      {
        text: "功能说明",
        icon: "lightbulb",
        link: "docs/feat_one_dragon"
      },
    ]
  },
  {
    text: "绝区零",
    icon: "z",
    prefix: "/zzz/zh",
    children: [
      {
        text: "项目简介",
        icon: "home",
        link: "home"
      },
      {
        text: "快速开始",
        icon: "rocket",
        link: "quickstart",
      },
      {
        text: "界面导航",
        icon: "display",
        link: "gui_guide",
      },
      {
        text: "必要设置",
        icon: "triangle-exclamation",
        link: "config",
      },
      {
        text: "常见问题",
        icon: "question",
        link: "faq",
      },
      {
        text: "功能说明",
        icon: "lightbulb",
        link: "feat/feat_one_dragon/onedragon"
      },
      {
        text: "设置说明",
        icon: "gear",
        link: "setting/setting_game"
      },
      {
        text: "自动战斗教程",
        icon: "book",
        link: "auto_battle_guide/basic/basic_00_intro"
      },
    ],
  },
  {
    text: "开发",
    icon: "code-branch",
    prefix: "/dev/zh",
    children: [
      {
        text: "简介",
        icon: "home",
        link: "home"
      },
      {
        text: "概念说明",
        icon: "lightbulb",
        link: "concept"
      },
      {
        text: "路线图",
        icon: "route",
        link: "roadmap"
      },
      {
        text: "贡献&开发",
        icon: "code-branch",
        link: "contribution"
      }
    ]
  },
  {
    text: "小工具",
    prefix: "/tools/zh",
    children: [
      {
        text: "千机链",
        icon: "link",
        link: "script_chainer"
      }
    ]
  },
  {
    text: "其它",
    prefix: "/other/zh",
    children: [
      {
        text: "安装运行常见问题",
        icon: "question",
        link: "common_qa"
      },
      {
        text: "Github访问指南",
        icon: "globe",
        link: "visit_github"
      },
      {
        text: "默认管理员启动",
        icon: "user-tie",
        link: "run_as_admin_by_default"
      },
      {
        text: "Windows任务计划程序",
        icon: "clock",
        link: "windows_plan"
      }
    ]
  },
  {
    text: "点赞",
    prefix: "/like",
    children: [
      {
        text: "点赞",
        icon: "heart",
        link: "like"
      },
      {
        text: "2025赞赏感谢",
        icon: "heart",
        link: "thanks_2025"
      },
      {
        text: "2024赞赏感谢",
        icon: "heart",
        link: "thanks_2024"
      }
    ]
  }
]);
