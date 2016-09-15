[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

If the distribution of U.S. men can be modelled by a normal with mean = 178cm and std = 7.7cm, then we can calculate the percentage of men in the range [178cm, 185cm] using the cumulative distribution function of the normal N(178,7.7).  
Concretely, this means simply taking the difference: CDF(x = 185, mean = 178, sig = 7.7) - CDF(x = 178, mean = 178, sig = 7.7)

```python
import scipy
upper = scipy.stats.norm.cdf(185, loc=178, scale=7.7)
lower = scipy.stats.norm.cdf(178, loc=178, scale=7.7)
prct = (upper - lower)*100
print(str(prct) + '% of U.S. men can join the Blue Man Group')
```
output:  
```
31.8348929557% of U.S. men can join the Blue Man Group
```
