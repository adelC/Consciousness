

# Consciousness

## The Consciousness Prior Components

### 1. Uncouscious representation state ![\Large h_{t}](https://latex.codecogs.com/svg.latex?\Large&space;h_{t})

* <img src="https://render.githubusercontent.com/render/math?math=h_{t} = F(x_{t}, h_{t-1})">


#### a. Learning objective
Good representation in <img src="https://render.githubusercontent.com/render/math?math=h_{t}">

### 2. Couscious Representation State <img src="https://render.githubusercontent.com/render/math?math=c_{t}">

### 3. Memory <img src="https://render.githubusercontent.com/render/math?math=m_{t}">

### 4. Verifier Network <img src="https://render.githubusercontent.com/render/math?math=V">

* <img src="https://render.githubusercontent.com/render/math?math=V(h_{t}, c_{t-k}) \in R">

* The Verifier Network role is to match the current represantation state ht with a past couscious state ct-k stored in memory mt-1

#### Mapping ht with the objective function
1. The attention mechanism, eg the Consciousness RNN (we consider using The Perceiver) which selects and combines few elements form the high leve state representation ht into a low-dimentional couscious sub state ct.
2. Predictions or actions derived from the sequence of conscious sub-state <img src="https://render.githubusercontent.com/render/math?math=c_{t} \in R">

## Connection to Symbolic Knowledge Representation

## Considerations

* For this experiment, we will consider the Unsupervised RL framework. we want to test the agent ability to to discover high-level abstractions alone. 

## Glossary 

Factor:  

![Factorgraph](https://user-images.githubusercontent.com/1243127/134007219-49c06ab8-60c6-4c66-90a0-c25b5ad9cb4f.jpeg)
