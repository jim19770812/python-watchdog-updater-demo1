# d.py
def hello():
    print("Hello, world!  2  ")


if __name__=="__main__":
    print()
    from d import hello  # 导入 d 模块中的 hello 函数
    
    hello()  # 输出 Hello, world!
    # 修改 d.py 中的代码，将 world 改为 Python
    import importlib
    import d  # 导入 d 模块
    
    importlib.reload(d)  # 重新导入 d 模块
    hello()  # 仍然输出 Hello, world!
    from d import hello  # 重新导入 hello 函数
    
    hello()  # 输出 Hello, Python!