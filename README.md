# merrer
M(app)er (and) R(educ)er

[G4G](https://www.geeksforgeeks.org/hadoop-streaming-using-python-word-count-problem/) with comments removed, utf tag added, and converted to Python3. 

Works over text files with a Python3 installed and execute permissions.

```
mapred streaming \
  -input ??? \
  -output ??? \
  -mapper mapper.py \
  -reducer reducer.py \
  -file mapper.py \
  -file reducer.py
```

# Hadoop Streaming with Python - Alaina's Attempt

## Overview
This repository contains Python scripts for a Hadoop Streaming job. The job reads text files, processes the words, and counts the occurrences of each word.

## Files
- `mapper.py`: Mapper script that reads lines from the input, finds contiguous strings of letters, converts them to lowercase, and outputs each word with a count of 1.
- `reducer.py`: Reducer script that reads key-value pairs, aggregates the counts for each word, and outputs the total count for each word.



## Running the Hadoop Streaming Job
1. Upload the books to HDFS:
    ```bash
    hdfs dfs -mkdir /user/sandbox/books
    hdfs dfs -copyFromLocal -f books/* /user/sandbox/books
    ```

2. Run the streaming job:
    ```bash
    mapred streaming \
      -input /user/sandbox/books \
      -output /user/sandbox/words \
      -mapper mapper.py \
      -reducer reducer.py \
      -file scripts/mapper.py \
      -file scripts/reducer.py
    ```

3. View the output:
    ```bash
    hdfs dfs -ls /user/sandbox/words
    hdfs dfs -head /user/sandbox/words/part-00000
    ```
