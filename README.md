# TelReper - Telegram Channel Reporter

A Python tool for reporting Telegram channels that violate Telegram's Terms of Service using multiple accounts simultaneously.

## ⚠️ Disclaimer

This tool is intended for legitimate reporting of channels that violate Telegram's Terms of Service. **Do not use this tool for harassment, spam, or malicious purposes.** The authors are not responsible for any misuse of this software. Use responsibly and in accordance with Telegram's Terms of Service.

## 🚀 Features

- **Multi-account support**: Add and manage multiple Telegram accounts
- **Batch reporting**: Report channels using all configured accounts simultaneously
- **Multiple report reasons**: Support for various violation types (spam, violence, etc.)
- **Session management**: Secure session storage for persistent logins
- **Colorized output**: Easy-to-read console output with color coding
- **Error handling**: Robust error handling for network issues and invalid inputs

## 📋 Requirements

- Python 3.7 or higher
- Telegram API credentials (api_id and api_hash)
- Valid Telegram account(s) with phone numbers

## 🛠️ Installation

### Termux (Android)
```bash
apt update && apt upgrade
pkg install python3 python3-pip git -y
git clone https://github.com/Mr3rf1/TelReper
cd TelReper
pip3 install telethon colorama
python3 reper.py
```

### Linux (Ubuntu/Debian)
```bash
sudo apt update && sudo apt upgrade
sudo apt install python3 python3-pip git -y
git clone https://github.com/Mr3rf1/TelReper
cd TelReper
pip3 install telethon colorama
python3 reper.py
```

### Windows
1. Install Python 3.7+ from [python.org](https://python.org)
2. Download or clone this repository
3. Open Command Prompt/PowerShell in the project directory
4. Run:
   ```cmd
   pip install telethon colorama
   python reper.py
   ```

## 🔧 Setup

1. **Get Telegram API credentials:**
   - Go to [my.telegram.org](https://my.telegram.org)
   - Log in with your phone number
   - Go to "API Development Tools"
   - Create a new application
   - Copy your `api_id` and `api_hash`

2. **Update API credentials:**
   - Open `reper.py`
   - Replace the `api_id` and `api_hash` values with your credentials:
   ```python
   api_id = YOUR_API_ID
   api_hash = 'YOUR_API_HASH'
   ```

## 📖 Usage

### Adding Accounts

Before reporting, you need to add at least one Telegram account:

```bash
python reper.py -an +1234567890
```

Replace `+1234567890` with your actual phone number (include country code).

### Reporting a Channel

```bash
python reper.py -r 100 -t channelname -m spam
```

**Parameters:**
- `-r, --run`: Number of reports to send
- `-t, --target`: Target channel username (without @)
- `-m, --mode`: Report reason (see available reasons below)

### Available Report Reasons

```bash
python reper.py -re
```

**Supported reasons:**
- `spam` - Spam content
- `fake_account` - Fake account/impersonation
- `violence` - Violent content
- `child_abuse` - Child abuse content
- `pornography` - Pornographic content
- `geoirrelevant` - Geographically irrelevant content

### Help

```bash
python reper.py -h
```

## 🔧 Command Line Options

| Option | Long Form | Description | Example |
|--------|-----------|-------------|---------|
| `-an` | `--add-number` | Add a new account | `-an +1234567890` |
| `-r` | `--run` | Number of reports to send | `-r 50` |
| `-t` | `--target` | Target channel (without @) | `-t spamchannel` |
| `-m` | `--mode` | Report reason | `-m spam` |
| `-re` | `--reasons` | Show available reasons | `-re` |
| `-h` | `--help` | Show help message | `-h` |

## 📁 Project Structure

```
TelReper/
├── reper.py          # Main application file
├── sessions/         # Directory for session files (auto-created)
│   ├── Ac1.session   # Session file for account 1
│   ├── Ac2.session   # Session file for account 2
│   └── ...
└── README.md         # This file
```

## 🔒 Security Notes

- Session files contain sensitive authentication data - keep them secure
- Never share your session files or API credentials
- The tool stores sessions locally in the `sessions/` directory
- Each account gets its own session file (Ac1.session, Ac2.session, etc.)

## 🐛 Troubleshooting

### Common Issues

**"The phoneNumber was invalid!"**
- Ensure you include the country code (e.g., +1 for US)
- Use the format: +[country_code][phone_number]

**"The link of channel was invalid!"**
- Make sure the channel username is correct
- Don't include the @ symbol
- Ensure the channel exists and is public

**Connection errors**
- Check your internet connection
- Telegram servers might be temporarily unavailable
- Try again after a few minutes

### Getting Help

If you encounter issues:
1. Check the error message carefully
2. Ensure all requirements are installed
3. Verify your API credentials are correct
4. Make sure you have at least one account added

## 🔄 Updates

This tool is compatible with **Telethon 1.40.0** and uses the latest Telegram API methods. The reporting system has been updated to work with Telegram's current API structure.

## 📜 License

This project is provided as-is for educational and legitimate reporting purposes only. Users are responsible for complying with all applicable laws and Telegram's Terms of Service.

## 🤝 Contributing

Contributions are welcome! Please ensure any contributions maintain the tool's legitimate purpose and include appropriate documentation.

## ⭐ Acknowledgments

- Built with [Telethon](https://github.com/LonamiWebs/Telethon) - Python Telegram client library
- Uses [Colorama](https://github.com/tartley/colorama) for colored terminal output
- Original concept by [@Mr3rf1](https://t.me/Mr3rf1)

---

**Remember: Use this tool responsibly and only for legitimate reporting of Terms of Service violations.**
