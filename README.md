# Apple Screenverter 📱➡️✨

*Because life's too short for App Store Connect rejections*

A dead-simple web tool that automatically resizes your screenshots to Apple's exact App Store Connect specifications. No more "invalid screenshot dimensions" emails. No more tears.

## The Problem

You've got beautiful screenshots. Apple wants them in *very specific* pixel dimensions. You resize them manually. Apple rejects them anyway. You question your life choices.

## The Solution

Upload screenshot → Get perfectly sized screenshot → Submit to App Store → Profit! 🎉

## Features

- **Drag & Drop Upload**
- **Smart Resizing** - Automatically finds the closest Apple specification
- **Center-Crop Magic** - Keeps the important stuff, crops the rest
- **Supports All Modern iPhones** - From iPhone XR to iPhone 16 Pro Max
- **Minimalist Design** - Clean, fast, no BS
- **Zero Configuration** - Just works™

## Quick Start

```bash
# Clone the repo
git clone https://github.com/Robooze/apple-screenverter.git
cd apple-screenverter

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Open `http://localhost:5001` and start converting!

## How It Works

1. **Upload** your screenshot (PNG, JPG, or JPEG)
2. **Magic happens** - Tool analyzes dimensions and picks the closest Apple spec
3. **Download** your perfectly sized screenshot
4. **Submit** to App Store Connect with confidence
5. **Celebrate** - No more dimension rejections!

## Supported Formats

- **Input**: PNG, JPG, JPEG (up to 16MB)
- **Output**: PNG (recommended for App Store)

## Supported Devices

All the iPhones that matter:
- iPhone 16 Pro Max
- iPhone 15 Pro Max  
- iPhone 14 Plus
- iPhone 13 Pro Max
- iPhone 12 Pro Max
- iPhone 11 Pro Max
- iPhone XS Max
- iPhone XR

## Why This Exists

After the 47th App Store rejection for "invalid screenshot dimensions," I built this tool with some bots in a fit of productive rage. Now you can benefit from my suffering.

## Tech Stack

- **Backend**: Flask (Python) - Simple and reliable
- **Frontend**: HTMX + Alpine.js + Tailwind closest
- **Image Processing**: Pillow - Because it just works
- **Deployment**: Ready for Railway, Render, or Vercel

## Contributing

Found a bug? Want a feature? Open an issue! PRs welcome.

## License

MIT - Do whatever you want with it, just don't blame me if it becomes sentient.

---

*Made with ☕ and mild frustration by [@Robooze](https://github.com/Robooze)*
