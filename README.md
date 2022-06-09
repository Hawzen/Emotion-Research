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

## Credits

### Data

| **Dataset**               | **Source**                                                                                                                                                                                                                                                                                                                                                             |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SMADC                     | Areej Alshutayri and Eric Atwell. Classifying arabic dialect text in the social media arabic dialect corpus (smadc). 01 2021.                                                                                                                                                                                                                                          |
| AOC-dialectal-annotations | Ryan Cotterell and Chris Callison-Burch. A multi-dialect, multigenre corpus of informal written Arabic. In Proceedings of the Ninth International Conference on Language Resources and Evaluation (LREC’14), pages 241–245, Reykjavik, Iceland, May 2014. European Language Resources Association (ELRA).                                                              |
| annotated_data            | Omar F. Zaidan and Chris Callison-Burch. The Arabic online commentary dataset: an annotated dataset of informal Arabic with high dialectal content. In Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies, pages 37–41, Portland, Oregon, USA, June 2011. Association for Computational Linguistics. |
| Dart                      | Israa Alsarsour, Esraa Mohamed, Reem Suwaileh, and Tamer Elsayed. DART: A large dataset of dialectal Arabic tweets. In Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018), Miyazaki, Japan, May 2018. European Language Resources Association (ELRA).                                                               |
| extra_data                | Us                                                                                                                                                                                                                                                                                                                                                                     |

### Superviser

Dr. Nasser A. AlSadhan

### Researchers
[Abdulrahman Al-Shawi](https://github.com/d7miiZ) </br>
[Musaad Al-Qubayl](https://github.com/musaad0) </br>
[Khaled Al-Bader](https://github.com/khalid-albadr) </br>
[Abdullah Al-Suwailem](https://github.com/Abdullah-Sw) </br>
[Mohand Al-Rasheed](https://github.com/Hawzen) </br>
