# coding: UTF-8

import pynder

facebook_auth_token = 'ZJTvG0IkTlr8pW8bi0RScuG3UwvnuJcS_6dWMBq5XK8.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUUN0WHl0X1Y3M3lLS3FzZldVbGtQeThEcU03cEttbV9RUzNvYTZaVlRGUmwzbVJNdTlJLWdzM0dRdW5naU1URl9hM3BGTm9NZ3ZxOE5qUWNOVkhmNUdQaXBsaFVTM2hldHpxek9MMEEtdGxHaldaSTdjUkFiTWpZbVBreWJNT2tYa0pmaGtUdWJtbDg0N3hVWXl6eUJKcHlSb0JWUWpLVzVWVFZGUXMyRUhsRVZsYmJGNVpkZ05NTE1UQlpzSmtLb181eUc5ZjliX1VScWxOdlBhc2k0TFpWa0kwVzIyRVdZUXZEX0ZxSmhpbTN4Qm9hcWM1TThGdnlkTzhwT1FoN2Z0ZkUxdFh0Mk9yajJEQ2dFeEtjQmpvVkhjYmhUSHJ0eGp4TWtxZk1pd0huTGFPclRJbVB2NFJjcnB5Y2R2R25xUEF0cGpVN2V2Yjl3OVJQZ1lkc1ZlQyIsImlzc3VlZF9hdCI6MTUyNjk1MjA4NiwidXNlcl9pZCI6IjExODI2MzQyODgwOTc1MyJ9' # 取得したFBアクセストークンを入力

session = pynder.Session(facebook_auth_token)
session.matches()  # 既にマッチしたユーザー情報を取得
# session.update_location(LAT, LON) # 位置情報を更新（緯度、経度）
session.profile  # 自分のプロフィール。更新すると本体の方も更新される。
users = session.nearby_users()  # 近くにいるユーザーを取得。

for user in users:
    print('画像'),
    print(user.photos)

    print('名前'),
    print(user.name)

    print('年齢'),
    print(user.age)

    print('BIO'),
    print(user.bio)

    print('誕生日'),
    print(user.birth_date)

    print('最終ログイン時刻'),
    print(user.ping_time)

    print('距離'),
    print(user.distance_km)

    print('学校名'),
    print(user.schools)

    print('職業'),
    print(user.jobs)

    print('共通の友人数'),
    print(user.common_connections)

    if user.common_connections == []: # 共通の知り合いがいるユーザーはLIKEしないようにしてます。
        user.like()
        print('LIKE!!!!!')

    print('==============================================================================')
