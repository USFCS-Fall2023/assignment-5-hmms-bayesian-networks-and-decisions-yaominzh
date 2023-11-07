[toc]

by YaoMin(Allen) Zhang
# Part 1

## 1.1 Question 1
Speed table, unit is km/h

 Sandy | Smooth | Rocky
 ---   | ---    | ---
 3 | 5 | 2


Route | Length | Sandy | Smooth | Rocky | Expectation of time calulation | ET 
--- | --- | --- | --- | --- | --- | ---
1 | 2 | 0.2 | 0.3 | 0.5 | 2/3 * 0.2 + 2/5 * 0.3 + 2/2 * 0.5 = 0.75  | 0.75
2 | 1.8 | 0.4 | 0.2 | 0.4 | 1.8/3 * 0.4 + 1.8/5 * 0.2 + 1.8/2 * 0.4 = 0.672 | 0.672
3 | 3.1 | 0.5 | 0.4 | 0.1 | 3.1/3 * 0.5 + 3.1/5 * 0.4 + 3.1/2 * 0.1 = 0.95 | 0.95

Route 2 is the best route to take.


## 1.2 Question 2

Route |  Expected time from step 1 | special case | New expected time
--- | --- | --- | ---
1 | 0.75 | 0.3 chance of add 0.75 | (0.75+0.75) * 0.3 + 0.75 * 0.7 = 0.975
2 | 0.672 | 0.6 chance of add 1 | (0.672+1) * 0.6 + 0.672 * 0.4 = 1.272
3 | 0.95 | no special case | 0.95

Route 3 is the best route to take.

## 1.3 Now suppose that we can use a satellite to find out whether the terrain in route 3 is smooth.  Is this helpful? What is the value of this information? Expressed differently, how long are we willing to wait for this information from the satellite?

Yes, it is helpful. 
If the terrain is smooth, then the expected time is 3.1/5 = 0.62.
If the terrain is not smooth, then the expected time is 3.1/3 * (0.5/0.6) + 3.1/2 * (0.1/0.6) = 1.12

By calculation 1.12-0.62 = 0.5, so we are willing to wait for 0.5 hours for this information from the satellite.

## 1.4 Now put this problem into ChatGPT. Is it able to solve it correctly? If not, where does it make mistakes?

For 1.1 not correct. The main reason is it messed up all the calculations, but it did give a good answer structure.

For 1.2, it got the right answer. While for this step, I fed GPT with my 1.1 answer, and the calculation is simple. 

For 1.3, at first, it just beat around the bush and didn't give a clear answer, like it just gave a long talk about Time Savings, Cost of Delay, Reliability of Satellite Data, Resource Availability. 

# Part 2
## 2.1 implement load, use two_english as a sample file
[HMM.py](HMM.py)

test
[submission.py](submission.py)

## 2.2 implement generate

[HMM.py](HMM.py)


# Part 3 

## 3.1 Modify query to determine probabilities
[pgm_alarm.py](pgm_alarm.py)

## 3.2 representing the car starting problem
[carnet.py](carnet.py)

## 3.3 add KeyPresent node
[carnet_keypresent.py](carnet_keypresent.py)

#  Part 4

## 4.1 What are the three dimensions along which Big Tech has an advantage in AI?

- The Data Advantage - Firms with access to more behavioral data have advantage in developing consumer AI products.
- Computing Power Advantage - Because AI relies heavily on substantial computing resources.
- Geopolitical Advantage - AI companies are positioned as crucial assets in the US-China AI race

## 4.2 Why does AI Now think it's important to focus on Big Tech?

AI Now focuses on Big Tech because these companies have an outsized impact on the AI ecosystem and economy more broadly. The report argues reasons as follows:
- Tackling challenges that either originate from or are exemplified by Big Tech
  companies can address the root cause of several key concerns
- The Big Tech business and regulatory playbook has a range of knock-on effects on the broader ecosystem, incentivizing and even compelling other companies to fall in line
- Growing dependencies on Big Tech across the tech industry and government make them a single point of failure.

## 4.3  Priority 1 discusses Algorithmic Accountability. What does this mean? Why is it important to shift responsibility for detecting harm on companies themselves?
AINow has another section for Algorithmic Accountability.(https://ainowinstitute.org/publication/algorithmic-accountability)

- What are the windows for action that are identified? Which do you personally think are the most effective or promising?

- The executive summary contains this quote:

"These are only a handful of examples, and what they make clear is that there is nothing about
artificial intelligence that is inevitable. Only once we stop seeing AI as synonymous with progress
can we establish popular control over the trajectory of these technologies and meaningfully confront
their serious social, economic, and political impacts—from exacerbating patterns of inequality in
housing, credit, healthcare, and education to inhibiting workers’ ability to organize and incentivizing
content production that is deleterious to young people’s mental and physical health."

Do you agree with this assessment? How might we rethink our relationship with AI and with technology in order to avoid these potential negative outcomes?

Now paste this last question into ChatGPT and include its response. How do you compare its output to your own? 


# Reflection

- In this assignment 5, we have two questions about analysing ChatGPT's output. ChatGPT is getting more and more powerful. As we evaluated in assignment 1, ChatGPT is good at  



