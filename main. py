from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 नमस्ते! Aviator Predictor Bot चालू है।\n/predict का उपयोग करें।")

async def predict(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 5:
        await update.message.reply_text("❌ कम से कम 5 multipliers भेजो!\nउदाहरण: /predict 1.2 2.4 1.1 5.0 2.1")
        return

    try:
        nums = [float(x) for x in context.args]
        avg = sum(nums) / len(nums)

        if avg < 2:
            msg = "⚠️ Pattern Weak लग रहा है\n⛔ Avoid Betting"
        elif avg < 3:
            msg = "🟡 Medium Pattern\n🔁 Wait or Low Bet"
        else:
            msg = "✅ Strong Pattern!\n🟢 Safe Bet कर सकते हो"

        await update.message.reply_text(msg)

    except:
        await update.message.reply_text("❌ Invalid input! सभी multipliers decimal में दो।")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("predict", predict))
app.run_polling()
