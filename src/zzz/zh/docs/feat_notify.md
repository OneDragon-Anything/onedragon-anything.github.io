---
lang: zh-CN
title: 功能-通知
---

::: important

- 如果查看了本文档仍旧无法解决你的问题，可以在[Issue](https://github.com/OneDragon-Anything/ZenlessZoneZero-OneDragon/issues)查阅是否有相似问题，如果无相似问题可以通过Issue提问。

:::

---
此页面施工中...
---

### Server酱APP
Server酱有两种版本，Server酱软件 和 第三方软件推送版  
APP版每天无推送上限，需要[下载APP](https://sc3.ft07.com/client)  
第三方推送版只需要在[官网](https://sc3.ft07.com/)绑定你的 微信/钉钉/飞书 即可  

绑定或下载后，可以获取一个通知url，填入一条龙软件内即可直接使用

### webhook
- `URL`: 你的 webhook 地址
- `BODY`: 通知内容  
BODY例子 具体格式根据你的 webhook 要求来  
$title 和 $content 作为标题和内容的占位符可以直接调用  
```
{
"title":"$title",
"content":"$content"
}
```
- `HEADERS`: 请求头 一般用于给你填写 key  
例: "Authorization": "Bearer your_token"  
- `METHOD`: get或post 一般使用post
- `CONTENT-TYPE`: 请求格式 需要和你的body保持一致  
例: application/json