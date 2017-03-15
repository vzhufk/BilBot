# By Zhufyak V.V
# zhufyakvv@gmail.com
# github.com/zhufyakvv
# 15.03.2017

from chatterbot import ChatBot

best_logic = dict(import_path="chatterbot.logic.BestMatch",
                  statement_comparison_function="chatterbot.comparisons.levenshtein_distance")

bot = ChatBot("BilBot",
              logic_adapters=[
                  best_logic
              ],
              trainer='chatterbot.trainers.ListTrainer'
              )
bot.train([
    "Фразочки",
    "Твої",
    "Дебільні"
])

# Просто цикл.
while True:
    response = bot.get_response(input(">"))
    print(response)
