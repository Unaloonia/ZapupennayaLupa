import os

def func():
    zapupitlupu()

def zapupitlupu():
    try:
        os.rename("лупа","пупа")
        print ("лупа запупилась")
    except FileNotFoundError :
        print("А папка-то есть,еблан?")
    except WindowsError :
        print("долбоеб,эта папка уже есть")
    except Exception:
        print("я хз что за ошибка")

if __name__ == "__main__":
    #zapupitlupu()
    func()
