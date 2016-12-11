This repo is dedicated to benchmarking several ways of boosting Python scripts performance.
Python 2.7, Python 3.5, Nuitka, Cython and pypy are compared for two Python scripts (data generation and data aggregation).

More detailed information on the methodology and result is available in Russian at https://habrahabr.ru/post/276569/.

If you'd like to run the benchmark in your own environment, just clone the repo, make sure you have python, python3, pypy and nuitka installed (also some libs from from requirements.txt) and use command `fab go`.
