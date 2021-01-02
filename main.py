import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import subprocess
import os
import requests
from urllib.request import urlopen, Request
import time
from bs4 import BeautifulSoup
import cv2



print('Akıllı asistanınız Jarvis açılıyor')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices.id')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def Dile():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good morning sir")
    elif hour >= 12 and hour < 18:
        speak("Good evening sir")
    else:
        speak("good night sir")

def Dile2():
    hour2 = datetime.datetime.now().hour
    if hour2 >= 7 and hour2 < 17:
        speak("have a good day sir")
    else:
        speak("Good night sir")

saat = ["saat", "kaç", "saat kaç", "zaman", "saat kaç", "zamamnı söyle", "saati söyler misin","zamanı söyler misin"]
kapatma = ["görüşürüz", "baybay", "kapatabilirsin", "kapat", "kapalı mod"]
videoac = ["video açar mısın", "video aç", "YouTube'u aç", "Youtube aç", "Youtube"]
yayın = ["yayını", "yayın aç", "yayını aç", "Twitch'i", "Twitch", "yayın", "Twitch'i aç", "Twitch aç","yayını açar mısın", "yayın açar mısın", "Twitch'i açar mısın", "Twitch açar mısın"]
arama = ["Google'ı", "Google", "arama sayfası", "aramayı", "Google'ı aç", "Google aç", "aramayı aç", "arama aç","Google'ı açar mısın", "aramayı açar mısın", "arama açar mısın"]
çeviri = ["Translate'i", "Translate", "çeviriyi", "çeviri", "dil çevirisi", "Translate'i aç", "Translate aç","çeviriyi aç", "çeviri aç", "çeviriyi açar mısın", "çeviri açar mısın", "Translate'i açar mısın","Translate açar mısın"]
egzersiz = ["egzersizlerimi", "egzersizleri", "egzersizler", "spor", "sporumu", "egzersiz", "egzersizlerimi aç","egzersizleri aç", "egzersiz listemi aç", "spor listemi aç", "sporumu aç","spor listemi açar mısın", "egzersiz listemi açar mısın","egzersizlerim açar mısın","sindirimi açar mısın"]
havadurumu = ["hava durumu", "hava nasıl", "hava durumu nedir", "hava durumunu söyle", "hava durumunu aç","hava durumunu söyler misin"]
araştırma = ["Wikipedia'yı", "Wikipedia", "araştırma", "araştırmayı", "araştırmaya", "araştırma yap","Wikipedia'yı aç", "araştırma yapar mısın"]
senkimsin = ["sen kimsin", "kimsin", "nesin", "adın ne", "ismin ne", "amacın ne", "sen nesin"]
nasılsın = ["naber", "nasılsın", "ne yapıyorsun", "ne haber", "nasıl gidiyor"]
ara = ["internetten bak", "ara", "arama yapar mısın", "internetten bakar mısın"]
fotoğraflar = ["fotoğrafları aç", "fotoğraflarımı", "resimleri", "resimlerimi", "fotoğrafları açar mısın","resimlerimi açar mısın", "resimleri aç"]
canlıders = ["canlı dersimi", "canlı derslerimi", "derslerimi", "dersimi", "canlı derslerimi aç","canlı dersimi aç", "dersimi aç", "canlı dersini aç", "canlı ders mi aç","canlı derslerimi açar mısın", "canlı dersimi açar mısın", "canlı derslerim açar mısın","canlı ders açar mısın", "canlı ders mi açar mısın", "canlı Dersim açar mısın","canlı ders 20 açar mısın", "yanlı Dersim açar mısın", "canlı Dersim açar mısın", "yanı dersimi açar mısın","Yalı dersimi açar mısın"]
müzik = ["müziklerimi", "dinlediğim", "müzikleri", "müzikler", "müzik", "şarkı", "müzik aç", "müziklerimi aç","müzik listemi aç", "müzik listemi açar mısın", "müziklerimi açar mısın", "şarkılarımı açar mısın" "şarkı listemi açar mısın"]
sosyalmedya = ["Instagram", "Facebook", "Twitter", "sosyal medyayı", "sosyal medya", "medyadan", "sosyal medya aç", "sosyal medyamı aç"]
oyun = ["oyunumu", "oyunu", "oyun", "Call Of Duty", "oyunumu aç", "oyunumu açar mısın", "oyunu açar mısın"]
hesapmakinesi = ["hesap makinesi", "hesaplama", "hesaplayıcı", "çarpı", "bölü", "artı", "eksi","hesaplama yapar mısın"]
yazı = ["not", "çevir", "yaz", "yazı yaz", "yazıya çevir", "not al", "yazı yazar mısın","söylediklerimi yazıya çevirir misin", "not alır mısın"]
uygulamalar = ["uygulamalar", "ders uygulamalarını", "uygulama", "program", "Uygulamalar", "uygulamalarını","ders uygulamalarını aç", "ders uygulamamı aç", "ders uygulamalarını aç","ders uygulamalarımı açar mısın", "ders uygulamalarını açar mısın", ]
haber = ["haber", "haber sitesi", "haber aç", "haber sitesi aç", "haberleri aç", "haber sitelerini aç", "haber sitesini açar mısın", "haber sitelerini açar mısın"]
bedeneğitimi = ["beden eğitimi", "Beden eğitimi", "bedeneğitimi", "Bedeneğitimi"]
fizik = ["Fizik", "fizik"]
tarih = ["Tarih", "tarih"]
ingilizce = ["Ingilizce", "İngilizce", "ingilizce"]
matematik = ["Matematik", "matematik"]
kimya = ["Kimya", "kimya"]
coğrafya = ["Coğrafya", "coğrafya"]
biyoloji = ["Bİyoloji", "biyoloji"]
müzikdersi = ["Müzik dersi", "müzik dersi"]
bilgisayar = ["Bilgisayar", "bilgisayar"]
edebiyat = ["edebiyat", "Edebiyat"]
din = ["Din", "din"]
felsefe = ["Felsefe", "felsefe"]
almanca = ["Almanca", "almanca"]
borsa = ["Borsa", "borsayı söyler misin", "borsa", "döviz kuru", "döviz", "borsaya söyler misin","Bu sayı söyler misin", "Morse söyler misin"]
euro = ["Euro", "euro"]
dolar = ["Dolar", "dolar", "donar"]
birim = ["Birim çevirir misin", "Birimi çevir", "birim çevirir misin", "birimi çevir"]

def Komutal():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Dinliyorum")
        audio = r.listen(source)

        try:
            durum = r.recognize_google(audio, language='tr-tr')
            print(f"user said:{durum}\n")

        except Exception as e:
            speak("Rica etsem tekrar söyler misiniz?")
            return "None"
        return durum

print("Jarvis açılıyor")
speak("Jarvis is opening")
Dile()

if __name__ == '__main__':

    while True:
        speak("How can i help you sir")
        durum = Komutal().lower()
        if durum == 0:
            continue

        if durum in kapatma:
            speak('See you')
            print('güle güle efendim')
            Dile2()
            break

        elif durum in videoac:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("I'm opening Youtube sir")
            time.sleep(2)

        elif durum in yayın:
            webbrowser.open_new_tab("https://www.twitch.tv")
            speak("Have fun sir")
            time.sleep(2)

        elif durum in arama:
            webbrowser.open_new_tab("https://www.google.com")
            speak("I'm opening Google sir")
            time.sleep(5)

        elif durum in borsa:
            speak("Which one do you want to learn? Euro or Dolar")
            para = Komutal()
            if para in euro:
                pasteURL = "http://tr.investing.com/currencies/eur-try"
                data = urlopen(Request(pasteURL, headers={'User-Agent': 'Mozilla'})).read()
                parse = BeautifulSoup(data)
                for dolar in parse.find_all('span', id="last_last"):
                    liste = list(dolar)
                    print("Güncel Euro Kuru: " + str(liste))
                    speak("Euro is" + str(liste))
            elif para in dolar:
                pasteURL = "http://tr.investing.com/currencies/usd-try"
                data = urlopen(Request(pasteURL, headers={'User-Agent': 'Mozilla'})).read()
                parse = BeautifulSoup(data)
                for dolar in parse.find_all('span', id="last_last"):
                    liste = list(dolar)
                    print("Güncel Dolar Kuru: " + str(liste))
                    speak("Dolar is" + str(liste))

        elif durum in çeviri:
            webbrowser.open_new_tab("https://translate.google.com")
            speak("I'm opening the translate sir")
            time.sleep(5)

        elif durum in egzersiz:  #burada reklam yaptım :)
            speak("Which part do you want to do")
            bölge = Komutal()
            if "kol" in bölge:
                webbrowser.open_new_tab(
                    "https://www.youtube.com/watch?v=fsqhIBsao8k&list=PLiSWjRxvq9kpJi-h2m5isacOIbAj2i7No&index=2&t=181s")
                speak("don't make you tired")
            elif "arka kol" in bölge:
                webbrowser.open_new_tab(
                    "https://www.youtube.com/watch?v=rxdLG1X-2zU&list=PLiSWjRxvq9kpJi-h2m5isacOIbAj2i7No&index=3&t=717s")
                speak("don't make you tired")
            elif "göğüs" in bölge:
                webbrowser.open_new_tab("https://www.youtube.com/watch?v=2JzwpMbAEUo")
                speak("don't make you tired")
            elif "sırt" in bölge:
                webbrowser.open_new_tab(
                    "https://www.youtube.com/watch?v=NqPv3queECU&list=PLiSWjRxvq9kpJi-h2m5isacOIbAj2i7No&index=5")
                speak("don't make you tired")
            elif "karın" in bölge:
                webbrowser.open_new_tab(
                    "https://www.youtube.com/watch?v=73yDE7c-ca8&list=PLiSWjRxvq9kpJi-h2m5isacOIbAj2i7No&index=6")
                speak("don't make you tired")
            elif "bacak" in bölge:
                webbrowser.open_new_tab(
                    "https://www.youtube.com/watch?v=x3SlEFakS_Q&list=PLiSWjRxvq9kpJi-h2m5isacOIbAj2i7No&index=7")
                speak("don't make you tired")

        elif durum in havadurumu:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name = Komutal()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))
            else:
                speak("City not found")

        elif durum in haber:
            speak("I'm opening the news sir")
            webbrowser.open_new_tab("https://www.sozcu.com.tr")

        elif durum in araştırma:
            speak("What do you want to search")
            konu = Komutal()
            print(f"user said:{konu}\n")
            speak('Searching Wikipedia...')
            konu = konu.replace("wikipedia", "")
            results = wikipedia.summary(konu, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif durum in senkimsin:
            speak("Hello my name is Jarvis. I'm a voice assistant. I can help you every time. İlke sert made me in 4 week. I'M trtying to help him every time")

        elif durum in nasılsın:
            speak("I'm good sir what about you?")
            his = Komutal()
            if "iyiyim" in his:
                speak("Thats good to hear")
            else:
                "i hope you will be better"

        elif durum in ara:
            speak("what do you want to search")
            merak = Komutal()
            merak = merak.replace("search", "")
            webbrowser.open_new_tab(merak)
            time.sleep(5)

        elif durum in saat:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif "acil durum" in durum:
            speak("Which place do you need")
            yer=Komutal()
            if "eczane" or "Eczane" in yer:
                webbrowser.open_new_tab("https://www.google.com.tr/maps/search/eczane/@39.5629483,26.6957146,11z/data=!3m1!4b1?hl=tr")
                speak("Here is the nearest pharmacy")
            elif "Hastane" or "hastane" in durum:
                webbrowser.open_new_tab("https://www.google.com.tr/maps/search/hastane/@39.5627801,26.6950276,11z/data=!3m1!4b1?hl=tr")
                speak("Here is the nearest hospitals")
            elif "Benzinlik" or "benzinlik" in durum:
                webbrowser.open_new_tab("https://www.google.com.tr/maps/search/benzinlik/@39.5624438,26.6943401,11z/data=!3m1!4b1?hl=tr")
                speak("Here is the nearest gas stations")
            elif "Lokanta" or "lokanta" or "Restoran" or "restoran" or "restorant" or "Restorant" in durum:
                webbrowser.open_new_tab("https://www.google.com.tr/maps/search/restoran/@39.5621074,26.6929661,11z/data=!3m1!4b1?hl=tr")
                speak("here is the nearest restaurant")
            elif "Karakol" or "karakol" or "polis" or "Polis" in durum:
                webbrowser.open_new_tab("https://www.google.com.tr/maps/search/karakol/@39.5403364,26.8385617,12z/data=!3m1!4b1?hl=tr")

        elif "moralim bozuk" or "eğlendir beni" in durum:
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=Cqwic8ufpWk")
            resim = cv2.imread("download.jpg")
            print(type(resim))
            cv2.imshow("bir mahmuttuncer klasiği", resim)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif durum in müzik:
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=xAooPC2ZToo&list=RDxAooPC2ZToo&index=1")  #burada yazanlar kendi müzik listemin o yüzden değiştirebilirsiniz.
            speak("have fun sir")

        elif durum in sosyalmedya:
            speak("which one do you want to enter. First one is instagram second one is facebook third one is twitter")
            site = Komutal()
            if "birinci" in site:
                webbrowser.open_new_tab("https://www.instagram.com/?hl=tr")
                speak("Have fun sir")
            elif "ikinci" in site:
                speak("Have fun sir")
                webbrowser.open_new_tab(#bu işareti silip kendi facebook adresinizi yazın
                )
            elif "üçüncü" in site:
                webbrowser.open_new_tab("https://twitter.com/home")
                speak("Have fun sir")

        elif durum in hesapmakinesi:
            speak("what do you want to do")
            işlem = Komutal()
            if "toplama" in işlem:
                speak("what is first number")
                ilksayı = Komutal()
                speak("what is second number")
                ikincisayı = Komutal()
                t1 = ilksayı
                t2 = ikincisayı
                try:
                    t_1 = int(t1)
                    t_2 = int(t2)
                    print(t_1 + t_2)
                    results = (t_1 + t_2)
                    speak(results)
                except ValueError:
                    speak("please try again later")
            elif "çıkartma" in işlem:
                speak("what is first number")
                ilksayı = Komutal()
                speak("what is second number")
                ikincisayı = Komutal()
                c1 = ilksayı
                c2 = ikincisayı
                try:
                    c_1 = int(c1)
                    c_2 = int(c2)
                    print(c_1 - c_2)
                    results = (c_1 - c_2)
                    speak(results)
                except ValueError:
                    speak("please try again later")
            elif "çarpma" in işlem:
                speak("what is first number")
                ilksayı = Komutal()
                speak("what is second number")
                ikincisayı = Komutal()
                m1 = ilksayı
                m2 = ikincisayı
                try:
                    m_1 = int(m1)
                    m_2 = int(m2)
                    print(m_1 * m_2)
                    results = (m_1 * m_2)
                    speak(results)
                except ValueError:
                    speak("please try again later")
            elif "bölme" in işlem:
                speak("what is first number")
                ilksayı = Komutal()
                speak("what is second number")
                ikincisayı = Komutal()
                b1 = ilksayı
                b2 = ikincisayı
                try:
                    b_1 = int(b1)
                    b_2 = int(b2)
                    print(b_1 / b_2)
                    results = (b_1 / b_2)
                    speak(results)
                except ValueError:
                    speak("please try again later")
            elif "üslü" in işlem:
                speak("what is first number")
                ilksayı = Komutal()
                speak("what is second number")
                ikincisayı = Komutal()
                u1 = ilksayı
                u2 = ikincisayı
                try:
                    u_1 = int(u1)
                    u_2 = int(u2)
                    print(u_1 ** u_2)
                    results = (u_1 ** u_2)
                    speak(results)
                except ValueError:
                    speak("please try again later")
            elif "karekök" or "karakök" in işlem:
                speak("what is number")
                ilksayı = Komutal()
                s1 = ilksayı
                try:
                    s_1 = int(s1)
                    print(s_1 ** 0.5)
                    results = (s_1 ** 0.5)
                    speak(results)
                except ValueError:
                    speak("please try again later")

        elif durum in yazı:
            speak("What do you want to write")
            yazı1 = Komutal()
            dosya = open('metin_dosyası.txt', 'w')
            dosya.write(yazı1)
            dosya.close()

        elif durum in birim:
            speak("Which unit does your number belong to?")
            birim1 = Komutal()
            if "Litre" or "litre" in birim1:
                speak("which unit do you want to convert")
                birim2 = Komutal()
                if "mililitre" or "mili litre" or "Mili litre" in birim2:
                    speak("What is your number")
                    eldesayı = Komutal()
                    e1 = eldesayı
                    e2 = 1000
                    try:
                        e_1 = int(e1)
                        e_2 = int(e2)
                        print(e_1 * e_2)
                        results = (e_1 * e_2)
                        speak(results)
                    except ValueError:
                        speak("please try again later")
            elif "Miliitre" or "mililitre" in birim1:
                speak("which unit do you want to convert")
                birim3 = Komutal()
                if "Litre" or "litre" or "ligde" in birim3:
                    speak("What is your number")
                    eldesayı2 = Komutal()
                    z1 = eldesayı2
                    z2 = 1000
                    try:
                        z_1 = int(z1)
                        z_2 = int(z2)
                        print(z_1 / z_2)
                        results = (z_1 / z_2)
                        speak(results)
                    except ValueError:
                        speak("please try again later")