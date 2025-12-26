#!/usr/bin/env python3
"""
ＰＹＴＨＯＮ 𝘼𝙐𝙏𝙊𝙈𝘼𝙏𝙄𝙊𝙉 𝘽𝙔 𝘿𝙀𝙑 ⚡⚡
Instagram DM Automation + Telegram Bot
Creator: @god_olds

This is the main entry point for VPS deployment.
It combines both the Instagram automation system and Telegram bot interface.
"""

import sys
import logging
import subprocess

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


def check_dependencies():
    """Verify all required dependencies are installed."""
    required_packages = {
        'playwright': 'playwright',
        'cfonts': 'python-cfonts',
        'telegram': 'python-telegram-bot',
        'asyncio': None,  # Built-in
        'os': None,  # Built-in
        'random': None,  # Built-in
        'logging': None,  # Built-in
    }
    
    logger.info("🔍 Checking dependencies...")
    
    missing_packages = []
    for module, pip_name in required_packages.items():
        try:
            __import__(module)
            logger.info(f"✅ {module} - OK")
        except ImportError:
            if pip_name:
                logger.error(f"❌ {module} - MISSING (pip: {pip_name})")
                missing_packages.append(pip_name)
            else:
                logger.error(f"❌ {module} - MISSING (built-in)")
    
    if missing_packages:
        logger.warning(f"\n⚠️  Installing missing packages: {', '.join(missing_packages)}")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install"] + missing_packages)
            logger.info("✅ Dependencies installed successfully!")
        except subprocess.CalledProcessError as e:
            logger.error(f"❌ Failed to install dependencies: {e}")
            return False
    
    logger.info("✅ All dependencies verified!\n")
    return True


def install_playwright_browsers():
    """Playwright browsers will be auto-installed on first use."""
    logger.info("📦 Playwright browsers will auto-install on first automation run\n")
    return True


def start_telegram_bot():
    """Start the Telegram bot with Instagram automation."""
    import os
    from telegram_bot import main as bot_main
    
    logger.info("=" * 50)
    logger.info("🚀 ＰＹＴＨＯＮ 𝘼𝙐𝙏𝙊𝙈𝘼𝙏𝙄𝙊𝙉 𝘽𝙔 𝘿𝙀𝙑 ⚡⚡")
    logger.info("=" * 50)
    logger.info("📱 Starting Telegram Bot...")
    logger.info("🤖 Instagram Automation System Ready")
    logger.info("=" * 50 + "\n")
    
    # Verify token exists
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    if not token:
        logger.error("❌ TELEGRAM_BOT_TOKEN environment variable not set!")
        logger.error("Please set your Telegram bot token before running.")
        return False
    
    try:
        bot_main()
    except KeyboardInterrupt:
        logger.info("\n🛑 Bot stopped by user")
        return True
    except Exception as e:
        logger.error(f"❌ Bot error: {e}")
        return False


def main():
    """Main entry point for VPS deployment."""
    logger.info("\n" + "=" * 50)
    logger.info("STARTUP CHECK")
    logger.info("=" * 50 + "\n")
    
    # Step 1: Check dependencies
    if not check_dependencies():
        logger.error("\n❌ Dependency check failed. Please install required packages.")
        sys.exit(1)
    
    # Step 2: Install Playwright browsers
    if not install_playwright_browsers():
        logger.error("\n❌ Playwright browser installation failed.")
        sys.exit(1)
    
    # Step 3: Start the bot
    if not start_telegram_bot():
        logger.error("\n❌ Bot startup failed.")
        sys.exit(1)


if __name__ == "__main__":
    main()
