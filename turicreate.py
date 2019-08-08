import turicreate as tc

actions = tc.SFrame.read_csv('./dataset/ml-20m/ratings.csv')
items = tc.SFrame.read_csv('./dataset/ml-20m/movies.csv')

training_data, validation_data = tc.recommender.util.random_split_by_user(actions, 'userId', 'movieId')
model = tc.recommender.create(training_data, 'userId', 'movieId')
model.save('recommendation.model')
