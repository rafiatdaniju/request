from src.request import ResqreApi

# d='https://reqres.in/api/users?'
d='https://reqres.in/api/unknown/'
me=ResqreApi()
print(me.resource(d,'id',5))
print(me.resource(d,'id',2))
print(me.resource(d,'name','fuchsia rose'))