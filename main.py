import vk_api

session = vk_api.VkApi(token='vk1.a.v_Uj4tlViF93OgvL8oZusC4V78A94Ff1ud9wydCui2chHRxwI1EIR3WrIw_Uolrdp5H9x77g3oSPN5-afQ-pWNPJ_zh-sAjTr6ry3qfBrT_lRpSzOy72IK9AtsgF2eVMUn2gL4vPKh1QFFOQtRIFqtaKeW9PdbC1hCA4dSxAnlK9v01FiseEfhE5a5HzAf6X29tVV4YuUDPH9YKxrqSJBA')
vk = session.get_api()

def delete_wall(owner_id, post_id):
    session.method('wall.delete', {'owner_id': owner_id, 'post_id':post_id})
    # vk.wall.delete(owner_id, post_id)


def delete_all_wall(count):
    posts = session.method('wall.get', {'count': count})
    posts_list = []
    for post in posts['items']:
        posts_list.append(post['id'])
    
    for post in posts_list:
        delete_wall(310513537, post)
        print(post)

#delete_all_wall(100)
# delete_wall(310513537, 1)


#https://vk.com/wall310513537_1920




