#安检器
name = input("Hi,你叫什么名字？")
namelist = [ '王思翰' , '王靖' , '余杨' ]
if name == namelist[0] or name == namelist[1] or name == namelist[2]:
    print("你好！", name, "，欢迎来到父女节大会！")
else:
    print( "禁止参加父女节大会，快走开！")