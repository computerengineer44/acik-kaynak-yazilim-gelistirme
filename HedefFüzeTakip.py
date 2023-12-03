import time
import random

class Hedef:
    def __init__(self):
        self.pozisyon = random.randint(1, 100)
        self.hareket_hizi = random.uniform(0.1, 2.0)  # Rastgele bir hareket hızı belirliyoruz

    def hareket_et(self):
        while True:
            self.pozisyon += self.hareket_hizi * random.choice([-1, 1])  # Rastgele hareket ettiriyoruz
            if self.pozisyon < 1:
                self.pozisyon = 1
            elif self.pozisyon > 100:
                self.pozisyon = 100

            print(f"Hedef pozisyonu: {self.pozisyon}")
            time.sleep(1)  # Yeni pozisyonu belirlemek için 1 saniye bekle

class Füze:
    def __init__(self):
        self.hedef = None

    def takip_et(self, hedef):
        self.hedef = hedef
        while True:
            if self.hedef is not None:
                print("Füze izliyor...")
                if self.hedef.pozisyon == 50:  # Füze hedefe vurmak için 50. pozisyonda olmalı
                    print("Hedefe vuruldu!")
                    break
                elif self.hedef.pozisyon > 50:
                    print("Hedefe doğru ilerleniyor...")
                else:
                    print("Hedefe doğru ilerleniyor...")
            else:
                print("Hedef belirlenmedi. Füze bekliyor...")
            time.sleep(1)  # Hedefi takip etmek için 1 saniye bekle

if __name__ == "__main__":
    hedef = Hedef()
    füze = Füze()

    # Hedefin hareketini başlat
    hedef_hareket_thread = threading.Thread(target=hedef.hareket_et)
    hedef_hareket_thread.start()

    # Füze, hedefi takip etmeye başlar
    füze_takip_thread = threading.Thread(target=füze.takip_et, args=(hedef,))
    füze_takip_thread.start()
