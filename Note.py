from notes import Notes

class Note:

    def __init__(self, title, text):
        self.tag = ['No tag`s']
        self.title = title
        self.text = text
        self.ID = None
    
    def add_tag(self, tag):
        if self.tag == ['No tag`s']:
            self.tag = tag.split(' ')
        else:
            self.tag.append(tag)

    def edit_tag(self, new_tag):
        self.tag = new_tag.split(' ')
    
    def edit_title(self, new_title):
        self.title = new_title

    def edit_text(self, new_text):
        self.text = new_text

    def __str__(self):
        return f'Tag: {self.tag}\nTitle: {self.title}\nText: {self.text}'
    
    
    

