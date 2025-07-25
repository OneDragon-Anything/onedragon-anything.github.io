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
        prefix: "docs",
        children: [
          {
            text: "功能-一条龙",
            link: "feat_one_dragon"
          },
          {
            text: "功能-锄大地",
            link: "feat_world_patrol"
          },
          {
            text: "功能-模拟宇宙",
            link: "feat_sim_uni"
          }
        ]
      },
      {
        text: "贡献&开发",
        prefix: "dev",
        children: [
          {
            text: "说明",
            link: "contribution",
          }
        ]
      }
    ]
  },
  {
    text: "绝区零",
    icon: "z",
    prefix: "/zzz/zh",
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
      text: "常见问题",
      icon: "question",
      link: "faq",
      },
      {
      text: "快速开始",
      icon: "rocket",
      link: "quickstart",
      },
      {
        text: "功能说明",
        prefix: "docs",
        children: [
          {
            text: "⚠︎必要设置-必读⚠︎",
            link: "config"
          },
          {
            text: "功能-战斗助手",
            link: "feat_battle_assistant"
          },
          {
            text: "功能-一条龙",
            link: "feat_one_dragon"
          },
          {
            text: "功能-零号空洞-迷失之地",
            link: "feat_lost_void"
          },
          {
            text: "功能-游戏助手",
            link: "feat_game_assistant"
          },
          {
          text: "功能-通知系统",
          link: "feat_notify"
          },
          {
            text: "功能-手柄支持",
            link: "feat_gamepad"
          }
        ]
      },
      {
        text: "自动战斗教程",
        prefix: "auto_battle_guide",
        children: [
          {
            text: "基础",
            link: "basic/basic_00_yaml",
          },
          {
            text: "功能-自定义指令",
            link: "feat_custom_op"
          },
          {
            text: "朱鸢示例",
            link: "zhu_yuan/zhu_yuan_01",
          },
          {
            text: "角色连招示例",
            link: "character_special/intro",
          }
        ]
      },
      {
        text: "贡献&开发",
        prefix: "dev",
        children: [
          {
            text: "说明",
            link: "contribution",
          }
        ]
      }
    ],
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
    prefix: "/other/zh/like",
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
