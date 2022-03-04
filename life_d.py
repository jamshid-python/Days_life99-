import datetime as dt

t_yil = int(input(">Tug'ilgan yilingizni yozing: "))
t_oy = int(input(">Tug'ulgan oyingiznini yozing(masalan avgust = 8, yanvar = 1): "))
t_kun = int(input(">Tug'ulgan kuningizni yozing: "))
print('     ')

a = dt.datetime.now()
sana1 = int(a.strftime("%Y"))
sana2 = int(a.strftime("%m"))
sana3 = int(a.strftime("%d"))

t = (t_yil*365) + (t_oy*30) + t_kun
t_hozir = (sana1*365) +(sana2*30) +sana3
year = sana1 - t_yil
month = sana2 - t_oy

jami_kun = int(t_hozir) - int(t)
print("Siz", jami_kun, "kun umr ko'rgansiz")
