# Content Aggregator - [realpython.com](https://realpython.com/intermediate-python-project-ideas/) | Status: *In Progress*
***
#### Objectives:
| TASK                                                                                                                 | Notes                                                                       | Status |
|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|--------|
| Collect data from 5 different sites                                                                                  | So far I have one site being requested\. Will implement more next session\. | 1/5    |
| Store data onto sqlite3                                                                                              | Took me a while to remember all itsfinicky methods, but I got it\.          | Done   |
| Run script in background using celery/apscheduler                                                                    |                                                                             |        |
| Create a website based subscriptiona function that will email aggregateddigest of a particular site data to an email |                                                                             |        |


#### Project Details

>Content is king. It exists everywhere on the web, from blogs to social media platforms. To keep up, you need to search for new information on the internet constantly. One way to stay updated is to check all the sites manually to see what the new posts are. But this is time consuming and quite tiring.

This is where the content aggregator comes in: A content aggregator fetches information from various places online and gathers all of that information in one place. Therefore, you don’t have to visit multiple sites to get the latest info: one website is enough.

With the content aggregator, all of the latest information can be gotten from one site that aggregates all the content. People can see the posts that interest them and can decide to find out more about them without traipsing all over the internet.

The main objective of this project idea is to aggregate content. First, you need to know what sites you’ll want the Content Aggregator to get content from. Then, you can use libraries such as requests for sending HTTP requests and BeautifulSoup to parse and scrape the necessary content from the sites.

Your application can implement its content aggregation as a background process. Libraries such as celery or apscheduler can help with that. You can try out apscheduler. It’s great for small background processes.

After scraping content from various sites, you’ll need to save it somewhere. So, you’ll use a database to save the scraped content.

# Extra Challenge

For a tougher challenge, you can add more websites. This will help you learn how to study and extract information from websites.

You can also have users subscribe to certain sites that you aggregate. Then, at the end of the day, the content aggregator will send the articles for that day to the email address of the user.