# -*- coding:utf-8 -*-
role_dict = {
    "superuser": 0,
    "common_user": 1,
    "product": 2,
    "user": 3,
    "acl": 4
}

period_status = {
    0: "创建中",
    1: "创建完成",
    2: "运行中",
    3: "完成",
    4: "失败",
    5: "被暂停",
    6: "等待周期",
    7: "第%s组运行中",
    8: "第%s组完成"
}

period_audit = {
    0: "创建了Job",
    1: "重开了Job",
    2: "继续了Job",
    3: "完成了Job",
    4: "失败了Job",
    5: "暂停了Job",
    7: "第%s组开始",
    8: "第%s组完成",
    9: "全部开始"
}