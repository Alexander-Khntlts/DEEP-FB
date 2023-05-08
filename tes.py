N,M,K,H,B,U,C,P = "\1b[00m","\1b[38;2;255;0;0m","\1b[38;2;208;255;0m","\1b[38;2;0;255;8m","\1b[38;2;38;0;255m","\1b[38;2;234;0;255m","\1b[38;2;0;221;255m","\1b[1;97m"
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






#coding by: utf-8












exp = []
Version = 'Beta'
Github = 'github.com/Xenz404'
Author = 'Xenz'
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
