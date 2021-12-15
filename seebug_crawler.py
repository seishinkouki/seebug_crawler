import json
import requests
import execjs
import hashh
url = "https://www.seebug.org/"

my_session = requests.session()
my_session.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                                         "like Gecko) Chrome/75.0.3770.100 Safari/537.36"})

# 第一步由__jsluid_s获取__jsl_clearance_s=, 通过第一步请求返回的js(称js1)计算而来
r = my_session.get(url).text.replace("<script>document.cookie=", "").replace(";location.href=location.pathname+location.search</script>", "")
default = execjs.get()
res = default.eval(r)
print(res)

# 第二步更新__jsl_clearance_s=, 由带__jsluid_s和旧的__jsl_clearance_s请求返回的js(称js2)计算而来
# js2 主要功能有检测是否为webdriver等等, 以及更新__jsl_clearance_s
# 更新js2 的算法目前发现有md5, sha1, sha256, 具体哪种由服务器随机返回, 目前仅实现sha256, 其它应该差不多
my_session.headers.update({"Cookie": "__jsluid_s" + "=" + my_session.cookies.get("__jsluid_s") + ";" + res})
r = my_session.get(url)
print(r.text)
go_para = json.loads(r.text.split("}};go(")[1].replace(")</script>", ""))
print(go_para)

print("len(aaa):", len(go_para['chars']), "ct:", go_para['ct'], "ha:", go_para['ha'])

if go_para['ha'] == "sha256":
    for i in range(0, len(go_para['chars'])):
        for j in range(0, len(go_para['chars'])):
            if hashh.gethash(go_para['bts'][0] + go_para['chars'][i] + go_para['chars'][j] + go_para['bts'][1]) == go_para['ct']:
                new_jslll = go_para['bts'][0] + go_para['chars'][i] + go_para['chars'][j] + go_para['bts'][1]
                print(new_jslll)
                my_session.headers.update({"Cookie": "__jsluid_s" + "=" + my_session.cookies.get("__jsluid_s") + ";" + "__jsl_clearance_s=" + new_jslll + ";max-age=3600;path=/"})
                r = my_session.get(url)
                print(r.text)
                break
        else:
            continue
        break
