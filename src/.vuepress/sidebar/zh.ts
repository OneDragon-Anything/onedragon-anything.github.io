import { sidebar } from "vuepress-theme-hope";

export const zhSidebar = sidebar({
  "/sr/zh/": [
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
    }
  ],
  "/zzz/zh/": [
    {
      text: "简介",
      icon: "home",
      link: "home",
    },
    {
      text: "快速开始",
      icon: "rocket",
      link: "quickstart",
    },
    {
      text: "常见问题",
      icon: "question",
      link: "faq",
    },
    {
      text: "功能说明",
      icon: "lightbulb",
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
          text: "功能-零号空洞-枯萎之都",
          link: "feat_hollow_zero"
        },
        {
          text: "功能-锄大地",
          link: "feat_world_patrol"
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
        },
      ],
    },
    {
      text: "自动战斗教程",
      icon: "book",
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
        },
        {
          text: "冷知识",
          link: "other/battle_knowledge",
        }
      ]
    }
  ],
  "/zzz/zh/auto_battle_guide/basic/":[
    {
      text: "00-Yaml格式",
      link: "basic_00_yaml",
    },
    {
      text: "01-自动战斗简介",
      link: "basic_01_intro",
    },
    {
      text: "02-场景",
      link: "basic_02_scenes",
    },
    {
      text: "03-场景下的触发器",
      link: "basic_03_triggers",
    },
    {
      text: "04-场景下的处理方法",
      link: "basic_04_handlers",
    },
    {
      text: "05-状态表达式",
      link: "basic_05_states",
    },
    {
      text: "06-操作指令数组",
      link: "basic_06_operations",
    },
    {
      text: "90-状态枚举",
      link: "basic_90_states_enum",
    },
  ],
  "/zzz/zh/auto_battle_guide/zhu_yuan/":[
    {
      text: "01-确定站场角色",
      link: "zhu_yuan_01",
    },
    {
      text: "02-角色连招",
      link: "zhu_yuan_02",
    },
    {
      text: "03-连携与快速支援",
      link: "zhu_yuan_03",
    },
  ],
  "/zzz/zh/auto_battle_guide/character_special/":[
    {
      text: "莱特",
      link: "lighter",
    }
  ]
});
