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
Algorithmic accountability refers to the growing policy focus on requiring transparency, auditing, and access to data from tech companies as a way to address harms caused by AI systems.
This is important because the current approach plays into the tech industry's interests by keeping accountability outside  the company. It allows companies to position themselves as cooperating through audits while avoiding fundamental changes.

## 4.4 What are the windows for action that are identified? Which do you personally think are the most effective or promising?

In the "Windows for policy movement" section, the windows for action are identified as follows:
 - Contain tech firms' data advantage
 - Build support for competition reforms as a key lever to reduce concentration in tech
 - Regulate ChatGPT and other large-scale models.
 - Displace audits as the primary policy response to harmful AI.
 - Future-proof against the quiet expansion of biometric surveillance into new domains like cars
 - Enact strong curbs on worker surveillance. 
 - Prevent “international preemption” by digital trade agreements that can be used to weaken national regulation on algorithmic accountability and competition policy

I think the most effective is building support for competition reforms and enacting strong curbs on worker surveillance. Competition reform can address the root cause of concentration of power and data advantages that many problems stem from. Curbing worker surveillance not only protects workers directly, but could force changes in business models and systems built around extensive monitoring and control.

## 4.5 The executive summary contains this quote:

"These are only a handful of examples, and what they make clear is that there is nothing about
artificial intelligence that is inevitable. Only once we stop seeing AI as synonymous with progress
can we establish popular control over the trajectory of these technologies and meaningfully confront
their serious social, economic, and political impacts—from exacerbating patterns of inequality in
housing, credit, healthcare, and education to inhibiting workers’ ability to organize and incentivizing
content production that is deleterious to young people’s mental and physical health."

Do you agree with this assessment? How might we rethink our relationship with AI and with technology in order to avoid these potential negative outcomes?

I agree with this assessment. In my view, there are a few ways we could rethink the relationship with AI and technology to avoid potential negative outcomes. Keeping human rights, ethics, and wellbeing as the focus for AI rather than efficiency or profit would steer development toward more responsible use cases. Laws and norms reinforcing those values are important. Applying AI in sensitive social domains like healthcare, law enforcement, etc. requires extremely careful evaluation to avoid automating and exacerbating existing biases or inequities. Slow, thoughtful adoption is prudent.

## 4.6 Now paste this last question into ChatGPT and include its response. How do you compare its output to your own? 
ChatGPT's reply is as following. I think it covers more area. And it can be a good strcture to do further exploration on this topic. 

ChatGPT:
The assessment touches on important concerns regarding the impact of AI on society, and many experts in the field share similar thoughts. The statement underscores the belief that AI development should not be driven solely by technical progress without consideration of social, economic, and political implications. Here are some reflections on this viewpoint:

1. **AI as a Tool, Not an Inevitability**: Treating AI as an inevitable force can lead to passivity and fatalism about its direction and effects. Instead, recognizing AI as a tool created and controlled by humans can empower society to steer its development in ways that align with broader social values and interests.

2. **Democratic Oversight**: There's growing advocacy for the democratic governance of AI, which includes establishing mechanisms through which the public can exert control over how AI is developed and deployed. This could involve more transparent AI policymaking processes and public consultations.

3. **Regulation and Legislation**: New laws and regulations could be developed to ensure that AI systems are fair, transparent, and accountable. This includes addressing issues of algorithmic bias, privacy, and the potential misuse of AI.

4. **Ethical AI Development**: Encouraging the integration of ethical considerations into AI research and development from the outset can help to mitigate potential harms. This might involve multidisciplinary teams that include ethicists and social scientists working alongside engineers and developers.

5. **Education and Awareness**: Increasing public understanding of AI technologies can help individuals better navigate and engage with these systems. This also includes education aimed at developers and users about the potential biases and limitations of AI.

6. **Economic Equity**: Addressing how AI may impact job markets and economic disparities is crucial. This could involve rethinking social safety nets and considering policies like retraining programs, universal basic income, or adjustments to education to prepare workers for a changing economy.

7. **Promoting Beneficial Uses**: Focusing AI development on areas that have clear public benefits, such as healthcare, climate change mitigation, and education, can help align its trajectory with the public interest.

By actively shaping AI's development, deployment, and governance, society can work to ensure that AI technologies are used in ways that are beneficial and do not exacerbate inequality or harm well-being. This requires collaborative effort from policymakers, technologists, civil society, and the public.

# Reflection
- As talked in piazza,(https://piazza.com/class/lldwv8sf2g57pl/post/100), the values in TabularCPD from alarm.py are not fully matching the Burglary example. But the main idea for the assignment is to work on conditions and probabilities, so I think it is fine. 




