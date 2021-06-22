import feedparser
from feed_item import FeedItem

class Feed:
  def __init__(self, url):
    self.url = url
    self.last_item = None

    #self.fetch()

  def fetch(self):
    feed = feedparser.parse("https://www.omgubuntu.co.uk/feed")
    item = FeedItem(feed.entries[0])

    if self.last_item:
      if self.last_item.get_id() != item.get_id():
        self.last_item = item
        return self.last_item
      else:
        return None
    else:
      self.last_item = item
      return None