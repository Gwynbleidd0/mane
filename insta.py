from instaparser.agents import Agent
from instaparser.entities import Account, Media, Location, Tag
def Get_inst(acc):
    anon = Agent()
    account = Account(acc)

    media1, pointer = anon.get_media(account)
#    print(media1)
    print(media1[0])    
    med = Media(media1[0])
    data = anon.update(med)
    typ = data['__typename']
    text = data['edge_media_to_caption']['edges'][0]['node']['text']
    if data['is_video']:
        return(True,data['video_url'],text)
    if not(data['is_video']):
        return(False,data['display_resources'][0]['src'],text)
#print(Get_inst('chp_groznyy'))
