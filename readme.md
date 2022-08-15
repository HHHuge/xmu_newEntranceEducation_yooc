## 食用指南

执行 ```python query.py```后, 脚本监控ctrl+c快捷键, 在答题时复制题目内容, 脚本自动在题库中搜索, 返回含有选中内容的题目及答案.
如果无法在网页端完成复制, 建议配合 Tampermonkey 的解除网页限制脚本食用.

### 题库更新
1. 保存cookies.txt.
   保存格式为 Netscape HTTP Cookie File
2. 脚本中修改 record.txt 的 url 到 yooc 考试答案的网址.
3. 执行 ```python record.txt```, 完成添加题库.
