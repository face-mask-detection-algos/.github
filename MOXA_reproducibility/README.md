# Reproducibility of the experiments on MOXA

To reproduce the experiments on MOXA, you should install [Alexey Bochkovskiy's fork of Darknet](https://github.com/AlexeyAB/darknet) on your machine.
After having set up the library, download the weights and configuration files for the desider models from [MOXA's site](https://shitty-bots-inc.github.io/MOXA/index.html).
Then, produce a txt file listing all of the images to be evaluated on the models separated by a newline:

```
---------------
path/to/img1.jpg
path/to/img2.jpg
...
---------------
```

You may then run inference using the following command:

```
./darknet detector test path/to/obj.data path/to/cfh -ext_output -dont_show path/to_weights < path/to/list_of_images.txt > result.txt
```

This will output a .txt file containing the output of Darknet for the recognition.
This file can be converted to a csv keeping only the relevant information by running the `rewrite_output.py` script:

```
python rewrite_output.py --input path/to/darknet_output --output path/to/output.csv --normalize_coordinates
```

This csv file can be then used to compute the match with the ground truth:

```
python match_results_*.py --predictions path/to/predictions.csv --ground_truth path/to/ground_truth --output path/to/output
```

Replace `*` with the relevant dataset name (`bafmd` or `fair`).
This will produce a number of csv files, one per protected attribute and metric, containing the rate attained by the model for each termination of the protected attribute, the p-value of the binomial test, and the Cohen's h for the difference.