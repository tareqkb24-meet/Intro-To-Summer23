def create_youtube_video(title,description):
  youtube_dict = {"title":title, "description":description, "likes":0, "dislikes":0, "comments": {} }
  return youtube_dict
def like(youtube_video):
  youtube_video["likes"] += 1
  return youtube_video
def dislike(video):
  video["dislikes"] += 1
  return video
def add_comment(video,username,comment_text):
  video["comments"][username] = comment_text
  return add_comment
youtube_video = create_youtube_video("tareq", "this is my first video")
vid = create_youtube_video("tareq","this is my first video")
add_comment(vid,"tareq","nice")
for i in range (495):
  like(vid)
  dislike(vid)
print(vid)


  

 
  
	

