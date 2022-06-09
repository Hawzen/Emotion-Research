# Emotion research

Research about emotions in Arabic dialects

## Notebooks

| **Notebook**                               | **Description**                                                                                               | **Notes**                                      |
|--------------------------------------------|---------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| generate_embeddings.ipynb                  | Trains and saves unsupervised embeddings to _embeddings/_ folder using the SMADC dataset in the _data_ folder |                                                |
| find_centroids.ipynb                       | Attempts to cluster emotions from embeddings, then generate similar words from each emotion cluster.          | Requires running generate_embeddings.ipynb     |
| test_lexicons.ipynb                        | Tests lexicon hand picked by researchers (from find_centroids.ipynb).                                         |                                                |
| mapping_embeddings_to_other_dialects.ipynb | Attempts to map embeddings cross dialectically                                                                | Is not supported by the environment in env.yml |

## Environment

Using conda import environment using ```conda env create --file env.yml``` then activate it using ```conda activate emotion_research```

##### fasttext

Windows users facing issues installing fasttext can download fasttext binaries from https://www.lfd.uci.edu/~gohlke/pythonlibs/#_fasttext then run ```pip install [WHEEL_FILE]```