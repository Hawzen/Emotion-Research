from glob import glob
from os.path import join
from os import path
import os
from pickle import dump, load

import numpy as np
import pandas as pd

def get_SMADC_folder_data(code_folder_path=""):
    """Returns a dataframe with Text and Region columns."""
    files = glob(join(code_folder_path, "data/SMADC/*.txt"))
    dataframes = []

    for file in files:
        region = file[-7:-4]
        temp_df = pd.read_csv(file, encoding="utf8", delimiter="\r\n", names=["Text"], engine="python")
        temp_df["Region"] = region
        dataframes.append(temp_df)
    
    return pd.concat(dataframes)

def get_annotated_data_folder_data(code_folder_path=""):
    """Returns a dataframe with Text and Region columns."""
    regions = ["egyptian", "gulf", "iraqi", "levantine", "maghrebi"]
    labels = ["EGY", "GLF", "IRQ", "LEV", "NOR"]
    region_to_label = {region:label for region, label in zip(regions, labels)}
    files = [join(code_folder_path, "data", "annotated_data", region) for region in regions]
    
    dfs = [pd.read_csv(file, encoding="utf8", sep="\t", names=["Region", "Text"])[2:] 
        for file in files]
    
    dfs = pd.concat(dfs)
    dfs["Region"] = dfs["Region"].apply(region_to_label.get)
    return dfs

def get_arabic_dialects_dataset_folder_data(code_folder_path=""):
    """Returns a dataframe with Text and Region columns."""
    # CHECK LAV MEANS LEV? # MENTION NO IRQ
    # Filter low quality test?
    labels = ["EGY", "GLF", "LEV", "NOR"]
    regions = [f"all{label if label != 'LEV' else 'LAV'}.txt" for label in labels]
    region_to_label = {region:label for region, label in zip(regions, labels)}
    files = [join(code_folder_path, "data", "ArabicDialectsDataset", "Dialects Full Text", region)
                for region in regions]

    dfs = []
    for file in files:
        norm_file_path = path.normpath(file)
        file_name = norm_file_path.split(os.sep)[-1]

        df = pd.read_csv(file, encoding="utf8", names=["Text"], delimiter="\r\n", engine="python")
        df["Region"] = region_to_label[file_name]
        dfs.append(df)
        
    return pd.concat(dfs)

def get_dart_folder_data(code_folder_path=""):
    """Returns a dataframe with Text and Region columns."""
    # What about dart gold? what is it
    # Filter low quality test?
    labels = ["EGY", "GLF", "IRQ", "LEV", "NOR"]
    regions = [region + ".txt" for region in ["EGY", "GLF", "IRQ", "LEV", "MGH"]]
    region_to_label = {region:label for region, label in zip(regions, labels)}
    files = [join(code_folder_path, "data", "DART", "cf-data", region)
                for region in regions]

    dfs = []
    for file in files:
        norm_file_path = os.path.normpath(file)
        file_name = norm_file_path.split(os.sep)[-1]

        df = pd.read_csv(file, delimiter="\t",encoding="utf8", names=["_", "__", "Text"])
        df["Region"] = region_to_label[file_name]
        df = df[["Text", "Region"]].iloc[1:]
        dfs.append(df)
        
    return pd.concat(dfs)

def get_music_df(code_folder_path=""):
    files = ["GLF","LEV","NOR","IRQ"]
    dataframes = []
    
    for file in files:
        temp_df = pd.read_csv(join(code_folder_path, f"data/extra_data/d7_data/{file}.txt"), encoding="utf8", delimiter="\n", names=["Text"])
        temp_df["Region"] = file
        dataframes.append(temp_df)
    
    return pd.concat(dataframes)

def get_arabic_lexicon_data(code_folder_path=""):
    """Returns a dictionary of emotions and a list of words that represent them. e.g. {emotion1: [word1, word2, word3, ..], ..}"""
    path_to_files = join(code_folder_path, "data", "emotion-lexicon-master", "arb", "*")
    paths = glob(path_to_files)
    emotions = [path[path.rfind("\\")+1:path.rfind(".")] for path in paths]
    emotion_to_words = {}
    for emotion, path in zip(emotions, paths):
        with open(path, encoding="utf8") as file:
            emotion_to_words[emotion] = file.read().split()
    return emotion_to_words
