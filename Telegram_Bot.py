import telebot
import requests
from data import *
from io import BytesIO

bot = telebot.TeleBot(' ') # Вставить полученный токен

dic = Dic()
load = 0
list = []

@bot.message_handler(commands=['start'])
def list_lvl_1(message):
    a = telebot.types.InlineKeyboardMarkup(row_width=1)

    rifles_1 = telebot.types.InlineKeyboardButton("Винтовки", callback_data = "rifles")
    pistols_1 = telebot.types.InlineKeyboardButton("Пистолеты", callback_data = "pistols")
    pp_1 = telebot.types.InlineKeyboardButton("ПП", callback_data = "pp")
    shotguns_1 = telebot.types.InlineKeyboardButton("Дробовики", callback_data = "shotguns")
    machine_guns_1 = telebot.types.InlineKeyboardButton("Пулемёты", callback_data = "machine_guns")

    a.add(rifles_1, pistols_1, pp_1, shotguns_1, machine_guns_1)

    bot.send_message(message.chat.id, "Hello!", reply_markup = a)

@bot.callback_query_handler(func = lambda call: True)
def list_lvl_2(call):
    if call.message:
        if call.data == "start":
            a_0 = telebot.types.InlineKeyboardMarkup(row_width=1)

            rifles_1 = telebot.types.InlineKeyboardButton("Винтовки", callback_data = "rifles")
            pistols_1 = telebot.types.InlineKeyboardButton("Пистолеты", callback_data = "pistols")
            pp_1 = telebot.types.InlineKeyboardButton("ПП", callback_data = "pp")
            shotguns_1 = telebot.types.InlineKeyboardButton("Дробовики", callback_data = "shotguns")
            machine_guns_1 = telebot.types.InlineKeyboardButton("Пулемёты", callback_data = "machine_guns")

            a_0.add(rifles_1, pistols_1, pp_1, shotguns_1, machine_guns_1)
            bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = "ALL RIFLES!", reply_markup = a_0)

        if call.data == "rifles":
            b = telebot.types.InlineKeyboardMarkup(row_width=1)

            ak_47_1 = telebot.types.InlineKeyboardButton("AK-47", callback_data = "ak47")
            m4a4_1 = telebot.types.InlineKeyboardButton("M4A4", callback_data = "m4a4")
            m4a4_s_1 = telebot.types.InlineKeyboardButton("M4A1-S", callback_data = "m4a1_s")
            aug_1 = telebot.types.InlineKeyboardButton("AUG", callback_data = "aug")
            awp = telebot.types.InlineKeyboardButton("AWP", callback_data = "awp")
            sg_553_1 = telebot.types.InlineKeyboardButton("SG 553", callback_data = "sg553")
            galil_ar_1 = telebot.types.InlineKeyboardButton("Galil AR", callback_data = "galil_ar")
            famas_1 = telebot.types.InlineKeyboardButton("FAMAS", callback_data = "famas")
            ssg_08_1 = telebot.types.InlineKeyboardButton("SSG 08", callback_data = "ssg_08")
            scar_20_1 = telebot.types.InlineKeyboardButton("SCAR-20", callback_data = "scar_20")
            g3sg1_1 = telebot.types.InlineKeyboardButton("G3SG1", callback_data = "g3sg1")
            back_button_all_weapon = telebot.types.InlineKeyboardButton("BACK", callback_data = "start")

            b.add(ak_47_1, m4a4_1, m4a4_s_1, aug_1, awp, sg_553_1, galil_ar_1, famas_1, ssg_08_1, scar_20_1, g3sg1_1, back_button_all_weapon)
            bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = "ALL RIFLES!", reply_markup = b)

        elif call.data == "pistols":
            c = telebot.types.InlineKeyboardMarkup(row_width=4)

            usp_s_1 = telebot.types.InlineKeyboardButton("USP-S", callback_data = "usp")
            glock_18_1 = telebot.types.InlineKeyboardButton("Glock-18", callback_data = "glock")
            desert_eagle_1 = telebot.types.InlineKeyboardButton("Desert Eagle", callback_data = "desert")
            p_250_1 = telebot.types.InlineKeyboardButton("P250", callback_data = "p250")
            five_seven_1 = telebot.types.InlineKeyboardButton("Five-Seven", callback_data = "five-seven")
            cz75_auto_1 = telebot.types.InlineKeyboardButton("CZ75-Auto", callback_data = "cz75")
            p_2000_1 = telebot.types.InlineKeyboardButton("P2000", callback_data = "p200")
            tec_9_1 = telebot.types.InlineKeyboardButton("Tec-9", callback_data = "tec9")
            revolver_r8_1 = telebot.types.InlineKeyboardButton("Revolver R8", callback_data = "revolver")
            dual_berettas_1 = telebot.types.InlineKeyboardButton("Dual Berettas", callback_data = "berettas")
            back_button_all_weapon = telebot.types.InlineKeyboardButton("BACK", callback_data = "start")

            c.add(usp_s_1, glock_18_1, desert_eagle_1, p_250_1, five_seven_1, cz75_auto_1, p_2000_1, tec_9_1, revolver_r8_1, dual_berettas_1, back_button_all_weapon)
            bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = "ALL PISTOLS!", reply_markup = c)

        elif call.data == "pp":
            d = telebot.types.InlineKeyboardMarkup(row_width=4)

            p90_1 = telebot.types.InlineKeyboardButton("P90", callback_data = "p90")
            ump_45_1 = telebot.types.InlineKeyboardButton("UMP-45", callback_data = "ump-45")
            mac_10_1 = telebot.types.InlineKeyboardButton("MAC-10", callback_data = "mac-10")
            mp7_1 = telebot.types.InlineKeyboardButton("MP7", callback_data = "mp7")
            mp9_1 = telebot.types.InlineKeyboardButton("MP9", callback_data = "mp-9")
            mp5_sd_1 = telebot.types.InlineKeyboardButton("MP5-SD", callback_data = "mp5-sd")
            pp_bizon_1 = telebot.types.InlineKeyboardButton("PP-Bizon", callback_data = "pp_bizon")
            back_button_all_weapon = telebot.types.InlineKeyboardButton("BACK", callback_data = "start")

            d.add(p90_1, ump_45_1, mac_10_1, mp7_1, mp9_1, mp5_sd_1, pp_bizon_1, back_button_all_weapon)
            bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = "ALL PP!", reply_markup = d)

        elif call.data == "shotguns":
            e = telebot.types.InlineKeyboardMarkup(row_width=4)

            sawed_off_1 = telebot.types.InlineKeyboardButton("Sawed-Off", callback_data = "sawed-off")
            mag_7_1 = telebot.types.InlineKeyboardButton("MAG-7", callback_data = "mag-7")
            nova_1 = telebot.types.InlineKeyboardButton("Nova", callback_data = "nova")
            xm1014_1 = telebot.types.InlineKeyboardButton("XM1014", callback_data = "xm1014")
            back_button_all_weapon = telebot.types.InlineKeyboardButton("BACK", callback_data = "start")

            e.add(sawed_off_1, mag_7_1, nova_1, xm1014_1, back_button_all_weapon)
            bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = "ALL SHOTGUNS!", reply_markup = e)

        elif call.data == "machine_guns":
            f = telebot.types.InlineKeyboardMarkup(row_width=4)

            negev_1 = telebot.types.InlineKeyboardButton("Negev", callback_data = "negev")
            m249_1 = telebot.types.InlineKeyboardButton("M249", callback_data = "m249")
            back_button_all_weapon = telebot.types.InlineKeyboardButton("BACK", callback_data = "start")

            f.add(negev_1, m249_1, back_button_all_weapon)
            bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = "ALL MACHINE GUNS!", reply_markup = f)

        # ссылки на скины***********************************************************************************************
        # винтовки
        elif call.data == "ak47":
            a1 = telebot.types.InlineKeyboardMarkup(row_width=1)

            ak_47_2 = telebot.types.InlineKeyboardButton("AK-47 | Wild Lotus", callback_data = "AK-47 | Wild Lotus")
            ak_47_3 = telebot.types.InlineKeyboardButton("AK-47 | Gold Arabesque", callback_data = "AK-47 | Gold Arabesque")
            ak_47_4 = telebot.types.InlineKeyboardButton("AK-47 | Vulcan", callback_data = "AK-47 | Vulcan")
            ak_47_5 = telebot.types.InlineKeyboardButton("AK-47 | X-Ray", callback_data = "AK-47 | X-Ray")
            ak_47_6 = telebot.types.InlineKeyboardButton("AK-47 | Hydroponic", callback_data = "AK-47 | Hydroponic")
            back_button_rifles = telebot.types.InlineKeyboardButton("BACK", callback_data = "rifles")

            a1.add(ak_47_2, ak_47_3, ak_47_4, ak_47_5, ak_47_6, back_button_rifles)
            bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = "ALL AK's!", reply_markup = a1)
            print(call.data)

        elif call.data == "m4a4":
            b1 = telebot.types.InlineKeyboardMarkup(row_width=1)

            m4a4_2 = telebot.types.InlineKeyboardButton("M4A4 | Poseidon", callback_data = "M4A4 | Poseidon")
            m4a4_3 = telebot.types.InlineKeyboardButton("M4A4 | The Coalition", callback_data = "M4A4 | The Coalition")
            m4a4_4 = telebot.types.InlineKeyboardButton("M4A4 | Eye of Horus", callback_data = "M4A4 | Eye of Horus")
            m4a4_5 = telebot.types.InlineKeyboardButton("M4A4 | Radiation Hazard", callback_data = "M4A4 | Radiation Hazard")
            m4a4_6 = telebot.types.InlineKeyboardButton("M4A4 | Daybreak", callback_data = "M4A4 | Daybreak")
            back_button_rifles = telebot.types.InlineKeyboardButton("BACK", callback_data = "rifles")

            b1.add(m4a4_2, m4a4_3, m4a4_4, m4a4_5, m4a4_6, back_button_rifles)
            bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = "ALL M4A4's!", reply_markup = b1)
            print(call.data)

        elif call.data == "m4a1_s":
            c1 = telebot.types.InlineKeyboardMarkup(row_width=1)

            m4a1_S_2 = telebot.types.InlineKeyboardButton("M4A1-S | Knight", callback_data = "M4A1-S | Knight")
            m4a1_S_3 = telebot.types.InlineKeyboardButton("M4A1-S | Welcome to the Jungle", callback_data = "M4A1-S | Welcome to the Jungle")
            m4a1_S_4 = telebot.types.InlineKeyboardButton("M4A1-S | Imminent Danger", callback_data = "M4A1-S | Imminent Danger")
            m4a1_S_5 = telebot.types.InlineKeyboardButton("M4A1-S | Hot Rod", callback_data = "M4A1-S | Hot Rod")
            m4a1_S_6 = telebot.types.InlineKeyboardButton("M4A1-S | Blue Phosphor", callback_data = "M4A1-S | Blue Phosphor")
            back_button_rifles = telebot.types.InlineKeyboardButton("BACK", callback_data = "rifles")

            c1.add(m4a1_S_2, m4a1_S_3, m4a1_S_4, m4a1_S_5, m4a1_S_6, back_button_rifles)
            bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = "ALL M4A1-S's!", reply_markup = c1)
            print(call.data)

        elif call.data == "aug":
            d1 = telebot.types.InlineKeyboardMarkup(row_width=1)

            aug_2 = telebot.types.InlineKeyboardButton("AUG | Akihabara Accept", callback_data = "AUG | Akihabara Accept")
            aug_3 = telebot.types.InlineKeyboardButton("AUG | Midnight Lily", callback_data = "AUG | Midnight Lily")
            aug_4 = telebot.types.InlineKeyboardButton("AUG | Hot Rod", callback_data = "AUG | Hot Rod")
            aug_5 = telebot.types.InlineKeyboardButton("AUG | Flame Jörmungandr", callback_data = "AUG | Flame Jörmungandr")
            aug_6 = telebot.types.InlineKeyboardButton("AUG | Lil' Pig", callback_data = "AUG | Lil' Pig")
            back_button_rifles = telebot.types.InlineKeyboardButton("BACK", callback_data = "rifles")

            d1.add(aug_2, aug_3, aug_4, aug_5, aug_6, back_button_rifles)
            bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = "ALL AUG's!", reply_markup = d1)
            print(call.data)

        elif call.data == "awp":
            e1 = telebot.types.InlineKeyboardMarkup(row_width=1)

            awp_2 = telebot.types.InlineKeyboardButton("AWP | Gungnir", callback_data = "AWP | Gungnir")
            awp_3 = telebot.types.InlineKeyboardButton("AWP | Dragon Lore", callback_data = "AWP | Dragon Lore")
            awp_4 = telebot.types.InlineKeyboardButton("AWP | Medusa", callback_data = "AWP | Medusa")
            awp_5 = telebot.types.InlineKeyboardButton("AWP | The Prince", callback_data = "AWP | The Prince")
            awp_6 = telebot.types.InlineKeyboardButton("AWP | Desert Hydra", callback_data = "AWP | Desert Hydra")
            back_button_rifles = telebot.types.InlineKeyboardButton("BACK", callback_data = "rifles")

            e1.add(awp_2, awp_3, awp_4, awp_5, awp_6, back_button_rifles)
            bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = "ALL AWP's!", reply_markup = e1)
            print(call.data)

        elif call.data == "sg553":
            f1 = telebot.types.InlineKeyboardMarkup(row_width=1)

            sg553_2 = telebot.types.InlineKeyboardButton("SG 553 | Hazard Pay", callback_data = "SG 553 | Hazard Pay")
            sg553_3 = telebot.types.InlineKeyboardButton("SG 553 | Bulldozer", callback_data = "SG 553 | Bulldozer")
            sg553_4 = telebot.types.InlineKeyboardButton("SG 553 | Integrale", callback_data = "SG 553 | Integrale")
            sg553_5 = telebot.types.InlineKeyboardButton("SG 553 | Tornado", callback_data = "SG 553 | Tornado")
            sg553_6 = telebot.types.InlineKeyboardButton("SG 553 | Hypnotic", callback_data = "SG 553 | Hypnotic")
            back_button_rifles = telebot.types.InlineKeyboardButton("BACK", callback_data = "rifles")

            f1.add(sg553_2, sg553_3, sg553_4, sg553_5, sg553_6, back_button_rifles)
            bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = "ALL SG 553's!", reply_markup = f1)
            print(call.data)

        elif call.data == "galil_ar":
            g1 = telebot.types.InlineKeyboardMarkup(row_width=1)

            galil_ar_2 = telebot.types.InlineKeyboardButton("Galil AR | Aqua Terrace", callback_data = "Galil AR | Aqua Terrace")
            galil_ar_3 = telebot.types.InlineKeyboardButton("Galil AR | Rainbow Spoon", callback_data = "Galil AR | Rainbow Spoon")
            galil_ar_4 = telebot.types.InlineKeyboardButton("Galil AR | Phoenix Blacklight", callback_data = "Galil AR | Phoenix Blacklight")
            galil_ar_5 = telebot.types.InlineKeyboardButton("Galil AR | Chatterbox", callback_data = "Galil AR | Chatterbox")
            galil_ar_6 = telebot.types.InlineKeyboardButton("Galil AR | Sugar Rush", callback_data = "Galil AR | Sugar Rush")
            back_button_rifles = telebot.types.InlineKeyboardButton("BACK", callback_data = "rifles")

            g1.add(galil_ar_2, galil_ar_3, galil_ar_4, galil_ar_5, galil_ar_6, back_button_rifles)
            bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = "ALL GALIL-AR's!", reply_markup = g1)
            print(call.data)

        elif call.data == "famas":
            h1 = telebot.types.InlineKeyboardMarkup(row_width=1)

            famas_2 = telebot.types.InlineKeyboardButton("FAMAS | Spitfire", callback_data = "FAMAS | Spitfire")
            famas_3 = telebot.types.InlineKeyboardButton("FAMAS | Sundown", callback_data = "FAMAS | Sundown")
            famas_4 = telebot.types.InlineKeyboardButton("FAMAS | Prime Conspiracy", callback_data = "FAMAS | Prime Conspiracy")
            famas_5 = telebot.types.InlineKeyboardButton("FAMAS | Waters of Nephthys", callback_data = "FAMAS | Waters of Nephthys")
            famas_6 = telebot.types.InlineKeyboardButton("FAMAS | Meltdown", callback_data = "FAMAS | Meltdown")
            back_button_rifles = telebot.types.InlineKeyboardButton("BACK", callback_data = "rifles")

            h1.add(famas_2, famas_3, famas_4, famas_5, famas_6, back_button_rifles)
            bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = "ALL FAMAS's!", reply_markup = h1)
            print(call.data)

        elif call.data == "ssg_08":
            i1 = telebot.types.InlineKeyboardMarkup(row_width=1)

            ssg_08_2 = telebot.types.InlineKeyboardButton("SSG 08 | Sea Calico", callback_data = "SSG 08 | Sea Calico")
            ssg_08_3 = telebot.types.InlineKeyboardButton("SSG 08 | Death Strike", callback_data = "SSG 08 | Death Strike")
            ssg_08_4 = telebot.types.InlineKeyboardButton("SSG 08 | Blood in the Water", callback_data = "SSG 08 | Blood in the Water")
            ssg_08_5 = telebot.types.InlineKeyboardButton("SSG 08 | Bloodshot", callback_data = "SSG 08 | Bloodshot")
            ssg_08_6 = telebot.types.InlineKeyboardButton("SSG 08 | Sand Dune", callback_data = "SSG 08 | Sand Dune")
            back_button_rifles = telebot.types.InlineKeyboardButton("BACK", callback_data = "rifles")

            i1.add(ssg_08_2, ssg_08_3, ssg_08_4, ssg_08_5, ssg_08_6, back_button_rifles)
            bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = "ALL SSG 08's!", reply_markup = i1)
            print(call.data)

        elif call.data == "scar_20":
            j1 = telebot.types.InlineKeyboardMarkup(row_width=1)

            scar_20_2 = telebot.types.InlineKeyboardButton("SCAR-20 | Brass", callback_data = "SCAR-20 | Brass")
            scar_20_3 = telebot.types.InlineKeyboardButton("SCAR-20 | Cyrex", callback_data = "SCAR-20 | Cyrex")
            scar_20_4 = telebot.types.InlineKeyboardButton("SCAR-20 | Splash Jam", callback_data = "SCAR-20 | Splash Jam")
            scar_20_5 = telebot.types.InlineKeyboardButton("SCAR-20 | Magna Carta", callback_data = "SCAR-20 | Magna Carta")
            scar_20_6 = telebot.types.InlineKeyboardButton("SCAR-20 | Emerald", callback_data = "SCAR-20 | Emerald")
            back_button_rifles = telebot.types.InlineKeyboardButton("BACK", callback_data = "rifles")

            j1.add(scar_20_2, scar_20_3, scar_20_4, scar_20_5, scar_20_6, back_button_rifles)
            bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = "ALL SCAR-20's!", reply_markup = j1)
            print(call.data)

        elif call.data == "g3sg1":
            k1 = telebot.types.InlineKeyboardMarkup(row_width=1)

            g3sg1_2 = telebot.types.InlineKeyboardButton("G3SG1 | Chronos", callback_data = "G3SG1 | Chronos")
            g3sg1_3 = telebot.types.InlineKeyboardButton("G3SG1 | Violet Murano", callback_data = "G3SG1 | Violet Murano")
            g3sg1_4 = telebot.types.InlineKeyboardButton("G3SG1 | New Roots", callback_data = "G3SG1 | New Roots")
            g3sg1_5 = telebot.types.InlineKeyboardButton("G3SG1 | Flux", callback_data = "G3SG1 | Flux")
            g3sg1_6 = telebot.types.InlineKeyboardButton("G3SG1 | Arctic Camo", callback_data = "G3SG1 | Arctic Camo")
            back_button_rifles = telebot.types.InlineKeyboardButton("BACK", callback_data = "rifles")

            k1.add(g3sg1_2, g3sg1_3, g3sg1_4, g3sg1_5, g3sg1_6, back_button_rifles)
            bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = "ALL G3SG1's!", reply_markup = k1)
            print(call.data)

        # пистолеты
        elif call.data == "usp":
            a2 = telebot.types.InlineKeyboardMarkup(row_width=1)

            usp_2 = telebot.types.InlineKeyboardButton("USP-S | Whiteout", callback_data = "USP-S | Whiteout")
            usp_3 = telebot.types.InlineKeyboardButton("USP-S | Target Acquired", callback_data = "USP-S | Target Acquired")
            usp_4 = telebot.types.InlineKeyboardButton("USP-S | Kill Confirmed", callback_data = "USP-S | Kill Confirmed")
            usp_5 = telebot.types.InlineKeyboardButton("USP-S | Printstream", callback_data = "USP-S | Printstream")
            usp_6 = telebot.types.InlineKeyboardButton("USP-S | Dark Water", callback_data = "USP-S | Dark Water")
            back_button_pistols = telebot.types.InlineKeyboardButton("BACK", callback_data = "pistols")

            a2.add(usp_2, usp_3, usp_4, usp_5, usp_6, back_button_pistols)
            bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = "ALL USP-S's!", reply_markup = a2)
            print(call.data)

        elif call.data == "glock":
            b2 = telebot.types.InlineKeyboardMarkup(row_width=1)

            glock_2 = telebot.types.InlineKeyboardButton("Glock-18 | Fade", callback_data = "Glock-18 | Fade")
            glock_3 = telebot.types.InlineKeyboardButton("Glock-18 | Gamma Doppler Emerald", callback_data = "Glock-18 | Gamma Doppler Emerald")
            glock_4 = telebot.types.InlineKeyboardButton("Glock-18 | Synth Leaf", callback_data = "Glock-18 | Synth Leaf")
            glock_5 = telebot.types.InlineKeyboardButton("Glock-18 | Twilight Galaxy", callback_data = "Glock-18 | Twilight Galaxy")
            glock_6 = telebot.types.InlineKeyboardButton("Glock-18 | Dragon Tattoo", callback_data = "Glock-18 | Dragon Tattoo")
            back_button_pistols = telebot.types.InlineKeyboardButton("BACK", callback_data = "pistols")

            b2.add(glock_2, glock_3, glock_4, glock_5, glock_6, back_button_pistols)
            bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = "ALL GLOCK's!", reply_markup = b2)
            print(call.data)

        elif call.data == "desert":
            c2 = telebot.types.InlineKeyboardMarkup(row_width=1)

            desert_2 = telebot.types.InlineKeyboardButton("Desert Eagle | Blaze", callback_data = "Desert Eagle | Blaze")
            desert_3 = telebot.types.InlineKeyboardButton("Desert Eagle | Hand Cannon", callback_data = "Desert Eagle | Hand Cannon")
            desert_4 = telebot.types.InlineKeyboardButton("Desert Eagle | Fennec Fox", callback_data = "Desert Eagle | Fennec Fox")
            desert_5 = telebot.types.InlineKeyboardButton("Desert Eagle | Emerald Jörmungandr", callback_data = "Desert Eagle | Emerald Jörmungandr")
            desert_6 = telebot.types.InlineKeyboardButton("Desert Eagle | Sunset Storm 弐", callback_data = "Desert Eagle | Sunset Storm 弐")
            back_button_pistols = telebot.types.InlineKeyboardButton("BACK", callback_data = "pistols")

            c2.add(desert_2, desert_3, desert_4, desert_5, desert_6, back_button_pistols)
            bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = "ALL DESERT EAGLE's!", reply_markup = c2)
            print(call.data)

        elif call.data == "p250":
            d2 = telebot.types.InlineKeyboardMarkup(row_width=1)

            p250_2 = telebot.types.InlineKeyboardButton("P250 | Whiteout", callback_data = "P250 | Whiteout")
            p250_3 = telebot.types.InlineKeyboardButton("P250 | Nuclear Threat", callback_data = "P250 | Nuclear Threat")
            p250_4 = telebot.types.InlineKeyboardButton("P250 | Apep's Curse", callback_data = "P250 | Apep's Curse")
            p250_5 = telebot.types.InlineKeyboardButton("P250 | Digital Architect", callback_data = "P250 | Digital Architect")
            p250_6 = telebot.types.InlineKeyboardButton("P250 | Undertow", callback_data = "P250 | Undertow")
            back_button_pistols = telebot.types.InlineKeyboardButton("BACK", callback_data = "pistols")

            d2.add(p250_2, p250_3, p250_4, p250_5, p250_6, back_button_pistols)
            bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = "ALL P250's!", reply_markup = d2)
            print(call.data)

        elif call.data == "five-seven":
            e2 = telebot.types.InlineKeyboardMarkup(row_width=1)

            five_seven_2 = telebot.types.InlineKeyboardButton("Five-SeveN | Neon Kimono", callback_data = "Five-SeveN | Neon Kimono")
            five_seven_3 = telebot.types.InlineKeyboardButton("Five-SeveN | Fall Hazard", callback_data = "Five-SeveN | Fall Hazard")
            five_seven_4 = telebot.types.InlineKeyboardButton("Five-SeveN | Crimson Blossom", callback_data = "Five-SeveN | Crimson Blossom")
            five_seven_5 = telebot.types.InlineKeyboardButton("Five-SeveN | Berries And Cherries", callback_data = "Five-SeveN | Berries And Cherries")
            five_seven_6 = telebot.types.InlineKeyboardButton("Five-SeveN | Hyper Beast", callback_data = "Five-SeveN | Hyper Beast")
            back_button_pistols = telebot.types.InlineKeyboardButton("BACK", callback_data = "pistols")

            e2.add(five_seven_2, five_seven_3, five_seven_4, five_seven_5, five_seven_6, back_button_pistols)
            bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = "ALL FIVE-SEVEN's!", reply_markup = e2)
            print(call.data)

        elif call.data == "cz75":
            f2 = telebot.types.InlineKeyboardMarkup(row_width=1)

            cz75_2 = telebot.types.InlineKeyboardButton("CZ75-Auto | Chalice", callback_data = "CZ75-Auto | Chalice")
            cz75_3 = telebot.types.InlineKeyboardButton("CZ75-Auto | Emerald Quartz", callback_data = "CZ75-Auto | Emerald Quartz")
            cz75_4 = telebot.types.InlineKeyboardButton("CZ75-Auto | The Fuschia Is Now", callback_data = "CZ75-Auto | The Fuschia Is Now")
            cz75_5 = telebot.types.InlineKeyboardButton("CZ75-Auto | Emerald", callback_data = "CZ75-Auto | Emerald")
            cz75_6 = telebot.types.InlineKeyboardButton("CZ75-Auto | Slalom", callback_data = "CZ75-Auto | Slalom")
            back_button_pistols = telebot.types.InlineKeyboardButton("BACK", callback_data = "pistols")

            f2.add(cz75_2, cz75_3, cz75_4, cz75_5, cz75_6, back_button_pistols)
            bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = "ALL CZ75's!", reply_markup = f2)
            print(call.data)

        elif call.data == "p200":
            g2 = telebot.types.InlineKeyboardMarkup(row_width=1)

            p200_2 = telebot.types.InlineKeyboardButton("P2000 | Ocean Foam", callback_data = "P2000 | Ocean Foam")
            p200_3 = telebot.types.InlineKeyboardButton("P2000 | Chainmail", callback_data = "P2000 | Chainmail")
            p200_4 = telebot.types.InlineKeyboardButton("P2000 | Silver", callback_data = "P2000 | Silver")
            p200_5 = telebot.types.InlineKeyboardButton("P2000 | Dispatch", callback_data = "P2000 | Dispatch")
            p200_6 = telebot.types.InlineKeyboardButton("P2000 | Fire Elemental", callback_data = "P2000 | Fire Elemental")
            back_button_pistols = telebot.types.InlineKeyboardButton("BACK", callback_data = "pistols")

            g2.add(p200_2, p200_3, p200_4, p200_5, p200_6, back_button_pistols)
            bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = "ALL P2000's!", reply_markup = g2)
            print(call.data)

        elif call.data == "tec9":
            h2 = telebot.types.InlineKeyboardMarkup(row_width=1)

            tec9_2 = telebot.types.InlineKeyboardButton("Tec-9 | Terrace", callback_data = "Tec-9 | Terrace")
            tec9_3 = telebot.types.InlineKeyboardButton("Tec-9 | Nuclear Threat", callback_data = "Tec-9 | Nuclear Threat")
            tec9_4 = telebot.types.InlineKeyboardButton("Tec-9 | Decimator", callback_data = "Tec-9 | Decimator")
            tec9_5 = telebot.types.InlineKeyboardButton("Tec-9 | Brass", callback_data = "Tec-9 | Brass")
            tec9_6 = telebot.types.InlineKeyboardButton("Tec-9 | Rust Leaf", callback_data = "Tec-9 | Rust Leaf")
            back_button_pistols = telebot.types.InlineKeyboardButton("BACK", callback_data = "pistols")

            h2.add(tec9_2, tec9_3, tec9_4, tec9_5, tec9_6, back_button_pistols)
            bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = "ALL TEC9's!", reply_markup = h2)
            print(call.data)

        elif call.data == "revolver":
            i2 = telebot.types.InlineKeyboardMarkup(row_width=1)

            revolver_2 = telebot.types.InlineKeyboardButton("R8 Revolver | Fade", callback_data = "R8 Revolver | Fade")
            revolver_3 = telebot.types.InlineKeyboardButton("R8 Revolver | Llama Cannon", callback_data = "R8 Revolver | Llama Cannon")
            revolver_4 = telebot.types.InlineKeyboardButton("R8 Revolver | Canal Spray", callback_data = "R8 Revolver | Canal Spray")
            revolver_5 = telebot.types.InlineKeyboardButton("R8 Revolver | Phoenix Marker", callback_data = "R8 Revolver | Phoenix Marker")
            revolver_6 = telebot.types.InlineKeyboardButton("R8 Revolver | Crimson Web", callback_data = "R8 Revolver | Crimson Web")
            back_button_pistols = telebot.types.InlineKeyboardButton("BACK", callback_data = "pistols")

            i2.add(revolver_2, revolver_3, revolver_4, revolver_5, revolver_6, back_button_pistols)
            bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = "ALL REVOLVER's!", reply_markup = i2)
            print(call.data)

        elif call.data == "berettas":
            j2 = telebot.types.InlineKeyboardMarkup(row_width=1)

            berettas_2 = telebot.types.InlineKeyboardButton("Dual Berettas | Duelist", callback_data = "Dual Berettas | Duelist")
            berettas_3 = telebot.types.InlineKeyboardButton("Dual Berettas | Cobra Strike", callback_data = "Dual Berettas | Cobra Strike")
            berettas_4 = telebot.types.InlineKeyboardButton("Dual Berettas | Emerald", callback_data = "Dual Berettas | Emerald")
            berettas_5 = telebot.types.InlineKeyboardButton("Dual Berettas | Pyre", callback_data = "Dual Berettas | Pyre")
            berettas_6 = telebot.types.InlineKeyboardButton("Dual Berettas | Sweet Little Angels", callback_data = "Dual Berettas | Sweet Little Angels")
            back_button_pistols = telebot.types.InlineKeyboardButton("BACK", callback_data = "pistols")

            j2.add(berettas_2, berettas_3, berettas_4, berettas_5, berettas_6, back_button_pistols)
            bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = "ALL BERETTAS's!", reply_markup = j2)
            print(call.data)

        # ПП

        elif call.data == "p90":
            a3 = telebot.types.InlineKeyboardMarkup(row_width=1)

            p90_2 = telebot.types.InlineKeyboardButton("P90 | Astral Jörmungandr", callback_data = "P90 | Astral Jörmungandr")
            p90_3 = telebot.types.InlineKeyboardButton("P90 | Run and Hide", callback_data = "P90 | Run and Hide")
            p90_4 = telebot.types.InlineKeyboardButton("P90 | Emerald Dragon", callback_data = "P90 | Emerald Dragon")
            p90_5 = telebot.types.InlineKeyboardButton("P90 | Cold Blooded", callback_data = "P90 | Cold Blooded")
            p90_6 = telebot.types.InlineKeyboardButton("P90 | Death by Kitty", callback_data = "P90 | Death by Kitty")
            back_button_pp = telebot.types.InlineKeyboardButton("BACK", callback_data = "pp")

            a3.add(p90_2, p90_3, p90_4, p90_5, p90_6, back_button_pp)
            bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = "ALL P90's!", reply_markup = a3)
            print(call.data)

        elif call.data == "ump-45":
            b3 = telebot.types.InlineKeyboardMarkup(row_width=1)

            ump_45_2 = telebot.types.InlineKeyboardButton("UMP-45 | Fade", callback_data = "UMP-45 | Fade")
            ump_45_3 = telebot.types.InlineKeyboardButton("UMP-45 | Day Lily", callback_data = "UMP-45 | Day Lily")
            ump_45_4 = telebot.types.InlineKeyboardButton("UMP-45 | Minotaur's Labyrinth", callback_data = "UMP-45 | Minotaur's Labyrinth")
            ump_45_5 = telebot.types.InlineKeyboardButton("UMP-45 | Crime Scene", callback_data = "UMP-45 | Crime Scene")
            ump_45_6 = telebot.types.InlineKeyboardButton("UMP-45 | Caramel", callback_data = "UMP-45 | Caramel")
            back_button_pp = telebot.types.InlineKeyboardButton("BACK", callback_data = "pp")

            b3.add(ump_45_2, ump_45_3, ump_45_4, ump_45_5, ump_45_6, back_button_pp)
            bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = "ALL UMP-45's!", reply_markup = b3)
            print(call.data)

        elif call.data == "mac-10":
            c3 = telebot.types.InlineKeyboardMarkup(row_width=1)

            mac_10_2 = telebot.types.InlineKeyboardButton("MAC-10 | Hot Snakes", callback_data = "MAC-10 | Hot Snakes")
            mac_10_3 = telebot.types.InlineKeyboardButton("MAC-10 | Copper Borre", callback_data = "MAC-10 | Copper Borre")
            mac_10_4 = telebot.types.InlineKeyboardButton("MAC-10 | Red Filigree", callback_data = "MAC-10 | Red Filigree")
            mac_10_5 = telebot.types.InlineKeyboardButton("MAC-10 | Case Hardened", callback_data = "MAC-10 | Case Hardened")
            mac_10_6 = telebot.types.InlineKeyboardButton("MAC-10 | Stalker", callback_data = "MAC-10 | Stalker")
            back_button_pp = telebot.types.InlineKeyboardButton("BACK", callback_data = "pp")

            c3.add(mac_10_2, mac_10_3, mac_10_4, mac_10_5, mac_10_6, back_button_pp)
            bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = "ALL MAC-10's!", reply_markup = c3)
            print(call.data)

        elif call.data == "mp7":
            d3 = telebot.types.InlineKeyboardMarkup(row_width=1)

            mp7_2 = telebot.types.InlineKeyboardButton("MP7 | Teal Blossom", callback_data = "MP7 | Teal Blossom")
            mp7_3 = telebot.types.InlineKeyboardButton("MP7 | Whiteout", callback_data = "MP7 | Whiteout")
            mp7_4 = telebot.types.InlineKeyboardButton("MP7 | Full Stop", callback_data = "MP7 | Full Stop")
            mp7_5 = telebot.types.InlineKeyboardButton("MP7 | Skulls", callback_data = "MP7 | Skulls")
            mp7_6 = telebot.types.InlineKeyboardButton("MP7 | Orange Peel", callback_data = "MP7 | Orange Peel")
            back_button_pp = telebot.types.InlineKeyboardButton("BACK", callback_data = "pp")

            d3.add(mp7_2, mp7_3, mp7_4, mp7_5, mp7_6, back_button_pp)
            bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = "ALL MP7's!", reply_markup = d3)
            print(call.data)

        elif call.data == "mp-9":
            e3 = telebot.types.InlineKeyboardMarkup(row_width=1)

            mp_9_2 = telebot.types.InlineKeyboardButton("MP9 | Wild Lily", callback_data = "MP9 | Wild Lily")
            mp_9_3 = telebot.types.InlineKeyboardButton("MP9 | Bulldozer", callback_data = "MP9 | Bulldozer")
            mp_9_4 = telebot.types.InlineKeyboardButton("MP9 | Pandora's Box", callback_data = "MP9 | Pandora's Box")
            mp_9_5 = telebot.types.InlineKeyboardButton("MP9 | Hot Rod", callback_data = "MP9 | Hot Rod")
            mp_9_6 = telebot.types.InlineKeyboardButton("MP9 | Dark Age", callback_data = "MP9 | Dark Age")
            back_button_pp = telebot.types.InlineKeyboardButton("BACK", callback_data = "pp")

            e3.add(mp_9_2, mp_9_3, mp_9_4, mp_9_5, mp_9_6, back_button_pp)
            bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = "ALL MP-9's!", reply_markup = e3)
            print(call.data)

        elif call.data == "mp5-sd":
            f3 = telebot.types.InlineKeyboardMarkup(row_width=1)

            mp5_sd_2 = telebot.types.InlineKeyboardButton("MP5-SD | Oxide Oasis", callback_data = "MP5-SD | Oxide Oasis")
            mp5_sd_3 = telebot.types.InlineKeyboardButton("MP5-SD | Phosphor", callback_data = "MP5-SD | Phosphor")
            mp5_sd_4 = telebot.types.InlineKeyboardButton("MP5-SD | Autumn Twilly", callback_data = "MP5-SD | Autumn Twilly")
            mp5_sd_5 = telebot.types.InlineKeyboardButton("MP5-SD | Nitro", callback_data = "MP5-SD | Nitro")
            mp5_sd_6 = telebot.types.InlineKeyboardButton("MP5-SD | Bamboo Garden", callback_data = "MP5-SD | Bamboo Garden")
            back_button_pp = telebot.types.InlineKeyboardButton("BACK", callback_data = "pp")

            f3.add(mp5_sd_2, mp5_sd_3, mp5_sd_4, mp5_sd_5, mp5_sd_6, back_button_pp)
            bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = "ALL MP5-SD's!", reply_markup = f3)
            print(call.data)

        elif call.data == "pp_bizon":
            g3 = telebot.types.InlineKeyboardMarkup(row_width=1)

            pp_bizon_2 = telebot.types.InlineKeyboardButton("PP-Bizon | Rust Coat", callback_data = "PP-Bizon | Rust Coat")
            pp_bizon_3 = telebot.types.InlineKeyboardButton("PP-Bizon | Carbon Fiber", callback_data = "PP-Bizon | Carbon Fiber")
            pp_bizon_4 = telebot.types.InlineKeyboardButton("PP-Bizon | Antique", callback_data = "PP-Bizon | Antique")
            pp_bizon_5 = telebot.types.InlineKeyboardButton("PP-Bizon | High Roller", callback_data = "PP-Bizon | High Roller")
            pp_bizon_6 = telebot.types.InlineKeyboardButton("PP-Bizon | Modern Hunter", callback_data = "PP-Bizon | Modern Hunter")
            back_button_pp = telebot.types.InlineKeyboardButton("BACK", callback_data = "pp")

            g3.add(pp_bizon_2, pp_bizon_3, pp_bizon_4, pp_bizon_5, pp_bizon_6, back_button_pp)
            bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = "ALL PP-BIZON's!", reply_markup = g3)
            print(call.data)

        # Дробовики

        elif call.data == "sawed-off":
            a4 = telebot.types.InlineKeyboardMarkup(row_width=1)

            sawed_off_2 = telebot.types.InlineKeyboardButton("Sawed-Off | Copper", callback_data = "Sawed-Off | Copper")
            sawed_off_3 = telebot.types.InlineKeyboardButton("Sawed-Off | First Class", callback_data = "Sawed-Off | First Class")
            sawed_off_4 = telebot.types.InlineKeyboardButton("Sawed-Off | Rust Coat", callback_data = "Sawed-Off | Rust Coat")
            sawed_off_5 = telebot.types.InlineKeyboardButton("Sawed-Off | Orange DDPAT", callback_data = "Sawed-Off | Orange DDPAT")
            sawed_off_6 = telebot.types.InlineKeyboardButton("Sawed-Off | Devourer", callback_data = "Sawed-Off | Devourer")
            back_button_shotguns = telebot.types.InlineKeyboardButton("BACK", callback_data = "shotguns")

            a4.add(sawed_off_2, sawed_off_3, sawed_off_4, sawed_off_5, sawed_off_6, back_button_shotguns)
            bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = "ALL SAWED-OFF's!", reply_markup = a4)
            print(call.data)

        elif call.data == "mag-7":
            b4 = telebot.types.InlineKeyboardMarkup(row_width=1)

            mag_7_2 = telebot.types.InlineKeyboardButton("MAG-7 | Cinquedea", callback_data = "MAG-7 | Cinquedea")
            mag_7_3 = telebot.types.InlineKeyboardButton("MAG-7 | Counter Terrace", callback_data = "MAG-7 | Counter Terrace")
            mag_7_4 = telebot.types.InlineKeyboardButton("MAG-7 | Bulldozer", callback_data = "MAG-7 | Bulldozer")
            mag_7_5 = telebot.types.InlineKeyboardButton("MAG-7 | Prism Terrace", callback_data = "MAG-7 | Prism Terrace")
            mag_7_6 = telebot.types.InlineKeyboardButton("MAG-7 | Chainmail", callback_data = "MAG-7 | Chainmail")
            back_button_shotguns = telebot.types.InlineKeyboardButton("BACK", callback_data = "shotguns")

            b4.add(mag_7_2, mag_7_3, mag_7_4, mag_7_5, mag_7_6, back_button_shotguns)
            bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = "ALL MAG-7's!", reply_markup = b4)
            print(call.data)

        elif call.data == "nova":
            c4 = telebot.types.InlineKeyboardMarkup(row_width=1)

            nova_2 = telebot.types.InlineKeyboardButton("Nova | Baroque Orange", callback_data = "Nova | Baroque Orange")
            nova_3 = telebot.types.InlineKeyboardButton("Nova | Bloomstick", callback_data = "Nova | Bloomstick")
            nova_4 = telebot.types.InlineKeyboardButton("Nova | Blaze Orange", callback_data = "Nova | Blaze Orange")
            nova_5 = telebot.types.InlineKeyboardButton("Nova | Hyper Beast", callback_data = "Nova | Hyper Beast")
            nova_6 = telebot.types.InlineKeyboardButton("Nova | Quick Sand", callback_data = "Nova | Quick Sand")
            back_button_shotguns = telebot.types.InlineKeyboardButton("BACK", callback_data = "shotguns")

            c4.add(nova_2, nova_3, nova_4, nova_5, nova_6, back_button_shotguns)
            bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = "ALL NOVA's!", reply_markup = c4)
            print(call.data)

        elif call.data == "xm1014":
            d4 = telebot.types.InlineKeyboardMarkup(row_width=1)

            xm1014_2 = telebot.types.InlineKeyboardButton("XM1014 | Frost Borre", callback_data = "XM1014 | Frost Borre")
            xm1014_3 = telebot.types.InlineKeyboardButton("XM1014 | Elegant Vines", callback_data = "XM1014 | Elegant Vines")
            xm1014_4 = telebot.types.InlineKeyboardButton("XM1014 | Ancient Lore", callback_data = "XM1014 | Ancient Lore")
            xm1014_5 = telebot.types.InlineKeyboardButton("XM1014 | Red Leather", callback_data = "XM1014 | Red Leather")
            xm1014_6 = telebot.types.InlineKeyboardButton("XM1014 | Banana Leaf", callback_data = "XM1014 | Banana Leaf")
            back_button_shotguns = telebot.types.InlineKeyboardButton("BACK", callback_data = "shotguns")

            d4.add(xm1014_2, xm1014_3, xm1014_4, xm1014_5, xm1014_6, back_button_shotguns)
            bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = "ALL XM1014's!", reply_markup = d4)
            print(call.data)

        # пулемёты

        elif call.data == "negev":
            a5 = telebot.types.InlineKeyboardMarkup(row_width=1)

            negev_2 = telebot.types.InlineKeyboardButton("Negev | Mjölnir", callback_data = "Negev | Mjölnir")
            negev_3 = telebot.types.InlineKeyboardButton("Negev | Anodized Navy", callback_data = "Negev | Anodized Navy")
            negev_4 = telebot.types.InlineKeyboardButton("Negev | CaliCamo", callback_data = "Negev | CaliCamo")
            negev_5 = telebot.types.InlineKeyboardButton("Negev | Phoenix Stencil", callback_data = "Negev | Phoenix Stencil")
            negev_6 = telebot.types.InlineKeyboardButton("Negev | Infrastructure", callback_data = "Negev | Infrastructure")
            back_button_machine_guns = telebot.types.InlineKeyboardButton("BACK", callback_data = "machine_guns")

            a5.add(negev_2, negev_3, negev_4, negev_5, negev_6, back_button_machine_guns)
            bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = "ALL NEGEV's!", reply_markup = a5)
            print(call.data)

        elif call.data == "m249":
            b5 = telebot.types.InlineKeyboardMarkup(row_width=1)

            m249_2 = telebot.types.InlineKeyboardButton("M249 | Shipping Forecast", callback_data = "M249 | Shipping Forecast")
            m249_3 = telebot.types.InlineKeyboardButton("M249 | Humidor", callback_data = "M249 | Humidor")
            m249_4 = telebot.types.InlineKeyboardButton("M249 | Blizzard Marbleized", callback_data = "M249 | Blizzard Marbleized")
            m249_5 = telebot.types.InlineKeyboardButton("M249 | Jungle", callback_data = "M249 | Jungle")
            m249_6 = telebot.types.InlineKeyboardButton("M249 | Contrast Spray", callback_data = "M249 | Contrast Spray")
            back_button_machine_guns = telebot.types.InlineKeyboardButton("BACK", callback_data = "machine_guns")

            b5.add(m249_2, m249_3, m249_4, m249_5, m249_6, back_button_machine_guns)
            bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = "ALL M249's!", reply_markup = b5)
            print(call.data)

        #ссылки на оружие******************************************************************************************************************
        #ссылки на оружие******************************************************************************************************************
        #ссылки на оружие******************************************************************************************************************

        ppp1 = []
        bbb1 = []
        quality_list = []

        if call.data in dic.dictionary:
            name = call.data  # call.data - название пушки
            global load
            if load == 0:
                load = 1
                dic_in_bot = dic.dictionary[call.data]
                index = 0
                for sds in dic_in_bot: #поиск в словаре значения по ключу пушки
                    index =+ 1
                    if index == 4:
                        break
                    if sds == "-":
                        quality_list.append(sds)
                    else:
                        bbb1 = (requests.get(sds).text).replace(".", " ").replace(">", " ").split()
                        if '{"success":1,"sell_order_table":"<table' in bbb1:
                            for i in bbb1:
                                if i != "<\\/td":
                                   ppp1.append(i)
                                else:
                                    break
                        else:
                            for i in bbb1:
                                if i != '<\/td':
                                   ppp1.append(i)
                                else:
                                    break
                        quality_list.append(" ".join(ppp1[-2::]))
                print(quality_list)

                print(f"FN {quality_list[0]} \nMW {quality_list[1]} \nFT {quality_list[2]}")
                print(f"WW {quality_list[3]} \nBS {quality_list[4]}")


                if len(dic_in_bot) == 6:
                    last_req = requests.get(dic_in_bot[-1])
                    for i in last_req.text.split():
                        if i == 'alt=""':
                            break
                        else:
                            list.append(i)
                    prav_list = list[-1].replace('src="', "", 1).replace('"', "", 1)
                    image_url = prav_list
                    response = requests.get(image_url)
                    image_data = BytesIO(response.content)
                    image_data.name = "image.jpg"
                    bot.delete_message(chat_id= call.message.chat.id, message_id=call.message.message_id)
                    bot.send_photo(chat_id= call.message.chat.id, photo=image_data, caption = f'{name} \n\nFN: {quality_list[0]} \nMW: {quality_list[1]} \nFT: {quality_list[2]} \nWW: {quality_list[3]} \nBS: {quality_list[4]}')
                else:
                    bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = f'{name} \n\nFN: {quality_list[0]} \nMW: {quality_list[1]} \nFT: {quality_list[2]} \nWW: {quality_list[3]} \nBS: {quality_list[4]}')

                load = 0
            else:
                None

bot.polling(none_stop=True)