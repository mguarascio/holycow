

class News():
    def __init__(self, results):
        self.id = results['id']
        self.description = results['description']
        self.headline = results['headline']
        self.link_text = results['linkText']
        self.published = results['published']
        self.type = results['type']
        self.links = results['links']
