from .errors import InvalidQuery, InvalidOption
import aiohttp

async def fetch(by:str, query, endpoint=None, case_sensitive=None):
    """
    Fetch an emoji
    
    Parameters
    ----------
    by : str, fetch an emoji by (option)
    query : query that you want to search for
    endpoint : optional, if left None, JSON response will be returned
    case_sensitive : bool, optional, if left None, it will NOT be case sensitive
    
    Returns
    -------
    string
        data given from the JSON response (if endpoint)
    JSON
        JSON response, not messed with (if endpoint is None)
        
    Raises
    ------
    InvalidQuery
        occurs when the query is not listed on the site or the query is improperly formatted
    InvalidOption
        occurs when the option/endpoint is invalid   
    """
    options = ['title', 'id', 'slug']
    by = by.lower()
    if by in options:
        async with aiohttp.ClientSession() as session:
            async with session.post(f"https://emoji.gg/api/") as response:
                r = await response.json()
        latest_emoji = ''
        for emoji in r:
            if not case_sensitive or case_sensitive == False:                
                if emoji[by] == query:
                    latest_emoji = emoji
                else:
                    pass
             else:
                if emoji[by].lower() == query.lower():
                    latest_emoji = emoji
                else:
                    pass
        if latest_emoji == '':
            raise InvalidQuery("The query you have given is not listed on the site.")
        else:
            if not endpoint:
                return latest_emoji
            else:
                endpoints = ['title', 'id', 'slug', 'image', 'category', 'license', 'source', 'faves', 'submitted_by']
                endpoint = endpoint.lower().replace('author', 'submitted_by').replace('favourite', 'faves').replace('favorite', 'faves')
                if not endpoint in endpoints:
                    available = ", ".join(endpoints)
                    raise InvalidOption(f"You have provided an invalid endpoint. Available Endpoints: {available}")
                else:
                    if endpoint == '':
                        return None
                    else:
                        return latest_emoji[endpoint]

    else:
        available = ", ".join(options)
        raise InvalidOption(f'You have provided an invalid option. Options: {available}')
