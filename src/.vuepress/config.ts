import {defineUserConfig} from "vuepress";
import {googleAnalyticsPlugin} from '@vuepress/plugin-google-analytics'

import theme from "./theme.js";

export default defineUserConfig({
  base: "/",

  locales: {
    "/": {
      lang: "zh-CN",
      title: "一条龙小助手",
    },
    "/zzz/": {
      lang: "zh-CN",
      title: "一条龙小助手",
    },
    "/sr/": {
      lang: "zh-CN",
      title: "一条龙小助手",
    },
  },

  theme,

  plugins: [
    googleAnalyticsPlugin({
      id: "G-95Y9L1MPG1",
    }),
  ],
  // Enable it with pwa
  // shouldPrefetch: false,
});
