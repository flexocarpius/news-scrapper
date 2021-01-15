class Item():
    def __init__(self, guid=None, title=None, link=None, pub_date=None, description=None, creator=None, category=None, content=None, media=None):
        self.guid = guid
        self.title = title
        self.link = link
        self.pub_date = pub_date
        self.description = description
        self.creator = creator
        self.category = category
        self.content = content
        self.media = media
    
    def to_array(self):
        return [
            self.guid,
            self.title,
            self.link,
            self.pub_date,
            self.description,
            self.creator,
            self.category,
            self.content,
            self.media
        ]

    def __str__(self):
        return 'guid={0}, title={1}, link={2}, pub_date={3}, description={4}, creator={5}, category={6}, content={7}, media={8}'.format(
            self.guid,
            self.title,
            self.link,
            self.pub_date,
            self.description,
            self.creator,
            self.category,
            self.content,
            self.media
        )