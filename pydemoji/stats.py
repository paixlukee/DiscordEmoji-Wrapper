from .errors import InvalidOption
import aiohttp

async def fetch(option:str):
    """
    Fetch DE stats
    
    Parameters
    ----------
    option : str, stat that you want to fetch from the site
    
    Returns
    -------
    string
        data given from the JSON response
        
    Raises
    ------
    InvalidOption
        occurs when the option/endpoint is invalid   
    """
    async with aiohttp.ClientSession() as session:
        async with session.post(f"https://emoji.gg/api/?request=stats") as response:
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
