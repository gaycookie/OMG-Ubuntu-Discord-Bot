import re, time
from datetime import datetime

class FeedItem:
  def __init__(self, entry):
    self.entry = entry

  def get_id(self):
    id = re.search("\?p=(.+?)$", self.entry.id)
    return id.group(1) if id.group(1) else None

  def get_title(self):
    return self.entry.title if self.entry.title else None

  def get_link(self):
    return self.entry.link if self.entry.link else None

  def get_datetime(self):
    return datetime.fromtimestamp(time.mktime(self.entry.published_parsed))

  def get_summary(self):
    summary = re.search('<p><img .+? \/>(.+?)<\/p>', self.entry.summary)
    return summary.group(1) if summary.group(1) else None

  def get_image(self):
    image = re.search('src\s*=\s*"(.+?)"', self.entry.summary)
    return image.group(1) if image.group(1) else None
