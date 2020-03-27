修改 models.py 后，需要同步到数据库

```shell
python manage.py makemigrations
python manage.py migrate
```

数据库初始化数据
需要在 app 目录下新建 fixtures 文件夹，然后新建 initial_data.json 文件保存初始化数据
数据格式如下：

```json
[
  {
    "model": "backend.ApiGroup",
    "pk": 1,
    "fields": {
      "parentApiGroupId": "0",
      "projId": 0,
      "apiGroupName": "默认分组",
      "isEdit": false
    }
  }
]
```

然后执行命令插入数据到数据库

```shell
python manage.py loaddata initial_data.json
```
