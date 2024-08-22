import pyrebase
import requests
import parser1
firebase_config = {
  'apiKey': "AIzaSyCKIdIOIAoxviSHq3aLA5BS4lKJDjJh2B0",
  'authDomain':  "citdb-8780e.firebaseapp.com",
  'databaseURL': "https://citdb-8780e-default-rtdb.firebaseio.com",
  'projectId': "citdb-8780e",
  'storageBucket': "citdb-8780e.appspot.com",
  'messagingSenderId': "240095447554",
  'appId': "1:240095447554:web:53aed078d4226d0a56f51b",
  'measurementId': "G-5XDM1422XD"

}
firebase = pyrebase.initialize_app(firebase_config)

auth = firebase.auth()
db = firebase.database()
# def sM(citName):
#     db.child(f'{citName}').get()


def pusher():

  url_grustniy = "https://finewords.ru/cit/grustnye"
  grustniy_page = requests.get(url_grustniy)

  url_zhiznennye = "https://finewords.ru/cit/zhiznennye"
  zhiznennye_page = requests.get(url_zhiznennye)

  url_smeshnye = "https://finewords.ru/cit/smeshnye"
  smeshnye_page = requests.get(url_smeshnye)

  url_umnye = "https://finewords.ru/cit/umnye"
  umnye_page = requests.get(url_umnye)

  url_mudrye_citaty = "https://finewords.ru/cit/mudrye-citaty"
  mudrye_citaty_page = requests.get(url_mudrye_citaty)

  url_mysli_o_zhizni = "https://finewords.ru/cit/mysli-o-zhizni"
  mysli_o_zhizni_page = requests.get(url_mysli_o_zhizni)

  url_motiviruyushhie = "https://finewords.ru/cit/motiviruyushhie"
  motiviruyushhie_page = requests.get(url_motiviruyushhie)

  url_love = "https://finewords.ru/cit/love"
  love_page = requests.get(url_love)

  for i in parser1.get_posts(grustniy_page):
      db.child('grustniy').push(i)

  for i in parser1.get_posts(zhiznennye_page):
      db.child('zhiznennye').push(i)

  for i in parser1.get_posts(umnye_page):
      db.child('umnye').push(i)

  for i in parser1.get_posts(mudrye_citaty_page):
      db.child('mudrye_citaty').push(i)

  for i in parser1.get_posts(mysli_o_zhizni_page):
      db.child('mysli_o_zhizni').push(i)

  for i in parser1.get_posts(motiviruyushhie_page):
      db.child('motiviruyushhie').push(i)

  for i in parser1.get_posts(smeshnye_page):
      db.child('smeshnye').push(i)

def sM(child):
  try:
    qu = ''
    d = db.child(child).get()
    for i,k in d.val().items():
        for v in k.values():
          if len(qu)==0:
            qu+=v
            db.child(child).child(f'{i}').remove()
            return str(qu)
          else:pass
  except:
    pusher()
    return "Упс, Что-то пошло не так попробуйте ещё раз"

