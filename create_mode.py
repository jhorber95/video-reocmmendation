import turicreate as tc

actions = tc.SFrame.read_csv('./dataset/ml-20m/ratings.csv')
items = tc.SFrame.read_csv('./dataset/ml-20m/movies.csv')

training_data, validation_data = tc.recommender.util.random_split_by_user(actions, 'userId', 'movieId')
model = tc.recommender.create(training_data, 'userId', 'movieId')

r = model.recommend(k=5)

most_popular = model.recommend(users=[1, 2, 3, 4, 5], k=3)
most_popular = most_popular.join(right=items, on={'movieId': 'movieId'}, how='inner').sort(['userId', 'rank'],
                                                                                           ascending=True)
most_popular.print_rows(num_rows=15)
items.show()
actions['rating'].show()

model.save('recommendation.model')
