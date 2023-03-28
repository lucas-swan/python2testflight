# 2023/3/28
1. 重写应用boxjs:https://raw.githubusercontent.com/chouchoui/QuanX/master/Scripts/testflight/testflight.key.snippet
打不开boxjs的把这个也加上:https://raw.githubusercontent.com/chavyleung/scripts/master/box/rewrite/boxjs.rewrite.quanx.tf.conf
2. boxjs订阅:https://raw.githubusercontent.com/githubdulong/Script/master/boxjs.json
3. 
```
task local:*/10 * * * * * https://raw.githubusercontent.com/chouchoui/QuanX/master/Scripts/testflight/Auto_join_TF.js, tag=TestFlight自动加入, img-url= https://raw.githubusercontent.com/Orz-3/mini/master/Color/testflight.png, enabled=true
```

> https://github.com/pluwen/awesome-testflight-link