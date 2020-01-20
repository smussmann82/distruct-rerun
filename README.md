# distruct-rerun

**NOTE: This package is deprecated and will no longer be updated. It is being merged with the admixturePipeline package. All future updates will be found at https://github.com/stevemussmann/admixturePipeline**

This code was written to help streamline the process of re-running distruct on the major clusters that are found by CLUMPAK (http://clumpak.tau.ac.il/).  It is useful in tandem with my admixture_cv_sum repository (https://github.com/smussmann82/admixture_cv_sum) to determine the best K value for analysis in Admixture (https://www.genetics.ucla.edu/software/admixture/). **Please note that this code only runs properly on the output produced by CLUMPAK when it is provided output from ADMIXTURE runs.  STRUCTURE output analyzed by CLUMPAK is not currently supported, but I plan to add an option for this in the future.  It also assumes you have used my ADMIXTURE Pipeline for running ADMIXTURE (https://github.com/smussmann82/admixturePipeline)**

## Usage:

Download your results from the CLUMPAK server.  This should give you a zipped folder of your results, named something like "1516030453.zip".  First, unzip this folder:
```
unzip 1516030453.zip
```
This should produce a folder in your current directory named 1516030453.  Now, run distruct-rerun.py on your folder.  Assuming that you have installed distruct-rerun.py somewhere in your path, the command will be something like the below command.  In this example, -d is used to give the name of the directory that the program will use as input, -k specifies the lowest clustering value that you tested in Admixture, and -K specifies the highest clustering value you tested.

```
distruct-rerun.py -d 1516030453/ -k 1 -K 12
```
This should have produced a file named MajorClusterRuns.txt in the directory from which you executed distruct-rerun.py.  This file contains all of the names of the .stdout files produced by my admixturePipeline repository that correspond to each of the major clusters recovered by CLUMPAK.  **Copy this file to the directory that contains your output files produced by the admixturePipeline, and cd into that directory.**  You can now get the CV values produced by Admixture by running the following code:
```
for file in `cat MajorClusterRuns.txt`; do grep CV $file >> cv_file.txt; done;
```
You should now have a file named cv_file.txt that contains all of the CV values for your major cluster runs.  The rest of the processing can be accomplished through my admixture_cv_sum repository.
