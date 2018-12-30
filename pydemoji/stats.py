from .errors import InvalidOption
import aiohttp

async def fetch(option:str):
    async with aiohttp.ClientSession() as session:
        async with session.post(f"https://discordemoji.com/api/?request=stats") as response:
            r = await response.json()

    if option.upper() == 'EMOJI':
        return r['emoji']
    elif option.upper() == 'USERS':
        return r['users']
    elif option.upper() == 'FAVES' or option.upper() == 'FAVOURITES' or option.upper() == 'FAVORITES':
        return r['faves']
    elif option.upper() == 'PENDING' or option.upper() == 'PENDINGAPPROVALS':
        return r['pending_approvals']
    else:
        raise InvalidOption("You have provided an invalid option. Options: Emoji, Users, Faves, Pending")
