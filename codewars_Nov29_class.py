# TODO: complete this class
class PaginationHelper:
    
    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
      self.collection = collection
      self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
      return len(self.collection)



    # returns the number of pages
    def page_count(self):
      if len(self.collection)%self.items_per_page == 0 :
        return len(self.collection)/self.items_per_page
      else:
        return int(len(self.collection)/self.items_per_page) +1


    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self,page_index):
      if page_index > self.page_count()-1:
        return -1
      elif page_index < self.page_count()-1:
        return self.items_per_page
      else:
        if len(self.collection)% self.items_per_page ==0 :
          return self.items_per_page
        else:
          return len(self.collection)% self.items_per_page

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self,item_index):
      if item_index < 0 or item_index > self.item_count()-1:
        return -1
      else:
        return int((1+item_index)/self.items_per_page)

helper = PaginationHelper(range(1,25), 10)
print(helper.page_count())
print(helper.page_index(28))
print(helper.item_count())