# Assessing Fairness in Open-Source Face Mask Detection Algorithms

This GitHub organization gathers six forks of open-source algorithms whose fairness we assessed in the paper "Assessing Fairness in Open-Source Face Mask Detection Algorithms", submitted for RHI@HHAI2023 and currently under review.

We carried out the fairness assessment by checking the performance of these six algorithms over three metrics on two different datasets.

## Methodology

### The datasets

The two datasets we made use of were the following:

1. [Bias Aware Face Mask Detection Dataset (BAFMD)](https://github.com/Alpkant/BAFMD), usage granted with the consent of the owners of the dataset. This is a dataset for face mask detection which was constructed with focus on variability especially in the racial/ethnic component. It does not come along with annotations concerning demographics of the people depicted in its images, but it only provides information on whether the people are or are not wearing face masks, plus the localization (`(x,y)` of the top-left corner, height and width of the bounding boxes). We extracted a subset of 319 images from the validation split, for a total of 695 bounding boxes, and annotated them according to the skin color (dark or light) and sex (female or male) of the faces depicted. The annotations will be released soon in this repo.
2. [FairFace](https://github.com/joojs/fairface): a dataset for face classification with labels on race, sex, and age for each of the face depicted. Every image contains exactly one face. The dataset does not contained masked faces, and info on localization is not provided. We made use of the validation split, which contains 10,954 images.


### The metrics

The models were evaluated on the following metrics:

1. **Localization rate**: the number of faces localized over the total number of faces. A bounding box from the ground truth is defined as _matching_ with a predicted bounding box when their IoU score is larger than 0.5. This metric does not consider the correctness of the prediction (mask vs. no mask) but only the overlap between the two bounding boxes.
2. **True positive rate**: the number of faces correctly predicted as wearing masks over the total number of faces wearing masks that were correctly localized by a model. We decided to remove from the denominator faces not localized by the model in order to isolate the predictive accuracy of the model from its localization capabilities. This metric is not assessable on the dataset FairFace as it contains no images of faces wearing face masks.
3. **True negative rate**: the number of faces correctly predicted as not wearing masks over the total number of faces not wearing masks that were correctly localized by a model. We decided to remove from the denominator faces not localized by the model in order to isolate the predictive accuracy of the model from its localization capabilities.


### Assessment of fairness

The fairness was assessed by testing for statistically significant differences in the rates attained by the models on the two datasets for different demographic groups.
Let `r` be one of the metrics introduced above.
We can calculate `r` on a dataset and a specific group `i`, let's call this rate `r_i`.
We call `r_minus_i` the rate attained by the same model on all the other groups.
We can assess if the difference between the two rates is significant by means of a unpaired binomial test, whose null hypothesis is `H0: r_i = r_minus_i`.
The test statistic can be compared with a Gaussian pdf to obtain the p-value.
We consider a difference _significantly_ biased when the p-value is lower than 0.05.
In addition, we quantify the _effect size_ of the difference by means of Cohen's `h`.
When a difference is significant and Cohen's `h` is greater than 0.2, we define the bias as _severe_.


## Reproducibility

The procedure for reproducing our results is divided in two logical parts, the first being related to the reproducibility of the original implementations, the second being specific to the assessment presented in our work.
We kept each fork of the implementations we analyzed as faithful as possible to the original implementations.
We added information for the reproducibility of our part **at the bottom of each README file** (section **"Reproducing fairness analysis"**).
It follows that the information for, e.g., creating the virtual environment for running the models is contained in the original README file _before_ the section "Reproducing fairness analysis".

### Notes on MOXA

The models for MOXA were not released on GitHub, but on a [custom site](https://shitty-bots-inc.github.io/MOXA/index.html).
We will soon provide information on the reproducibility for these models as well.
