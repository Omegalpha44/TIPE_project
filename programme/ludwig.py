from ludwig.api import LudwigModel

file_path = "informations/res4.csv"
config = {...}
ludwig_model = LudwigModel(config)
train_stats, _, _  = ludwig_model.train(dataset=file_path)
