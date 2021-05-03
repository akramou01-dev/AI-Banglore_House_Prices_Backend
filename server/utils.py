import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None


def get_estimated_price(location,sqft,bath,bhk):
    try: 
        loca_index = __data_columns.index(location.lower())
    except:
        loca_index = -1

    x=np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loca_index >=0: 
        x[loca_index] =1

    return round(__model.predict([x])[0],2)


def get_locations():
    return __locations


def load_saved_artifacts():
    print("************loading saved artifacts**************")
    global __locations
    global __data_columns
    global __model

    with open("./artifacts/columns.json", "r")as f:
        __data_columns = json.load(f)["data_columns"]
        __locations = __data_columns[3:]

    with open("./artifacts/Banglore_home_prices_model.pickle", "rb") as f:
        __model = pickle.load(f)


if __name__ == "__main__":
    load_saved_locations()
    # print(get_estimated_price("neeladri nagar",250,3,3))
    # print(get_estimated_price("neeladri nagar",250,3,3))
    # print(get_estimated_price("1st phase jp nagar",1000,2,2))
    # print(get_estimated_price("9th phase jp nagar",500,1,2))
