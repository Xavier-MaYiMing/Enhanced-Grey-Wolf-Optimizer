### Enhanced Grey Wolf Optimizer

##### Reference: Kaiping Luo. Enhanced grey wolf optimizer with a model for dynamically estimating the location of the prey. Applied Soft Computing. 2019,77 :225-235.

| Variables   | Meaning                                                |
| ----------- | ------------------------------------------------------ |
| pop         | The number of wolves                                   |
| iter        | The iteration number                                   |
| lb          | The lower bound (list)                                 |
| ub          | The upper bound (list)                                 |
| pos         | The set of wolves (list)                               |
| score       | The score of wolves (list)                             |
| dim         | Dimension (list)                                       |
| alpha_score | The score of the alpha wolf                            |
| alpha_pos   | The position of the alpha wolf (list)                  |
| beta_score  | The score of the beta wolf                             |
| beta_pos    | The position of the beta wolf (list)                   |
| delta_score | The score of the delta wolf                            |
| delta_pos   | The position of the delta wolf (list)                  |
| prey_pos    | The dynamically estimating position of the prey (list) |
| gbest       | The score of the global best score                     |
| gbest_pos   | The position of the global best (list)                 |
| iter_best   | The global best score of each iteration (list)         |
| con_iter    | The last iteration number when "gbest" is updated      |

#### Test problem: Pressure vessel design

![](https://github.com/Xavier-MaYiMing/Enhanced-Grey-Wolf-Optimizer/blob/main/Pressure%20vessel%20design.png)

$$
\begin{align}
&\text{min}\ f(x)=0.6224x_1x_3x_4+1.7781x_2x_3^2+3.1661x_1^2x_4+19.84x_1^2x_3,\\
&\text{s.t.} \\
&-x_1+0.0193x_3\leq0,\\
&-x_3+0.0095x_3\leq0,\\
&-\pi x_3^2x_4-\frac{4}{3}\pi x_3^3+1296000\leq0,\\
&x_4-240\leq0,\\
&0\leq x_1\leq99,\\
&0\leq x_2 \leq99,\\
&10\leq x_3 \leq 200,\\
&10\leq x_4 \leq 200.
\end{align}
$$


#### Example

```python
if __name__ == '__main__':
    # Parameter settings
    pop = 50
    iter = 2000
    lb = [0, 0, 10, 10]
    ub = [99, 99, 200, 200]
    print(main(pop, iter, lb, ub))
```

##### Output:

![](https://github.com/Xavier-MaYiMing/Enhanced-Grey-Wolf-Optimizer/blob/main/convergence%20curve.png)

The EGWO converges at its 1,271-th iteration, and the global best value is 8050.913534658795. 

```python
{
    'best score': 8050.913534658795, 
    'best solution': [1.3005502034963052, 0.6428626394484327, 67.3860209065443, 10.0], 
    'convergence iteration': 1271
}
```

#### Compared with the GWO on the shifted functions

##### Shifted sphere function

$$
f(x)=\sum_{i=1}^{30}(x_i-0.0001)^2,\qquad x_i\in[-10, 100], \quad i=1,\cdots,30.
$$

![](https://github.com/Xavier-MaYiMing/Enhanced-Grey-Wolf-Optimizer/blob/main/Shifted%20sphere%20function.png)

###### The best value found by the GWO is 1.000035678101285e-08.

###### The best value found by the EGWO is 2.115383003666077e-25.

##### Shifted Rastrigin function

$$
f(x)=\sum_{i=1}^{30}((x_i-1)^2-10\cos(2\pi(x_i-1)) + 10),\qquad x_i\in[-4.12, 5.12], \quad i=1,\cdots,30.
$$

![](https://github.com/Xavier-MaYiMing/Enhanced-Grey-Wolf-Optimizer/blob/main/Shifted%20Rastrigin%20function.png)

###### The best value found by the GWO is 25.32141353244897.

###### The best value found by the EGWO is 8.954631513839622.

##### Conclusion

If the global optimal solution shifts away from the origin of the coordination, the performance of the original GWO deteriorates sharply. The EGWO solves this problem, and its performance on shifted functions proves its effectiveness.
