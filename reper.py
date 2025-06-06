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
parser.add_argument('-m', '--mode', help='Set reason of reports', choices=['spam', 'fake_account', 'violence', 'child_abuse', 'pornography', 'geoirrelevant'])
parser.add_argument('-re', '--reasons', help='Shows list of reasons', action='store_true')
parser.add_argument('-h', '--help', action='store_true')
args = parser.parse_args()

try:
    mkdir('sessions')
except:
    pass

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

elif args.add_number is not None:
    number = args.add_number
    if sesis:
        nums = [int(search(r'Ac(\d+)\.session', x).group(1)) for x in sesis]
        nums.sort()
        ses = TelegramClient(f'sessions/Ac{nums[-1]+1}', api_id, api_hash)
    else:
        ses = TelegramClient('sessions/Ac1', api_id, api_hash)
    try:
        ses.start(number)
        print(f' [{Fore.GREEN}✅{Fore.RESET}] Your account added successfully :D')
    except PhoneNumberInvalidError:
        print(f' [{Fore.RED}!{Fore.RESET}] The phone number was invalid!')
    exit(0)

elif args.run is not None and args.target and args.mode:
    if not sesis:
        print(f' [{Fore.RED}!{Fore.RESET}] Please {Fore.RED}add an account{Fore.RESET} to start reporting!')
        exit(0)

    count = args.run
    target = args.target

    async def report(client):
        async with client as cli:
            self_info = await cli.get_entity('self')
            self_name = self_info.first_name

            try:
                rep_msgs = await cli.get_messages(target, limit=3)
            except ValueError:
                print(f' [{Fore.RED}!{Fore.RESET}] The link of the channel is invalid!')
                return

            rep_ids = [m.id for m in rep_msgs]

            try:
                exists = any(
                    dialog.entity.username == target
                    async for dialog in cli.iter_dialogs()
                    if dialog.is_channel
                )
                if not exists:
                    await cli(JoinChannelRequest(target))
                    await asyncio.sleep(1)
            except:
                pass

            for r in range(count):
                try:
                    reason_map = {
                        'spam': types.InputReportReasonSpam(),
                        'fake_account': types.InputReportReasonFake(),
                        'violence': types.InputReportReasonViolence(),
                        'child_abuse': types.InputReportReasonChildAbuse(),
                        'pornography': types.InputReportReasonPornography(),
                        'geoirrelevant': types.InputReportReasonGeoIrrelevant()
                    }
                    result = await cli(functions.messages.ReportRequest(
                        peer=target,
                        id=rep_ids,
                        reason=reason_map[args.mode],
                        message="This channel sends offensive content"
                    ))

                    if result:
                        print(f" [{Fore.GREEN}✅{Fore.RESET}] Reported :) Ac:{Fore.YELLOW}{self_name}{Fore.RESET} count:{Fore.LIGHTBLUE_EX}{r}{Fore.RESET}")
                    else:
                        print(f" [{Fore.RED}!{Fore.RESET}] Failed :( Ac:{Fore.YELLOW}{self_name}{Fore.RESET}, count:{Fore.LIGHTBLUE_EX}{r}{Fore.RESET}")
                except Exception as e:
                    print(f" [{Fore.RED}!{Fore.RESET}] Error from {self_name}: {e}")

    async def main():
        tasks = []
        for num in range(1, len(sesis) + 1):
            client = TelegramClient(f'sessions/Ac{num}', api_id, api_hash)
            tasks.append(report(client))
        await asyncio.gather(*tasks)

    asyncio.run(main())

else:
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
