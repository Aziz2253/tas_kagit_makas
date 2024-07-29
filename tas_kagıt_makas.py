import random
oyuncuskor=0
pcskor=0
print("0)Taş   1)Kağıt  2)Makas")

while True :
      oyuncu_sayı=int(input("Bir sayı giriniz :"))
      pc_sayısı=random.randint(0,2)
      print(pc_sayısı)

      if oyuncu_sayı==0 and pc_sayısı==0 :
          print("Beraber")
          print("Bilgisayar :", pcskor, "  Oyuncu :", oyuncuskor)

      elif oyuncu_sayı==1 and pc_sayısı==0 :
          oyuncuskor+=1
          print("Bilgisayar :", pcskor, "  Oyuncu :", oyuncuskor)

      elif oyuncu_sayı==2 and pc_sayısı==0 :
          pcskor+=1
          print("Bilgisayar :", pcskor, "  Oyuncu :", oyuncuskor)

      elif oyuncu_sayı==0 and pc_sayısı==1 :
          pcskor+=1
          print("Bilgisayar :", pcskor, "  Oyuncu :", oyuncuskor)

      elif oyuncu_sayı==1 and pc_sayısı==1:
          print("Beraber")
          print("Bilgisayar :", pcskor, "  Oyuncu :", oyuncuskor)

      elif oyuncu_sayı==2 and pc_sayısı==1 :
          oyuncuskor+=1
          print("Bilgisayar :", pcskor, "  Oyuncu :", oyuncuskor)

      elif oyuncu_sayı==0 and pc_sayısı==2 :
          oyuncuskor+=1
          print("Bilgisayar :", pcskor, "  Oyuncu :", oyuncuskor)

      elif oyuncu_sayı==1 and pc_sayısı==2 :
           pcskor+=1
           print("Bilgisayar :", pcskor, "  Oyuncu :", oyuncuskor)

      elif oyuncu_sayı==2 and pc_sayısı==2 :
          print("Beraber")
          print("Bilgisayar :", pcskor, "  Oyuncu :", oyuncuskor)






      if oyuncuskor == 3 or pcskor== 3:
          if oyuncuskor==3 :
              print("Tebrikler Kazandınız !!!")
              break
          else :
              print("Bilgisayar kazandı")
              break

      else :

          pass