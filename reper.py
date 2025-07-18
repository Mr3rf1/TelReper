# t.me/Mr3rf1  <3
# Eski khasti beri manba bezan :|
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from telethon import functions
from os import listdir, mkdir
from sys import argv
from re import search
from colorama import Fore
import asyncio, argparse
argument_parser = argparse.ArgumentParser(description='A tool for reporting telegram channels by t.me/mr3rf1', add_help=False)
argument_parser.add_argument('-an', '--add-number', help='Add a new account')
argument_parser.add_argument('-r', '--run', help='To get count and run', type=int)
argument_parser.add_argument('-t', '--target', help='Enter target', type=str)
argument_parser.add_argument('-m', '--mode', help='set reason of reports', choices=['spam', 'fake_account', 'violence', 'child_abuse', 'pornography', 'geoirrelevant'])
argument_parser.add_argument('-re', '--reasons', help='shows list of reasons', action='store_true')
argument_parser.add_argument('-h', '--help', action='store_true')
command_line_args = argument_parser.parse_args()
try:
    mkdir('sessions')
except: pass
session_files = listdir('sessions')
session_files.sort()
api_id = 1234567
api_hash = '967fc90f90ajfu1dd7fe0724jm5e28f8'
if command_line_args.help:
    print(f'''Help:
  -an {Fore.LIGHTBLUE_EX}NUMBER{Fore.RESET}, --add-number {Fore.LIGHTBLUE_EX}NUMBER{Fore.RESET} ~> {Fore.YELLOW}add account to script{Fore.RESET}
  example: python3 {argv[0]} -an {Fore.LIGHTBLUE_EX}+1512****{Fore.RESET}

  -r {Fore.LIGHTBLUE_EX}COUNT{Fore.RESET}, --run {Fore.LIGHTBLUE_EX}COUNT{Fore.RESET} ~> {Fore.YELLOW}set count of reports{Fore.RESET}
  -t {Fore.LIGHTBLUE_EX}TARGET{Fore.RESET}, --target {Fore.LIGHTBLUE_EX}TARGET{Fore.RESET} ~> {Fore.YELLOW}set target (without @){Fore.RESET}
  -m {Fore.LIGHTBLUE_EX}MODE{Fore.RESET}, --mode {Fore.LIGHTBLUE_EX}MODE{Fore.RESET} ~> {Fore.YELLOW}set type of reports (spam,...){Fore.RESET}
  example: python3 {argv[0]} -r {Fore.LIGHTBLUE_EX}1000{Fore.RESET} -t {Fore.LIGHTBLUE_EX}mmdChannel{Fore.RESET} -m {Fore.LIGHTBLUE_EX}spam{Fore.RESET}

  -re, --reasons ~> {Fore.YELLOW}show list of reasons for reporting{Fore.RESET}
  -h, --help ~> {Fore.YELLOW}show help{Fore.RESET}''')
elif command_line_args.reasons:
    print(f'''List of reasons:
    {Fore.YELLOW}*{Fore.RESET} spam
    {Fore.YELLOW}*{Fore.RESET} fake_account
    {Fore.YELLOW}*{Fore.RESET} violence
    {Fore.YELLOW}*{Fore.RESET} child_abuse
    {Fore.YELLOW}*{Fore.RESET} pornography
    {Fore.YELLOW}*{Fore.RESET} geoirrelevant''')
elif command_line_args.add_number != None:
    phone_number = command_line_args.add_number
    if session_files != []:
        account_numbers = [int(search('Ac(\d+)\.session', session_file).group(1)) for session_file in session_files]
        account_numbers.sort()
        last_account_number = int(search('Ac(\d+)\.session', session_files[-1]).group(1))
        telegram_client = TelegramClient(f'sessions/Ac{account_numbers[-1]+1}', api_id, api_hash)
        try:
            telegram_client.start(phone_number)
            print(f' [{Fore.GREEN}✅{Fore.RESET}] Your account added succesfully :D')
            exit(0)
        except PhoneNumberInvalidError:
            print(f' [{Fore.RED}!{Fore.RESET}] The phoneNumber was invalid!{Fore.RESET}')
    else:
        telegram_client = TelegramClient(f'sessions/Ac1', api_id, api_hash)
        try:
            telegram_client.start(phone_number)
            print(f' [{Fore.GREEN}✅{Fore.RESET}] Your account added succesfully :D')
            exit(0)
        except PhoneNumberInvalidError:
            print(f' [{Fore.RED}!{Fore.RESET}] The phoneNumber was invalid!{Fore.RESET}')
elif command_line_args.add_number == None and command_line_args.run != None and command_line_args.target != None and command_line_args.mode != None:
    if session_files == []:
        print(f' [{Fore.RED}!{Fore.RESET}] Please {Fore.RED}add a acount{Fore.RESET} to reporting!')
        exit(0)
    else:
        report_count = int(command_line_args.run)
        target_channel = command_line_args.target
        async def report_channel(telegram_client):
            async with telegram_client as client:
                current_user = await client.get_entity('self')
                current_user_name = current_user.first_name
                try:
                    recent_messages = await client.get_messages(target_channel, limit=3)
                except ValueError:
                    print(f' [{Fore.RED}!{Fore.RESET}] The link of channel was invalid!'); exit(0)
                message_ids = []
                for message in recent_messages:
                    message_ids.append(message.id)
                channel_exists = False
                async for dialog in client.iter_dialogs():
                    if dialog.is_channel:
                        if dialog.entity.username == target_channel:
                            channel_exists = True
                            break
                if not channel_exists:
                    await client(JoinChannelRequest(target_channel))
                    await asyncio.sleep(1)
                for report_iteration in range(report_count):
                    # result = await client(functions.messages.ReportSpamRequest(peer=target_channel))
                        # functions.account.ReportPeerRequest(peer=target_channel, reason=types.InputReportReasonPornography(), message='This channel sends offensive content'))
                    # Updated for Telethon 1.40.0 - ReportRequest now uses 'option' parameter instead of 'reason'
                    # The option parameter should initially be empty bytes, and Telegram will return available options
                    report_message = f"This channel sends offensive content - {command_line_args.mode}"

                    # Start with empty option bytes - Telegram will return available report options
                    report_result = await client(functions.messages.ReportRequest(
                        peer=target_channel,
                        id=message_ids,
                        option=b'',  # Initially empty as per API documentation
                        message=report_message
                    ))
                    if report_result:
                        print(f" [{Fore.GREEN}✅{Fore.RESET}] Reported :) Ac:{Fore.YELLOW}{current_user_name}{Fore.RESET} count:{Fore.LIGHTBLUE_EX}{report_iteration}{Fore.RESET}")
                    else:
                        print(f" [{Fore.RED}!{Fore.RESET}] Error :( Ac:{Fore.YELLOW}{current_user_name}{Fore.RESET}, count:{Fore.LIGHTBLUE_EX}{report_iteration}{Fore.RESET}")
        async def run_all_accounts():
            reporting_tasks = []
            for account_number in range(1, len(session_files) + 1):
                exec(
                    f"reporting_tasks.append(report_channel(TelegramClient(f'sessions/Ac{account_number}', api_id, api_hash)))")
            await asyncio.gather(*reporting_tasks)
        asyncio.run(run_all_accounts())
elif command_line_args.add_number == None and command_line_args.run != None and (command_line_args.target == None or command_line_args.mode == None):
    print(f" [{Fore.RED}!{Fore.RESET}] Please use this format{Fore.RED}~>{Fore.RESET} python3 {argv[0]} -r 10000 -t mmdChannel -m reportReseaon")
elif command_line_args.add_number == None and command_line_args.run == None and command_line_args.target == None and command_line_args.mode == None:
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
