# seebug_crawler
一点关于知道创宇 Seebug 漏洞平台反反爬的研究, 成功通过非webdriver的方式获取cookies

必须携带合法的cookies访问网站才会正常返回内容, 否则服务器返回521
![image](https://user-images.githubusercontent.com/8842321/146194417-8a599503-326b-4c7a-9521-fd35c33e0480.png)

+ 第一步由__jsluid_s 获取__jsl_clearance_s=, 通过第一步请求返回的 js(称 js1)计算而来, js1 可以 execjs 直接跑
+ 第二步更新__jsl_clearance_s=, 由带__jsluid_s 和旧的__jsl_clearance_s 请求返回的 js(称 js2)计算而来
+ js2 主要功能有检测浏览器是否为 webdriver 等等, 以及更新__jsl_clearance_s
+ 更新 js2 的算法目前发现有 md5, sha1, sha256, 具体哪种由服务器随机返回, 本人仅实现sha256, 其它应该差不多吧(
+ js2 经过一些人肉反混淆后也能 execjs 跑, 主要是那个 hash 函数
+ 3.js 为部分人肉处理后的结果, 懒得整了, 又不是不能用(

仅供学习交流，禁止用于其他用途
