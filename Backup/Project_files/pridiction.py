from Scraper import *
import pandas as pd
from datetime import datetime
import json
# import instagram_explore as insta
from Scraper import *


def pdinst(uname):
    res = insta(uname)
    post = res.get("edge_owner_to_timeline_media").get('edges')
    # print("pos",len(post))
    if (len(post)!=0):
        for pic in post:
            utags=pic.get('node').get('edge_media_to_tagged_user').get('edges')
            tags=[]
            if utags:
                # print(utags[0].get('node').get('user').get('username'))
                for t in utags:
                    tags.append(t.get('node').get('user').get('username'))
            else:
                tags=[]
            rcaption = pic.get('node').get('edge_media_to_caption').get('edges')
            caption = []
            if rcaption:
                for c in rcaption:
                    caption.append(c.get('node').get('text'))
            else:
                caption = []
            # decoded_hand = json.dumps(res.data)
            df = pd.DataFrame({
            'Time' : datetime.now(),
            'Bio':[res.get("biography")],
            'Full Name':[res.get("full_name")],
            'is Verified':[res.get("is_verified")],
            'is Private':[res.get("is_private")],
            'Username':[res.get("username")],
            'fb_page': [res.get("connected_fb_page")],
            'No. of Post' : [res.get("edge_owner_to_timeline_media").get("count")],
            'followers' : [res.get("edge_followed_by").get("count")],
            'following' : [res.get("edge_follow").get("count")],
            'Picture URL' : [pic.get('node').get('display_url')],
            'Time of Post' : [datetime.fromtimestamp(pic.get('node').get('taken_at_timestamp'))],
            'Accessibility Caption' : [pic.get('node').get('accessibility_caption')],
            'Likes' : [pic.get('node').get('edge_liked_by').get('count')],
            'Tags' : [tags],
            'No of Tags':[len(tags)],
            'Post Caption' : [caption],
            'is Video' : [pic.get('node').get('is_video')],
            'Comments Counts' : [pic.get('node').get('edge_media_to_comment').get('count')],
            'bussiness' : [res.get('is_business_account')],
            'new_user' : [res.get('is_joined_recently')]
            })
        print("Not Null val ",df)
        df.to_csv('pripro.csv')
        return df

    else:
        df = pd.DataFrame({
        'Time' : datetime.now(),
        'Bio':[res.get("biography")],
        'Full Name':[res.get("full_name")],
        'is Verified':[res.get("is_verified")],
        'is Private':[res.get("is_private")],
        'Username':[res.get("username")],
        'fb_page': [res.get("connected_fb_page")],
        'No. of Post' : [res.get("edge_owner_to_timeline_media").get("count")],
        'followers' : [res.get("edge_followed_by").get("count")],
        'following' : [res.get("edge_follow").get("count")],
        'Picture URL' : [None],
        'Time of Post' : [None],
        'Accessibility Caption' : [None],
        'Likes' : [0],
        'Tags' : [None],
        'No of Tags':[0],
        'Post Caption' : [None],
        'is Video' : [False],
        'Comments Counts' : [0],
        'bussiness' : [res.get('is_business_account')],
        'new_user' : [res.get('is_joined_recently')]
        })
        print("Null val ",df)
        df.to_csv('pripro.csv')
        return df
