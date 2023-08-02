# reload.py
import importlib
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import a
from module_parse import parse_module_name


class ReloadHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.src_path.endswith(".py"):
            return
        module_name = parse_module_name(event.src_path)
        # 尝试导入该模块
        try:
            module = importlib.import_module(module_name)
            # 重新导入该模块
            importlib.reload(module)
            print(f"module {module_name} reloaded.")
        except ImportError:
            # 如果导入失败，忽略该文件
            pass


if __name__=="__main__":
    
    # 创建一个观察者对象
    observer = Observer()
    # 设置观察者对象监控当前目录下的所有 py 文件，添加处理器
    #observer.schedule(ReloadHandler(), path=".", recursive=False, patterns=["*.py"])
    observer.schedule(ReloadHandler(), path=".", recursive=True)
    # 启动观察者对象
    observer.start()
    a.A().start()
    observer.join()