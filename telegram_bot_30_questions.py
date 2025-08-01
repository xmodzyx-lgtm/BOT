
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

questions = [
    {
        "text": "1. Як ти зазвичай реагуєш у ситуації 1?",
        "options": [
            "🔵 Варіант A",
            "🟢 Варіант B"
        ]
    },
    {
        "text": "2. Як ти зазвичай реагуєш у ситуації 2?",
        "options": [
            "🔵 Варіант A",
            "🟢 Варіант B"
        ]
    },
    {
        "text": "3. Як ти зазвичай реагуєш у ситуації 3?",
        "options": [
            "🔵 Варіант A",
            "🟢 Варіант B"
        ]
    },
    {
        "text": "4. Як ти зазвичай реагуєш у ситуації 4?",
        "options": [
            "🔵 Варіант A",
            "🟢 Варіант B"
        ]
    },
    {
        "text": "5. Як ти зазвичай реагуєш у ситуації 5?",
        "options": [
            "🔵 Варіант A",
            "🟢 Варіант B"
        ]
    },
    {
        "text": "6. Як ти зазвичай реагуєш у ситуації 6?",
        "options": [
            "🔵 Варіант A",
            "🟢 Варіант B"
        ]
    },
    {
        "text": "7. Як ти зазвичай реагуєш у ситуації 7?",
        "options": [
            "🔵 Варіант A",
            "🟢 Варіант B"
        ]
    },
    {
        "text": "8. Як ти зазвичай реагуєш у ситуації 8?",
        "options": [
            "🔵 Варіант A",
            "🟢 Варіант B"
        ]
    },
    {
        "text": "9. Як ти зазвичай реагуєш у ситуації 9?",
        "options": [
            "🔵 Варіант A",
            "🟢 Варіант B"
        ]
    },
    {
        "text": "10. Як ти зазвичай реагуєш у ситуації 10?",
        "options": [
            "🔵 Варіант A",
            "🟢 Варіант B"
        ]
    },
    {
        "text": "11. Як ти зазвичай реагуєш у ситуації 11?",
        "options": [
            "🔵 Варіант A",
            "🟢 Варіант B"
        ]
    },
    {
        "text": "12. Як ти зазвичай реагуєш у ситуації 12?",
        "options": [
            "🔵 Варіант A",
            "🟢 Варіант B"
        ]
    },
    {
        "text": "13. Як ти зазвичай реагуєш у ситуації 13?",
        "options": [
            "🔵 Варіант A",
            "🟢 Варіант B"
        ]
    },
    {
        "text": "14. Як ти зазвичай реагуєш у ситуації 14?",
        "options": [
            "🔵 Варіант A",
            "🟢 Варіант B"
        ]
    },
    {
        "text": "15. Як ти зазвичай реагуєш у ситуації 15?",
        "options": [
            "🔵 Варіант A",
            "🟢 Варіант B"
        ]
    },
    {
        "text": "16. Як ти зазвичай реагуєш у ситуації 16?",
        "options": [
            "🔵 Варіант A",
            "🟢 Варіант B"
        ]
    },
    {
        "text": "17. Як ти зазвичай реагуєш у ситуації 17?",
        "options": [
            "🔵 Варіант A",
            "🟢 Варіант B"
        ]
    },
    {
        "text": "18. Як ти зазвичай реагуєш у ситуації 18?",
        "options": [
            "🔵 Варіант A",
            "🟢 Варіант B"
        ]
    },
    {
        "text": "19. Як ти зазвичай реагуєш у ситуації 19?",
        "options": [
            "🔵 Варіант A",
            "🟢 Варіант B"
        ]
    },
    {
        "text": "20. Як ти зазвичай реагуєш у ситуації 20?",
        "options": [
            "🔵 Варіант A",
            "🟢 Варіант B"
        ]
    },
    {
        "text": "21. Як ти зазвичай реагуєш у ситуації 21?",
        "options": [
            "🔵 Варіант A",
            "🟢 Варіант B"
        ]
    },
    {
        "text": "22. Як ти зазвичай реагуєш у ситуації 22?",
        "options": [
            "🔵 Варіант A",
            "🟢 Варіант B"
        ]
    },
    {
        "text": "23. Як ти зазвичай реагуєш у ситуації 23?",
        "options": [
            "🔵 Варіант A",
            "🟢 Варіант B"
        ]
    },
    {
        "text": "24. Як ти зазвичай реагуєш у ситуації 24?",
        "options": [
            "🔵 Варіант A",
            "🟢 Варіант B"
        ]
    },
    {
        "text": "25. Як ти зазвичай реагуєш у ситуації 25?",
        "options": [
            "🔵 Варіант A",
            "🟢 Варіант B"
        ]
    },
    {
        "text": "26. Як ти зазвичай реагуєш у ситуації 26?",
        "options": [
            "🔵 Варіант A",
            "🟢 Варіант B"
        ]
    },
    {
        "text": "27. Як ти зазвичай реагуєш у ситуації 27?",
        "options": [
            "🔵 Варіант A",
            "🟢 Варіант B"
        ]
    },
    {
        "text": "28. Як ти зазвичай реагуєш у ситуації 28?",
        "options": [
            "🔵 Варіант A",
            "🟢 Варіант B"
        ]
    },
    {
        "text": "29. Як ти зазвичай реагуєш у ситуації 29?",
        "options": [
            "🔵 Варіант A",
            "🟢 Варіант B"
        ]
    },
    {
        "text": "30. Як ти зазвичай реагуєш у ситуації 30?",
        "options": [
            "🔵 Варіант A",
            "🟢 Варіант B"
        ]
    }
]

answer_scores = {
    "🔵 Варіант A": [
        "Аналітик",
        "Творець"
    ],
    "🟢 Варіант B": [
        "Лідер",
        "Гармонізатор"
    ]
}

user_answers = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_answers[user_id] = {"current_q": 0, "scores": {"Аналітик": 0, "Творець": 0, "Лідер": 0, "Гармонізатор": 0}}
    await send_question(update, context)

async def send_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    q_index = user_answers[user_id]["current_q"]
    if q_index >= len(questions):
        await update.message.reply_text("Опитування завершено.")
        return
    question = questions[q_index]
    keyboard = ReplyKeyboardMarkup([[opt] for opt in question["options"]], one_time_keyboard=True, resize_keyboard=True)
    await update.message.reply_text(question["text"], reply_markup=keyboard)

async def handle_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    response = update.message.text
    user_state = user_answers.get(user_id)

    if not user_state:
        await update.message.reply_text("Напиши /start, щоб почати.")
        return

    types = answer_scores.get(response, [])
    for t in types:
        user_state["scores"][t] += 1

    user_state["current_q"] += 1
    if user_state["current_q"] < len(questions):
        await send_question(update, context)
    else:
        scores = user_state["scores"]
        top_type = max(scores, key=scores.get)
        summary = {
            "Аналітик": "🧠 Ти — Аналітик: логічний, зосереджений, раціональний.",
            "Творець": "🎨 Ти — Творець: креативний, інтуїтивний, гнучкий.",
            "Лідер": "🧭 Ти — Лідер: енергійний, впевнений, ініціативний.",
            "Гармонізатор": "🌱 Ти — Гармонізатор: врівноважений, дружній, стабільний."
        }
        await update.message.reply_text(f"✅ Готово!\n\n{summary[top_type]}")

if __name__ == '__main__':
    app = ApplicationBuilder().token("ВСТАВ_СЮДИ_СВІЙ_BOT_TOKEN").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_response))
    app.run_polling()
