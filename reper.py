# t.me/Mr3rf1  <3
# Eski khasti beri manba bezan :|
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from telethon import functions, types
from os import listdir, mkdir
from sys import argv
from re import search
from colorama import Fore
import asyncio, argparse
parser = argparse.ArgumentParser(description='A tool for reporting telegram channels by t.me/mr3rf1', add_help=False)
parser.add_argument('-an', '--add-number', help='Add a new account')
parser.add_argument('-r', '--run', help='To get count and run', type=int)
parser.add_argument('-t', '--target', help='Enter target', type=str)
parser.add_argument('-m', '--mode', help='set reason of reports', choices=['spam', 'fake_account', 'violence', 'child_abuse', 'pornography', 'geoirrelevant'])
parser.add_argument('-re', '--reasons', help='shows list of reasons', action='store_true')
parser.add_argument('-h', '--help', action='store_true')
args = parser.parse_args()
try:
    mkdir('sessions')
except: pass
sesis = listdir('sessions')
sesis.sort()
api_id = 2839216
api_hash = '967fc90f9013e51dd7fe0713c35e28f8'
if args.help:
    print(f'''Help:
  -an {Fore.LIGHTBLUE_EX}NUMBER{Fore.RESET}, --add-number {Fore.LIGHTBLUE_EX}NUMBER{Fore.RESET} ~> {Fore.YELLOW}add account to script{Fore.RESET}
  example: python3 {argv[0]} -an {Fore.LIGHTBLUE_EX}+1512****{Fore.RESET}
  
  -r {Fore.LIGHTBLUE_EX}COUNT{Fore.RESET}, --run {Fore.LIGHTBLUE_EX}COUNT{Fore.RESET} ~> {Fore.YELLOW}set count of reports{Fore.RESET}
  -t {Fore.LIGHTBLUE_EX}TARGET{Fore.RESET}, --target {Fore.LIGHTBLUE_EX}TARGET{Fore.RESET} ~> {Fore.YELLOW}set target (without @){Fore.RESET}
  -m {Fore.LIGHTBLUE_EX}MODE{Fore.RESET}, --mode {Fore.LIGHTBLUE_EX}MODE{Fore.RESET} ~> {Fore.YELLOW}set type of reports (spam,...){Fore.RESET}
  example: python3 {argv[0]} -r {Fore.LIGHTBLUE_EX}1000{Fore.RESET} -t {Fore.LIGHTBLUE_EX}mmdChannel{Fore.RESET} -m {Fore.LIGHTBLUE_EX}spam{Fore.RESET}
  
  -re, --reasons ~> {Fore.YELLOW}show list of reasons for reporting{Fore.RESET}
  -h, --help ~> {Fore.YELLOW}show help{Fore.RESET}''')
elif args.reasons:
    print(f'''List of reasons:
    {Fore.YELLOW}*{Fore.RESET} spam
    {Fore.YELLOW}*{Fore.RESET} fake_account
    {Fore.YELLOW}*{Fore.RESET} violence
    {Fore.YELLOW}*{Fore.RESET} child_abuse
    {Fore.YELLOW}*{Fore.RESET} pornography
    {Fore.YELLOW}*{Fore.RESET} geoirrelevant''')
elif args.add_number != None:
    number = args.add_number
    if sesis != []:
        nums = [int(search('Ac(\d+)\.session', x).group(1)) for x in sesis]
        nums.sort()
        nOfLastAc = int(search('Ac(\d+)\.session', sesis[-1]).group(1))
        ses = TelegramClient(f'sessions/Ac{nums[-1]+1}', api_id, api_hash)
        try:
            ses.start(number)
            print(f' [{Fore.GREEN}✅{Fore.RESET}] Your account added succesfully :D')
            exit(0)
        except PhoneNumberInvalidError:
            print(f' [{Fore.RED}!{Fore.RESET}] The phoneNumber was invalid!{Fore.RESET}')
    else:
        ses = TelegramClient(f'sessions/Ac1', api_id, api_hash)
        try:
            ses.start(number)
            print(f' [{Fore.GREEN}✅{Fore.RESET}] Your account added succesfully :D')
            exit(0)
        except PhoneNumberInvalidError:
            print(f' [{Fore.RED}!{Fore.RESET}] The phoneNumber was invalid!{Fore.RESET}')
elif args.add_number == None and args.run != None and args.target != None and args.mode != None:
    if sesis == []:
        print(f' [{Fore.RED}!{Fore.RESET}] Please {Fore.RED}add a acount{Fore.RESET} to reporting!')
        exit(0)
    else:
        count = int(args.run)
        target = args.target
        async def report(client):
            async with client as cli:
                selfName = await cli.get_entity('self')
                selfName = selfName.first_name
                try: repMes = await cli.get_messages(target, limit=3)
                except ValueError: print(f' [{Fore.RED}!{Fore.RESET}] The link of channel was invalid!'); exit(0)
                repMess = []
                for m in repMes:
                    repMess.append(m.id)
                async for dialog in cli.iter_dialogs():
                    if dialog.is_channel:
                        if dialog.entity.username == target: exi = True; break
                    else:
                        exi = False
                if not exi:
                    await cli(JoinChannelRequest(target))
                    await asyncio.sleep(1)
                for r in range(count):
                    # result = await cli(functions.messages.ReportSpamRequest(peer=target))
                        # functions.account.ReportPeerRequest(peer=target, reason=types.InputReportReasonPornography(), message='This channel sends offensive content'))
                    if args.mode == 'spam':
                        result = await cli(functions.messages.ReportRequest(peer=target, id=repMess, reason=types.InputReportReasonSpam(), message="This channel sends offensive content"))                        # functions.account.ReportPeerRequest(peer=target, reason=types.InputReportReasonViolence()))
                    elif args.mode == 'fake_account':
                        result = await cli(functions.messages.ReportRequest(peer=target, id=repMess, reason=types.InputReportReasonFake(), message="This channel sends offensive content"))
                    elif args.mode == 'violence':
                        result = await cli(functions.messages.ReportRequest(peer=target, id=repMess, reason=types.InputReportReasonViolence(), message="This channel sends offensive content"))
                    elif args.mode == 'child_abuse':
                        result = await cli(functions.messages.ReportRequest(peer=target, id=repMess, reason=types.InputReportReasonChildAbuse(), message="This channel sends offensive content"))
                    elif args.mode == 'pornography':
                        result = await cli(functions.messages.ReportRequest(peer=target, id=repMess, reason=types.InputReportReasonPornography(), message="This channel sends offensive content"))
                  
                    elif args.mode == 'geoirrelevant':
                        result = await cli(functions.messages.ReportRequest(peer=target, id=repMess, reason=types.InputReportReasonGeoIrrelevant(), message="This channel sends offensive content"))                        # functions.account.ReportPeerRequest(peer=target, reason=types.InputReportReasonViolence()))
                    if result:
                        print(f" [{Fore.GREEN}✅{Fore.RESET}] Reported :) Ac:{Fore.YELLOW}{selfName}{Fore.RESET} count:{Fore.LIGHTBLUE_EX}{r}{Fore.RESET}")
                    else:
                        print(f" [{Fore.RED}!{Fore.RESET}] Error :( Ac:{Fore.YELLOW}{selfName}{Fore.RESET}, count:{Fore.LIGHTBLUE_EX}{r}{Fore.RESET}")
        async def main():
            runLis = []
            for num in range(1, len(sesis) + 1):
                exec(
                    f"runLis.append(report(TelegramClient(f'sessions/Ac{num}', api_id, api_hash)))")
            await asyncio.gather(*runLis)
        asyncio.run(main())
elif args.add_number == None and args.run != None and (args.target == None or args.mode == None):
    print(f" [{Fore.RED}!{Fore.RESET}] Please use this format{Fore.RED}~>{Fore.RESET} python3 {argv[0]} -r 10000 -t mmdChannel -m reportReseaon")
elif args.add_number == None and args.run == None and args.target == None and args.mode == None:
    print(f"""
    _____    _ __    t.me/{Fore.MAGENTA}Mr3rf1{Fore.RESET}    💀
   |_   _|__| |  _ \ ___ _ __   ___ _ __
     | |/ _ \ | |_) / _ \ '_ \ / _ \ '__|
     | |  __/ |  _ <  __/ |_) |  __/ |
     |_|\___|_|_| \_\___| .__/ \___|_|
                         |_|
     github.com/e811-py
{Fore.YELLOW}-----------------------------------------------{Fore.RESET}
 a tool for reporting telegram channels by @Mr3rf1
 use --help to see help: python3 {argv[0]} --help
    """)
