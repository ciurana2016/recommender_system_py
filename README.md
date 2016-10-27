# recommender_system_py
This is a submission for the Recommender challenge by @Sirajology on [Youtube](https://youtu.be/9gBC9R-msAk).

## Overview

For this challenge I choose to create a program that recommends artists to users from Last.fm, it takes real data from users and uses a recommendation algorithm to generate the results.

The original dataset file can be found [here](http://www.dtic.upf.edu/~ocelma/MusicRecommendationDataset/lastfm-360K.html), but I took only the 100k first lines for this challenge. The reason for this is that the original file has 17,559,530 lines and weights 1.6G, so I did not want to upload the entire thing or code a downloader on the "fetch_lastfm" function because it took a lot of time to download.

The challenge required you to compare the results of 3 loss functions, but I didnt do it because I didnt know how to. ):

## Dependencies

* numpy (http://www.numpy.org/)
* scipy (https://www.scipy.org/)
* lightfm (https://github.com/lyst/lightfm)

## Usage
Just run
```
recommend_challage.py
```
It will ask you to select 3 users, by id (from 0 to 2033), press Enter after every question and it will give you the recommended artists for the users you selected.

## Credits
Credits to [Siraj](https://github.com/llSourcell)
