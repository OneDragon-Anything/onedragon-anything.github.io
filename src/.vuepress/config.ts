import {defineUserConfig} from "vuepress";
import { viteBundler } from "@vuepress/bundler-vite";
import {googleAnalyticsPlugin} from '@vuepress/plugin-google-analytics'

import theme from "./theme.js";

const zhLocale = {
  lang: "zh-CN",
  title: "一条龙小助手",
};

export default defineUserConfig({
  base: "/",

  bundler: viteBundler({
    viteOptions: {
      css: {
        preprocessorOptions: {
          scss: {
            silenceDeprecations: ["if-function"],
          },
          sass: {
            silenceDeprecations: ["if-function"],
          },
        },
      },
    },
    vuePluginOptions: {
      template: {
        compilerOptions: {
          isCustomElement: (tag) => tag === "font",
        },
      },
    },
  }),

  locales: {
    "/": zhLocale,
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
