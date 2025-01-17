from pyrogram import filters
from pyrogram.types import Message

from StringGen import Anony
from StringGen.utils import add_served_user, keyboard


@Anony.on_message(filters.command("start") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    await message.reply_text(
        text=f"ʜᴇʏ {message.from_user.first_name},\n\n๏ ᴛʜɪs ɪs {Anony.mention},\nᴄʟɪᴄᴋ ᴏɴ ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ🌱.\n🙂ᴜꜱᴇ ᴛʜɪꜱ ᴀᴘɪ ꜰᴏʀ ꜱᴛʀɪɴɢ ꜰɪʟᴇ ɪꜰ ʏᴏᴜ ᴅᴏɴ'ᴛ ᴡᴀɴᴛ ᴛᴏ ᴜꜱᴇ ʏᴏᴜʀ ᴏᴡɴ ᴀᴘɪ.\n<blockquote><b>🥀ᴀᴘɪ ɪᴅ :12380656\n🌲ᴀᴘɪ_ʜᴀꜱʜ :d927c13beaaf5110f25c505b7c071273</b></blockquote>",
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
    await add_served_user(message.from_user.id)
