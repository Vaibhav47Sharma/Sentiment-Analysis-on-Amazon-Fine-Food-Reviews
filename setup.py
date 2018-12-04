import json, csv, gzip, requests

class ReviewModel:
  #Model class for review
  def __init__(self, json_input):
    self.product_id = ReviewModel.get_val_from_dict('product/productId', json_input)
    self.user_id = ReviewModel.get_val_from_dict('review/userId', json_input)
    self.profile_name = ReviewModel.get_val_from_dict('review/profileName', json_input)
    self.helpfulness = ReviewModel.get_val_from_dict('review/helpfulness', json_input)
    self.score = ReviewModel.get_val_from_dict('review/score', json_input)
    self.time = ReviewModel.get_val_from_dict('review/time', json_input)
    self.summary = ReviewModel.get_val_from_dict('review/summary', json_input)
    self.text = ReviewModel.get_val_from_dict('review/text', json_input)

  @classmethod
  def get_val_from_dict(cls, dict_key, dict_input):
    #Method which takes in a dict, returns the value against the key specified if present. It returns a blank in the absence of a key.
    return dict_input[dict_key] if dict_key in dict_input else ''

#Download the dataset from this url and save it as finefoods.txt.gz
url = 'https://snap.stanford.edu/data/finefoods.txt.gz'
r = requests.get(url, allow_redirects=True)
open('finefoods.txt.gz', 'wb').write(r.content)

#Open a writable connection to a csv file to copy all the data to this file
file = open(r'food_reviews.csv', 'w')
writer = csv.writer(file, delimiter=',', lineterminator='\n')
writer.writerow(
    ['product/productId', 'review/userId', 'review/profileName', 'review/helpfulness', 'review/score', 'review/time', 'review/summary', 'review/text'])


def parse(filename):
  #Creating a dict of all the entries in the gzip file
  f = gzip.open(filename, 'rt')
  entry = {}
  for l in f:
    l = l.strip()
    colonPos = l.find(':')
    if colonPos == -1:
      yield entry
      entry = {}
      continue
    eName = l[:colonPos]
    rest = l[colonPos+2:]
    entry[eName] = rest
  yield entry

for line in parse('finefoods.txt.gz'):
  review_model = ReviewModel(line)
  #Writing all the data to the csv
  writer.writerow([review_model.product_id, review_model.user_id, review_model.profile_name, review_model.helpfulness, review_model.score, review_model.time, review_model.summary, review_model.time])

file.close()  
