# XJTUclassroom
一个简单的[西交ehall](ehall.xjtu.edu.cn)爬虫，用于获取空闲教室\
基于 requests + selenium\
简单配置后运行 `main.py` 即可，可用于设置定时任务\
获取结果保存在 `empty_class.json` 中

# Requirements
selenium（用于自动获取cookie）

# Set-up
* 在 `main.py` 中分别将账号密码赋值到 `username` 和 `password`，还可以自定义查询日期和教学楼（默认查询今天，所有主楼）。
* 在 `GetCookie.py` 中修改 `driver_path` ，根据浏览器选择 `driver` 。
