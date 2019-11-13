class Post:
  def __init__(self,title,body):
    self.title = title
    self.body = body
    self.comments = [] 
  def add_comment(self,comment): 
    if(comment.subject != ""):
      self.comments.append(comment)
class Comment:
  def __init__(self, subject, body):
    self.subject = subject
    self.body = body
post = Post("Hello Python","Welcome to Python")
comment = Comment("abc","def")
post.add_comment(comment)
#post.comments.append(comment)