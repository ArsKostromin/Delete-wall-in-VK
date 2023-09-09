import vk_api #нужно скачать модуль pip install vk_api


user_token = input('Введите ваш токен https://vkhost.github.io   ==>  ')

session = vk_api.VkApi(token=user_token)


def delete_wall(post_id):        #Удаление поста
    session.method('wall.delete', { 'post_id':post_id})


def delete_all_wall(count):
    posts = session.method('wall.get', {'count': count})
    posts_list = []
    for post in posts['items']:
        posts_list.append(post['id'])
    
    for post in posts_list:
        delete_wall(post)
        print(post)

delete_all_wall(100) #Удалить сто постов 




