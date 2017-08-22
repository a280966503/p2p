class MyJson():
    def myJson(isSuccess,msg):
        context={'success':isSuccess,'msg':msg}
        return context
    def myJson(isSuccess,msg,data):
        context={'success':isSuccess,'msg':msg,'data':data}
        return context