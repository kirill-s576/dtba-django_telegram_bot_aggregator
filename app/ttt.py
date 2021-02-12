


s = "test_bot.tg_bot.TestBot"

cl = s.split(".")[-1]
o = s.replace(f".{cl}", "")
print(o)