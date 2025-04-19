# bot.py
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

TOKEN = "7776611328:AAHJ4JiPh3KKpvbvKq92kc3HxN4ANiPB4qA"

menu_buttons = [
    ("🖌 Logo dizayn", "logo"),
    ("📄 Post dizayn", "post"),
    ("🪪 Vizitka dizayn", "vizitka"),
    ("📢 Banner dizayn", "banner"),
    ("🤯 Foto mantaj", "yuz"),
    ("🖼 Portfolio", "portfolio"),
    ("💬 Bog‘lanish", "boglanish"),
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton(text, callback_data=data)] for text, data in menu_buttons]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("👋 Salom! Qaysi xizmatdan foydalanmoqchisiz?", reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    tanlov = {
        "logo": "🖌 Logo dizayn xizmatimiz haqida batafsil ma’lumot olish uchun biz bilan bog‘laning!",
        "post": "📄 Post dizayn — kontentga mos va jozibali postlar yaratamiz!",
        "stories": "📱 Stories dizayn — trendda bo‘lish uchun kerakli dizaynlar!",
        "vizitka": "🪪 Vizitka dizayn — sizning brendingizga mos kartochkalar!",
        "banner": "📢 Banner dizayn — reklamangizni ko‘zga ko‘rinadigan qilamiz!",
        "yuz": "🤯 Yuzni tiniqlashtirish — rasmingizni sifatli qilib beramiz!",
        "portfolio": "🖼 Portfolio — ishlarimiz bilan tanishing: @grafixportfolio",
        "boglanish": "💬 Bog‘lanish: @asomiddindonayev yoki instagram: instagram.com/asomiddinportfolio"
    }

    text = tanlov.get(query.data, "Noma’lum tanlov.")
    await query.edit_message_text(text)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()
