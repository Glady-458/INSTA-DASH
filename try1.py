import json
import instagram_explore as insta
from datetime import datetime
# from try2 import *
from datetime import datetime
import pandas as pd


df = pd.DataFrame({'Time':[],
'Bio':[],
'Full Name':[],
'is Verified':[],
'is Private':[],
'Username':[],
'fb_page':[],
'No. of Post':[],
'followers':[],
'following':[],
'Picture URL':[],
'Time of Post':[],
'Accessibility Caption' : [],
'Likes' : [],
'Tags':[],
'No of Tags':[],
'Post Caption':[],
'is Video' :[],
'Comments Counts' : []
})
df.to_csv('kind.csv', mode = 'w', header = True)
def inst(uname):
    res = insta(uname)
    # res = insta.user(uname)
    # decoded_hand = json.dumps(res.data)
    # df = pd.DataFrame({
    # 'Time' : datetime.now(),
    # 'Bio':[res.data.get("biography")],
    # 'Full Name':[res.data.get("full_name")],
    # 'is Verified':[res.data.get("is_verified")],
    # 'is Private':[res.data.get("is_private")],
    # 'Username':[res.data.get("username")],
    # 'fb_page': [res.data.get("connected_fb_page")],
    # 'No. of Post' : [res.data.get("edge_owner_to_timeline_media").get("count")],
    # 'followers' : [res.data.get("edge_followed_by").get("count")],
    # 'following' : [res.data.get("edge_follow").get("count")]
    # })
    # df.append(df, ignore_index=True,sort=False)
    # df.to_csv('kind.csv', mode = 'a', header = False)
    # print(type(res.data))
    # print(res.data.get("biography"))
    # print(res.data.get("full_name"))
    # print(res.data.get("is_private"))
    # print(res.data.get("is_verified"))
    # print(res.data.get("username"))
    # print(res.data.get("connected_fb_page"))
    # print(res.data.get("edge_owner_to_timeline_media").get("count"))
    # print(res.data.get("edge_followed_by").get("count"))
    # print(res.data.get("edge_follow").get("count"))
    # print("*********************Photos**********************")
    post = res.get("edge_owner_to_timeline_media").get('edges')
    # print(len(post))
    # print(post[0].get('node').get('edge_liked_by'))
    # print(post[0])
    # return(res.data.get("biography"),res.data.get("full_name"),res.data.get("is_private"),res.data.get("is_verified"),res.data.get("username"),res.data.get("connected_fb_page"),res.data.get("edge_owner_to_timeline_media").get("count"),res.data.get("edge_followed_by").get("count"))

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
        'is Video' : [pic.get('node').get('is_video'),],
        'Comments Counts' : [pic.get('node').get('edge_media_to_comment').get('count')]
        })
        # print("******************")
        # print(pic.get('node').get('display_url'))
        # print(pic.get('node').get('accessibility_caption'),"<- accessibility_caption")
        # print(pic.get('node').get('edge_liked_by').get('count'),"<-likes")
        # print(tags,"<-tags")
        # print(caption,"<-caption")
        # print(pic.get('node').get('is_video'),"<-is video")
        # print(pic.get('node').get('edge_media_to_comment').get('count'),"<-commets count")
        # print(datetime.fromtimestamp(pic.get('node').get('taken_at_timestamp')),"<-time of post")
        df.append(df, ignore_index=True,sort=False)
        df.to_csv('kind.csv', mode = 'a', header = False)


    # print(type(decoded_hand))
# inst("glady_458")
print("#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#")
# print(df)
# inst('subhojitjana')
def hashtag(Hash):
    res2 = insta.tag('bike')
    hashtag = res2.data.get("edge_hashtag_to_media").get('edges')
    p1=hashtag[0].get('node').get('edge_media_to_caption').get('edges')
    c = 0
    for edges in hashtag:
        # print(c)

        c = c+1

        cap = edges.get('node').get('edge_media_to_caption').get('edges')
        for cap in cap:
            print(cap.get('node').get('text'))

# print(inst("subhojitjana"))
# inst("suraj_singh07")
# inst("glady_458")
# hashtag("bike")
