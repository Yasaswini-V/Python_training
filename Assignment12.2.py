def supress_exception(exception,result):
        def decorator(fn):
            def inner(*args,**kwargs):
                try:
                    result1=fn(*args,**kwargs)
                    return result1
                except exception:
                    return result
            return inner
        return decorator

@supress_exception(exception=KeyError,result=False)
def authentication(user,pwsd):
    users=dict(yassu="yassu@123",rama="rama@123")
    return users[user]==pwsd

print(authentication("yassu","yassu@123"))
print(authentication("deepu","deepu@123"))
print(authentication("Yassu@123"))