<!--
2023/3/28
-->

1. QX:
    1. 添加rewrite资源:
        ```
        https://raw.githubusercontent.com/chouchoui/QuanX/master/Scripts/testflight/testflight.key.snippet
        ```
    2. 如果打不开网页, 需要继续添加rewrite资源:
        ```
        https://raw.githubusercontent.com/chavyleung/scripts/master/box/rewrite/boxjs.rewrite.quanx.tf.conf
        ```
    3. 添加task: 编辑🔜[task_local], 添加:
        ```
        task local:*/10 * * * * * https://raw.githubusercontent.com/chouchoui/QuanX/master/Scripts/testflight/Auto_join_TF.js, tag=TestFlight自动加入, img-url= https://raw.githubusercontent.com/Orz-3/mini/master/Color/testflight.png, enabled=true
        ```
2. 进入网页www.boxjs.com, 点击右上角的设置, 然后添加订阅
    ```
    https://raw.githubusercontent.com/githubdulong/Script/master/boxjs.json
    ```
3. 挂起QX,进入testflight自动获取apple id
4. 结合以下网址python自动获取testflight邀请码填入boxjs
    >https://github.com/pluwen/awesome-testflight-link
5. 补充testflight邀请码
    1. 微信键盘:
    2. 京东云: