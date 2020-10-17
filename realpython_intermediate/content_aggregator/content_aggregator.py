import requests
import sqlite3
from prettytable import PrettyTable
from scrapy.selector import Selector
import logging

sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS {table_name} (
                                id INTEGER PRIMARY KEY,
                                post_id INTEGER NOT NULL,
                                title text NOT NULL UNIQUE,
                                story_link TEXT NOT NULL);'''

sqlite_write_row = '''INSERT INTO {table_name} VALUES (?,?,?,?)'''

class CA:
    def __init__(self):
        self.newsy_main_url = "https://news.ycombinator.com/news"
        self.newsy_post = "https://news.ycombinator.com/item?id={post_id}"
        self.response = None
        self.table_name = None
        self.posts = {}
        
    def fetch_data(self):
        # Handeling my own request instead using scrapy HtmlResponse function because...
        # overhead?
        self.response = requests.get(self.newsy_main_url)
        #logging.DEBUG("Response is {}".format(self.response))
        counter = 0
        for post in Selector(text=self.response.content).css("tr.athing").extract():
            self.posts[counter] = {"post_id": Selector(text=post).xpath("//tr/@id").extract_first(),
                              "title": Selector(text=post).css("td.title a::text").extract_first(),
                              "story_link": Selector(text=post).css("td.title > a.storylink::attr(href)").extract_first()}
            counter += 1

    def write_data_newsy(self):
        self.table_name = Selector(text=self.response.url).xpath("//body/p/text()").re_first("(?<=https://news.).*(?=.com)")
        #sqlite_create_table_query = sqlite_create_table_query.format(self.table_name)
        conn = sqlite3.connect('caDB.db')
        crsr = conn.cursor()
        print(self.table_name)
        crsr.execute(sqlite_create_table_query.format(table_name=self.table_name))
        for post in self.posts.keys():
            crsr.execute(sqlite_write_row.format(table_name=self.table_name), [post, self.posts[post]["post_id"], self.posts[post]["title"], self.posts[post]["story_link"]])
            conn.commit()
        crsr.close()

    def print_data_newsy(self):
        pt_table = PrettyTable()
        pt_table.field_names = ["Post_ID", "Title", "Story Link"]
        table_name = Selector(text=self.response.url).xpath("//body/p/text()").re_first("(?<=https://news.).*(?=.com)")
        print(table_name)
        counter = 0
        for post in Selector(text=self.response.content).css("tr.athing").extract():
            title = Selector(text=post).css("td.title a::text").extract_first()
            post_id = Selector(text=post).xpath("//tr/@id").extract_first()
            storylink = Selector(text=post).css("td.title > a.storylink::attr(href)").extract_first()
            counter += 1
            pt_table.add_row([post_id, title, storylink])
        print(pt_table)


if __name__ == '__main__':
    CA = CA()
    CA.fetch_data()
    CA.print_data_newsy()
    CA.write_data_newsy()