import os
import turtle
import random
from PIL import Image

# Gerekli parametler // essentials parameters
nok = turtle.Turtle()
nok.speed(0)
nok.hideturtle()
pen = turtle.Screen()
entro = os.urandom(4)
turtle.colormode(255)
gen =pen.window_width()
uzu = pen.window_height()

rast_int1 = random.randint(-365, 365)
rast_int2 = random.randint(0, 365)
rast_int3 = random.randint(-365, 365)
rast_int4 = random.randint(0, 365)

renk_kaos1 = random.randint(0, 255)
renk_kaos2 = random.randint(0, 255)
renk_kaos3 = random.randint(0, 255)

kalem_kaos1 = random.randint(0, 25)

ent_gen = random.randint(0,gen * 2)
ent_uzu = random.randint(0,uzu * 2)
# Saf entropi ve okunur (ok_entro) entropi // Pure entropy and readable (ok_entro) entropy
print("Entropi eşittir :")
print(entro)

print("Okunur Entropi eşittir :")
ok_entro = entro.hex()
print(ok_entro)
# ok_entro_kaydet = ok_entro # ok_entro_kaydet hiçbir zaman kullanılmadı // ok_entro_kaydet was never used
print("rast int:")
print(rast_int1)
pen.title(ok_entro) # turtle başlığı / turtle title

# Çizim // Draw
boyut = rast_int2
def sanat(rast_int4):
    for _ in range(rast_int2):
        #pen.bgcolor(renk_kaos1,
        # renk_kaos3,
        # renk_kaos2)
# arka plan rengi PIL tarafından kaydedilmiyor / background color isn't saved by the PIL
        nok.color(renk_kaos1,
                  renk_kaos2,
                  renk_kaos3)

        nok.forward(rast_int3)
        nok.right(rast_int1)
sanat(boyut * kalem_kaos1)

# Mesaj // Message
nok.penup()
nok.goto(ent_gen /ent_uzu,
         ent_uzu /ent_gen)
nok.pendown()
nok.pencolor(renk_kaos3,
             renk_kaos1,
             renk_kaos2)
nok.write(ok_entro,
          align="center",
          font=("Arial",
                28,
                "bold")
          )

# .eps olarak kaydet // save as .eps
ham_foto = turtle.getcanvas()
ham_foto.postscript(file=ok_entro + ".eps")

# .eps > .jpg && rm .eps
foto = Image.open(ok_entro + ".eps")
foto.save(
          "[" +
          str(rast_int1) + " " +
          str(rast_int2) + " " +
          str(rast_int3) + " " +
          str(rast_int4) + "" +
          "] " +

          "[ " +
          str(renk_kaos1) + " " +
          str(renk_kaos2) + " " +
          str(renk_kaos3) + "" +
          "] " +

          "[" +
          str(ent_gen) + " " +
          str(ent_uzu) + "" +
          "] " +

          str(ok_entro)+ ".png"
          )

os.remove(ok_entro + ".eps") # Buna değerdi (:
