**Microdistribution Analysis Pipeline**
==========================================

Instructions for reproducible data analysis

====================
Step 1: Run dataCleaning.py
==================== 

-----------
Prerequisites
-----------

Python 3.5.2

------------
Instructions
------------

`python src/dataCleaning.py`



====================
Step 2: Run fixSampleID.sh
====================

---------
Prerequisites
---------

/bin/bash/

-----------
Instructions
-----------


`./fixSampleID.sh`

======================
Step 3: run transectAnalysis.Rmd
======================

----------
Prerequisites
----------

R 3.3.2
- knitr
- ggplot2
- ggtern
- MASS
- vegan

------------
Instructions
------------

```r
library(knitr)
knit('transectAnalysis.Rmd')
```
