# 学习通课程视频自动观看脚本

**1⃣️.安装 selenium：**
  ```
  pip3 install selenium
  ```

**2⃣️.下载Edge远程自动化驱动(edgedriver)并配置**

  1.[下载与你的Edge版本相应的 edgedriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

  2.修改`main.py`

  ```
  service = Service('PATH')
  ```
  `PATH`为 edgedriver 路径

**3⃣️.运行`main.py`**

  根据提示扫码登录，然后在脚本终端输入要开始操作的首个视频链接

  注意：

  1.尽量保持自动打开的浏览器最大化

  2.不要操作自动打开的浏览器（可以将页面静音）
  
  3.不要在别的浏览器或者手机客户端播放视频，否则学习通会检测到多个设备同时在学习。

  4.建议新建一个桌面，把自动打开的浏览器和脚本终端放进去，此时可以做其他事情。
