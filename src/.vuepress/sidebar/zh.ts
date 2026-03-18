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
      text: "项目简介",
      icon: "home",
      link: "home",
    },
    {
      text: "快速开始",
      icon: "rocket",
      link: "quickstart",
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
      children: [
        {
          text: "功能-战斗助手",
          link: "feat_battle_assistant"
        },
        {
          text: "功能-一条龙",
          collapsible: true,
          children: [
            {
              text: "快速开始",
              link: "feat_one_dragon/quickstart"
            },
            {
              text: "随便观",
              link: "feat_one_dragon/suibian"
            },
            {
              text: "恶名狩猎计划",
              link: "feat_one_dragon/notorious_hunt"
            },
            {
              text: "体力计划",
              link: "feat_one_dragon/charge_plan"
            },
            {
              text: "咖啡计划",
              link: "feat_one_dragon/coffee"
            },
            {
              text: "零号空洞",
              link: "feat_one_dragon/hollow_zero"
            },
            {
              text: "锄大地",
              link: "feat_one_dragon/world_patrol"
            },
            {
              text: "式舆防卫战",
              link: "feat_one_dragon/shiyu_defense"
            },
          ]
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
          text: "基础教程",
          collapsible: true,
          prefix: "basic/",
          children: [
            {
              text: "00-自动战斗简介",
              link: "basic_00_intro",
            },
            {
              text: "01-YAML格式",
              link: "basic_01_yaml",
            },
            {
              text: "02-场景",
              link: "basic_02_scenes",
            },
            {
              text: "03-触发条件",
              link: "basic_03_triggers",
            },
            {
              text: "04-处理方法",
              link: "basic_04_handlers",
            },
            {
              text: "05-状态表达式",
              link: "basic_05_states",
            },
            {
              text: "06-操作指令",
              link: "basic_06_operations",
            },
            {
              text: "07-模板系统",
              link: "basic_07_templates",
            },
          ]
        },
        {
          text: "参考手册",
          collapsible: true,
          prefix: "reference/",
          children: [
            {
              text: "状态枚举",
              link: "states_enum",
            },
            {
              text: "内置战斗配置",
              link: "battle_configs",
            },
            {
              text: "架构解析-全配队通用",
              link: "architecture",
            },
            {
              text: "建议与调试",
              link: "tips_and_debug",
            },
          ]
        },
        {
          text: "实战教程",
          collapsible: true,
          prefix: "tutorial/",
          children: [
            {
              text: "01-确定站场角色-朱鸢",
              link: "zhu_yuan_01",
            },
            {
              text: "02-角色连招-朱鸢",
              link: "zhu_yuan_02",
            },
            {
              text: "03-连携与快速支援-朱鸢",
              link: "zhu_yuan_03",
            },
            {
              text: "角色连招示例",
              link: "intro",
            },
          ]
        },
        {
          text: "冷门知识",
          link: "other/battle_knowledge",
        }
      ]
    },
    {
      text: "贡献&开发",
      icon: "code-branch",
      prefix: "dev",
      children: [
        {
          text: "说明",
          link: "contribution",
        },
        {
          text: "路线图",
          link: "roadmap",
        }
      ]
    }
  ],
});
