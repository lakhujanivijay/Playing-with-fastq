[![Build Status](http://img.shields.io/travis/doge/wow.svg)](https://travis-ci.org/doge/wow)
[![Dependency Status](http://img.shields.io/gemnasium/doge/wow.svg)](https://gemnasium.com/doge/wow)
[![Coverage Status](http://img.shields.io/coveralls/doge/wow.svg)](https://coveralls.io/r/doge/wow)
[![Code Climate](http://img.shields.io/codeclimate/github/doge/wow.svg)](https://codeclimate.com/github/doge/wow)
[![Gem Version](http://img.shields.io/gem/v/suchgem.svg)](https://rubygems.org/gems/suchgem)
[![License](http://img.shields.io/:license-mit-blue.svg)](http://doge.mit-license.org)
[![Badges](http://img.shields.io/:badges-7/7-ff6799.svg)](https://github.com/badges/badgerbadgerbadger)

### About

This program takes a fastq file as an input and gives out the mean phred score for the
user defined base position.

A mean of phred scores will be calculated for user provided base position across all the
reads in the user provided fastq file as provided by "Per Base Sequence Quality" metric
of FastQC tool.

### Usage
`average_phred_score_per_base.py -i <input_fastq> -b <position of base as integer>`

### Example:
`average_phred_score_per_base.py -i input_fastq -b 30`

### Output Example:

```
Mean of 30th base: 23
```

### Dependencies:
Biopython

