# -*- coding: utf-8 -*-
from app import App
import sys

def main():
    app = App()
    
    # 検索ウィンドウのサイズを変更不可にする
    app.root.resizable(height=False, width=False)
    
    app.root.mainloop()
    return 0

if __name__ == '__main__':
    sys.exit(main())