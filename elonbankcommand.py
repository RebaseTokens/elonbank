from telegram.ext.commandhandler import CommandHandler
from telegram.ext.updater import Updater
from telegram.ext.dispatcher import Dispatcher
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.bot import Bot
from telegram.parsemode import ParseMode
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import json

updater = Updater("5317695525:AAFMW8CLuyMz4NOWBRdHjfb5yTGTTYI4R8A", use_context=True)

dispatcher: Dispatcher = updater.dispatcher


def mcap(update: Update, context: CallbackContext):
    
    with open('/root/Desktop/elonbank.json', 'r') as myfile:
        data=myfile.read()

    obj = json.loads(data)
    marketcap = str(obj['mcap'])
    volume = str(obj['volume'])
    liq = str(obj['liquidity'])
    price = str(obj['price'])
    holders = str(obj['holders'])
    treasury = str(obj['treasury'])
    reserves = str(obj['reserves'])
    tokenburn = str(obj['tokenburn'])
    valueburn = str(obj['valueburn'])
    percentburn = str(obj['percentburn'])
    apy = str(obj['apy'])
    
    bot: Bot = context.bot
    
    
    keyboard = [
            [
                InlineKeyboardButton("Poocoin", url='https://poocoin.app/tokens/0xd5f363f83b36e10e8a823166b992c0bdc3dede2c'),
                InlineKeyboardButton("MC Track", url='https://alexarrig.godaddysites.com/elonbank')
            ]
        ]
             
    reply_markup = InlineKeyboardMarkup(keyboard)
    

    bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=open('/root/Desktop/elonbank/elonbank.png','rb'),
        caption= f"\U0001F48E <a href='https://t.me/elonbankbscglobal'>ElonBank</a> Official Group \U0001F48E\n<i>Auto-staking & Auto-compounder BSC Protocol: Earn {apy} APY</i>\n\n \U0001F4B5 <b>Market Cap:</b> {marketcap}\n \U0001F4B0	<b>Price:</b> {price}\n \U0001F5D3 <b>24h Volume:</b> {volume}\n \U0001F3E6 <b>Treasury:</b> {treasury}\n \U0001F45C <b>Reserves:</b> {reserves}\n \U0001F512 <b>Liquidity:</b> {liq}\n \U0001F4AC <b>Holders:</b> {holders}\n\n \U0001F525 <b>Burn Pit</b> \U0001F525\n <b>{tokenburn}</b> has been burned, valued <b>{valueburn}</b>, <b>{percentburn}</b> of the Supply! ( <a href='https://bscscan.com/token/0xd5f363f83b36e10e8a823166b992c0bdc3dede2c?a=0x3b7ff88c4898b479c92ef3325131cbca2d5e11ec'>BSCScan.com</a> )\n \n\n\U0001F4C8 <b>Charts:</b> <a href='https://www.dextools.io/app/bsc/pair-explorer/0xe153abd5b5debbfe17c0a50d50c3013ed7cf05fe'>DexTools</a> | <a href='https://charts.bogged.finance/?c=bsc&t=0xD5f363F83b36E10e8a823166b992c0bDc3deDE2C'>Bogged Finance</a>\n\U0001F30E <b>Website:</b> <a href='https://elonbank.io/'>elonbank.io</a>\n\U0001F99C <b>Twitter:</b> <a href='https://twitter.com/ElonBankBSC'>twitter.com/ElonBankBSC</a>\n \U0001F95E<b>Buy from:</b> <a href='https://flooz.trade/wallet/0xd5f363f83b36e10e8a823166b992c0bdc3dede2c?selectedTab=swap'>FloozTrade</a>",
        disable_notification=False,
        timeout = 20,
        reply_to_message_id=None,
        reply_markup=json.dumps(reply_markup.to_dict()),
        parse_mode=ParseMode.HTML
        )

    


dispatcher.add_handler(CommandHandler("mcap", mcap))

updater.start_polling()
