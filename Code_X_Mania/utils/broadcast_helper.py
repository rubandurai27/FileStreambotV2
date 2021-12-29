# (c) @AbirHasan2005
from Code_X_Mania.vars import Var
import asyncio
import traceback
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid

async def send_msg(user_id, message):
    try:
        if Var.BROADCAST_AS_COPY is False:
            await message.forward(chat_id=user_id)
        elif Var.BROADCAST_AS_COPY is True:
            await message.copy(chat_id=user_id)
        return 200, None
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return send_msg(user_id, message)
    except InputUserDeactivated:
        return 400, f"{user_id} : deactivated\n"
    except UserIsBlocked:
        return 400, f"{user_id} : blocked the bot\n"
    except PeerIdInvalid:
        return 400, f"{user_id} : user id invalid\n"
    except Exception as e:
        return 500, f"{user_id} : {traceback.format_exc()}\n"
