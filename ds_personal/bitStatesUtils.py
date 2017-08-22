#coding=utf-8
"""用户绑定手机号码状态"""
def OP_BIND_PHONE():
    return 1L << 0
"""用户绑定邮箱状态"""
def OP_BIND_EMAIL():
    return 1L << 1
"""用户填写基本资料"""
def OP_BASIC_INFO():
    return 1L << 2
"""用户是否已经实名认证"""
def OP_REAL_AUTH():
    return 1L << 3
"""用户是否已经视频认证"""
def OP_VIDEO_AUTH():
    return 1L << 4
"""用户是否已经有一个借款申请在申请流程中"""
def OP_HAS_BIDREQUEST_PROCESS():
    return 1L << 5
"""用户是否已经绑定了银行卡"""
def OP_HAS_BIND_BANK():
    return 1L << 6
"""用户是否有提现在审核流程中"""
def OP_HAS_WITHDRAY_PROCESS():
    return 1L << 7

"""
判断状态state
states:所有状态值
value:需要判断状态值
"""
def hasState(states,value):
    return (states & value) != 0

"""
添加状态值
states:所有状态值
value:需要判断状态值
"""
def addState(states,value):
    if hasState(states,value):
        return states
    return (states | value)

"""
移除状态值
states:所有状态值
value:需要判断状态值
"""
def removeState(states,value):
    if hasState(states,value):
        return states ^ value
    return states