import vk_api



#user_token = input('Введите ваш токен https://vkhost.github.io   ==>  ')

session = vk_api.VkApi(token='vk1.a.QzRAo7KUj1qSWql8rmAuoDdCJ9jjEDvbkA0074NY0_p4_mpVIxSdnZLlrjDgl49MR5Nb-LdUQMY99wM_zS5g1msDggH9yTqYKRxk308Ew6x-tpwVBsRUKQFxLwCWcUpbM75QIOCFKawwJxi5kiFV25Fw44d9-E2I6NUqM2276jDCstSudzbBty5ZFBmlXNFUTwk-cCsxZuLCWeu9tEa2QQ')
vk = session.get_api()


user_id = session.method('user_id.get')

print(user_id)

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


#vk1.a.QzRAo7KUj1qSWql8rmAuoDdCJ9jjEDvbkA0074NY0_p4_mpVIxSdnZLlrjDgl49MR5Nb-LdUQMY99wM_zS5g1msDggH9yTqYKRxk308Ew6x-tpwVBsRUKQFxLwCWcUpbM75QIOCFKawwJxi5kiFV25Fw44d9-E2I6NUqM2276jDCstSudzbBty5ZFBmlXNFUTwk-cCsxZuLCWeu9tEa2QQ




