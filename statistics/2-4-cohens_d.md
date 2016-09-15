[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

The effect size of being a first-born on the child's birth weight and the length of the pregnancy are calculated using the following python code:
```python
from __future__ import print_function
import math
import nsfg
preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()
    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d
wfirstbabies = live.birthwgt_lb[live.pregordr == 1]
wotherbabies = live.birthwgt_lb[live.pregordr != 1]
wCD = CohenEffectSize(wfirstbabies,wotherbabies)
print('Effect size of being first-born on birth weight is:' + str(wCD))
lfirstbabies = live.prglngth[live.pregordr == 1]
lotherbabies = live.prglngth[live.pregordr != 1]
lCD = CohenEffectSize(lfirstbabies,lotherbabies)
print('Effect size of being first-born on pregnancy length is:' + str(lCD))
```
Which produced the following output:
```
Effect size of being first-born on birth weight is:-0.0750165286963
Effect size of being first-born on pregnancy length is:0.0139171938336
```
