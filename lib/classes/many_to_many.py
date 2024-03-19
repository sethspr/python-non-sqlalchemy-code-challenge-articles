class Article: # many to one
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = title #Ben said we shouldn't do this, but it would only pass the test if I had self._title = title. 
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str) and 5 <= len(new_title) <= 50 and not hasattr(self, '_title'):
            self._title = new_title
        else:
            print(f'Invalid title: {new_title}')

    def __repr__(self):
        return f'{self.title} by {self.author.name} in {self.magazine}'
        
class Author: #many to many
    all = []
    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name) > 0 and not hasattr(self, '_name'):
            self._name = new_name   
        else:
            print(f'invalid name: {new_name}')
    def articles(self):
        result_list = []
        for result_obj in Article.all:
            if result_obj.author is self:
                result_list.append(result_obj)
        return result_list

    def magazines(self):
        magazine_list = []
        for result_obj in self.articles():
            if result_obj.magazine not in magazine_list:
                magazine_list.append(result_obj.magazine)
        return magazine_list

    def add_article(self, magazine, title):
        article_1 = Article(self, magazine, title)
        return article_1

    def topic_areas(self):
        pass

class Magazine: #many to many
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        result_list = []
        for result_obj in Article.all:
            if result_obj.magazine is self:
                result_list.append(result_obj)
        return result_list

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass

# article_1 = Article("Author, some guy", "Magazine Vogue", 123)
# add_article_1 = Author.add_article( "testing magazine", "testing title")
author_1 = Author("charlotte is an author")
magazine_1 = Magazine("British Mag", "category any")
title_1 = "this is a title"
article_2 = author_1.add_article(magazine_1, title_1)

print(magazine_1.articles())
