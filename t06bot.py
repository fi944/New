from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests
from config import *
import asyncio
from telethon import events
from help import *
c = requests.session()
bot_username3 = '@TRS04BOT'


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.بوت لايهم"))
async def _(event):
    if ispay[0] == "yes":
        await event.edit('TRS04BOT')
    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع لايهم"))
async def _(event):
    if ispay[0] == "yes":
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء(@JJXJXX)")
        channel_entity = await sedthon.get_entity(bot_username3)
        await sedthon.send_message('@TRS04BOT', '/start')
        await asyncio.sleep(10)
        msg0 = await sedthon.get_messages('@TRS04BOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(10)
        msg1 = await sedthon.get_messages('@TRS04BOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            if ispay[0] == 'no':
                break
            await asyncio.sleep(10)

            list = await sedthon(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('(@JJXJXX)لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sedthon.send_message(event.chat_id, f"مافي قنوات بلبوت")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sedthon(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sedthon(ImportChatInviteRequest(bott))
                msg2 = await sedthon.get_messages('@TRS04BOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await sedthon.send_message(event.chat_id, f"تم الاشتراك في {chs} قناة")
            except:
                await sedthon.send_message(event.chat_id, f"خطأ , ممكن تبندت(@JJXJXX)")
                break
        await sedthon.send_message(event.chat_id, "تم الانتهاء من التجميع !(@JJXJXX)")

    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")


@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "مرحبا" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    مرحبتين
    
    """)
        
@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "هاي" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    هلا
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "كيفك" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""

      بخير
        
""")

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "صباح الخير " in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""

      صباح النور   
        
""")
        
@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "مساء الخير" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    مساء الفل
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "هو ار يو " in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    ايام فاين
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "سيو" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    هلا بيك
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "مع السلامة" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    الله وياك
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "اترخص" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    اخذ راحتك
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "شكرا" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    العفو
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "شخبارك" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    زي اخبارك
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "شلونج" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    بخير وانتي
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "باي" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    بايات
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "احبك" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    حبك برص 
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "احبج" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    حبتك حية
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "زعلت" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    طبك طوب 
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "تفضل" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    زاد فضلك
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "نورتي" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    نورك
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "نورت" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    بنورك
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "تشرفت" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    الي الشرف
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "حلو" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    انت الاحلى
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "بالتوفيق " in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    حبيبي
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "دوم" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    تدوم الي
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "سلام" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    وعليكم السلام
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "عيوني" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    فديت
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "مح" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    عيب ادبسزز
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "اطلع برا" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    شكرا
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "خاص" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    الخاص للرخاص
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "تعاي" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    جاية
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "تعال" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    اجيت
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "استغفر الله" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    مؤمن
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "شبيج" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    مابيه شي
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "شبيك" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    شعليك
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "شكو" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    ماكو شي
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "ولي" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    تمام
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "ادبسز" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    من زمان
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "احترم" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    اوكي
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "ديلا خوش" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    ولي
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "دروح" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    احترم لك
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "دروحي" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    احترمي ولج
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "مشغول" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    استقر اربعة وعشرين ساعة بزنس 
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "مشغولة" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    براحتج
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "ادري" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    من يمته
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "اعتذر" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    ما صار شي
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "بليز" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    تمام
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "خطية" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    طبها مرض
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "على راسي" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    يسلم راسك
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "قلبي" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    بعد قلبي
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "ها" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    وجعا
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "رايح" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    وين مولي
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "شتحس" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    ماكو حساس بهل وكت
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "حمار " in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    انت حمار لاتجاوز خوش 
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "نعال" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    بحلكك
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "زباله" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    اكبر زباله انت 
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "تحبني" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    حبتك حيه ان شاء الله
    
    """)
