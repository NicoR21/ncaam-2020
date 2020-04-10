#!/usr/bin/env bash

unzip ./ncaam/resources/data/google-cloud-ncaa-march-madness-2020-division-1-mens-tournament.zip -d ./ncaam/resources/data && rm ./ncaam/resources/data/google-cloud-ncaa-march-madness-2020-division-1-mens-tournament.zip
if [ ! -d ./ncaam/resources/data/MPlayByPlay_Stage1 ]; then
    mkdir -p ./ncaam/resources/data/MPlayByPlay_Stage1
fi
mv ./ncaam/resources/data/MEvents2015.csv ./resources/data/MPlayByPlay_Stage1
mv ./ncaam/resources/data/MEvents2016.csv ./resources/data/MPlayByPlay_Stage1
mv ./ncaam/resources/data/MEvents2017.csv ./resources/data/MPlayByPlay_Stage1
mv ./ncaam/resources/data/MEvents2018.csv ./resources/data/MPlayByPlay_Stage1
mv ./ncaam/resources/data/MEvents2019.csv ./resources/data/MPlayByPlay_Stage1
mv ./ncaam/resources/data/MPlayers.csv ./resources/data/MPlayByPlay_Stage1
