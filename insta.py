from instapy import InstaPy
 2 
 3 session = InstaPy(username="<your_username>", password="<your_password>")
 4 session.login()
 5 session.like_by_tags(["bmw", "mercedes"], amount=5)

session.set_dont_like(["naked", "nsfw"])
session.set_do_follow(True, percentage=50)
session.set_do_comment(True, percentage=50)
session.set_comments(["Nice!", "Sweet!", "Beautiful :heart_eyes:"])

session.end()


#insta.py login.py main.py all need to merge and fix errors#
