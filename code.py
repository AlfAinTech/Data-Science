from textblob.classifiers import NaiveBayesClassifier

train = [
    ('I love this sandwich.', 'positive'),
    ('this is an amazing place!', 'positive'),
    ('I feel very good about these beers.', 'positive'),
    ('this is my best work.', 'positive'),
    ("what an awesome view", 'positive'),
    ('I do not like this restaurant', 'negative'),
    ('I am tired of this stuff.', 'negative'),
    ("I can't deal with this", 'negative'),
    ('he is my sworn enemy!', 'negative'),
    ('my boss is horrible.', 'negative'),
    ('i hate someone.','negative')
 ]

cl = NaiveBayesClassifier(train)

print (cl.classify("This is an amazing library!"))
print (cl.classify("I hate keyboards"))
print(cl.classify("I love you"))
print(cl.classify("I don't want to travel"))
