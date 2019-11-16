#from flask_appbuilder import Model

COMMENTS = []
class Comments(object):    
    def __init__(self):
        self.comments = COMMENTS
    
    def add_comment(self, id, body):
        comment = {
            'id':id,
            'body':body
        }

        self.comments.append(comment)
        return comment

    def get_comment(self, id):
        comment = filter(lambda comment: comment['id'] == id, self.comments)
        return comment

    def edit_comment(self, id, body):
        comment = self.get_comment(id)
        comment.body = body
        return comment
