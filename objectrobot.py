class robot:

    prototype_version = ("v2.01", "v2.12")

    def __init__(self,name,production_units):

        self.name= name
        self.production_units = production_units

See_Bot = robot("See-Bot", 500)
ak_bot = robot("AK-bot", 1500)

print("See-Bot is a {}".format(See_Bot.prototype_version[0]))
print("AK-bot is a {}".format(ak_bot.prototype_version[1]))

print("{} has this many production units:{}".format(See_Bot.name, See_Bot.production_units))
print("{} has this many production units:{}".format(ak_bot.name,ak_bot.production_units))