You call 2 Ubers and 3 Lyfts. If the time that each takes to reach you are independent and identical distributions, what is the probability that all the Lyfts arrive first? What is the probability that all the Ubers arrive first?

5!/(5-3)! (permutation without repitition formula) choices out of which 6 (3*2*1 chocies for places) are correct so 10%


Consider a group of 20 people. If everyone shakes hands with everyone else, how many handshakes take place?

20*19/2 = 190
20 people, 19 handshakes per, /2 to count each handshake once instead of for both people


A worker has asked her supervisor for a letter of recommendation for a new job. She estimates that there is an 80 percent chance that she will get the job if she receives a strong recommendation, a 40 percent chance if she receives a moderately good recommendation, and a 10 percent chance if she receives a weak recommendation. She further estimates that the probabilities that the recommendation will be strong, moderate, and weak are .7, .2, and .1, respectively.

(Conditional Probability)

(a) How certain is she that she will receive the new job offer?

P = weighted average = .8*.7 +.4*.2 +.1*.1 = .65

(b) Given that she does receive the offer, how likely should she feel that she received a strong recommendation? a moderate recommendation? a weak recommendation?

p(strong rec|job offer) = p(job offer|strong)* P(strong rec) / p(Job offer)
strong = .8*.7/.65 = .86
moderate = .4*.2/.65 = .12
weak = .1*.1/.65 = .02


(c) Given that she does not receive the job offer, how likely should she feel that she received a strong recommendation? a moderate recommendation? a weak recommendation?

p(strong rec|decline) = p(decline|strong)* P(strong rec) / p(decline)
strong = .2*.7/.35 = .4
moderate = .6*.2/.35 = .34
weak = .9 * .1 / .35 = .26


A simplified model for the movement of the price of a stock supposes that on each day the stock’s price either moves up 1 unit with probability p or moves down 1 unit with probability 1 − p. The changes on different days are assumed to be independent.

(Conditional Probability)

(a) What is the probability that after 2 days the stock will be at its original price?

four possibilities UU,UD,DD,DU => 50%

(b) What is the probability that after 3 days the stock’s price will have increased by 1 unit?

UUU,UUD,UDU,UDD,DDD,DDU,DUD,DUU (2^3 total choices)
same as saying have 1 D total 3 ways to do that, so 3/8, could have realized that before typing all the combinations out

(c) Given that after 3 days the stock’s price has increased by 1 unit, what is the probability that it went up on the first day?

given that its one of those 3 possibilities, 2 will have it on the first day, so 2/3.

A salesman has scheduled two appointments to sell encyclopedias. His first appointment will lead to a sale with probability .3, and his second will lead independently to a sale with probability .6. Any sale made is equally likely to be either for the deluxe model, which costs $1000, or the standard model, which costs $500. Determine the probability mass function of X, the total dollar value of all sales.

(Random Variable - PMF)

Range = [0,500,1000,1500,2000]
F(X) such that:
first option has probability .7*.4 = .28
2nd = .3*.5*.4 +.7*.6*.5 = .27
3rd = .3*.5*.4 + .7*.6*.5 +.3*.5*.6*.5 = .315
4th = .3*.5*.6*.5*2 =.09
5th = .3*.5*.6*.5 = .045
These all total to 1

A gambling book recommends the following “winning strategy” for the game of roulette: Bet $1 on red. If red appears (which has probability 18/38), then take the $1 profit and quit. If red does not appear and you lose this bet (which has probability 20/38 of occurring), make additional $1 bets of red on each of the next two spins of the roulette wheel and then quit. Let X denote your winnings when you quit.

(Random Variable - Expected Value)

(a) Find P(X > 0).

Possible outcomes: [-3,-1,1,1 (other way)]
prob -3 = 20/38*20/38*20/38 = 1000/6859
prob -1 = 20/38*18/38*20/38*2 = 1800/6859
Prob 1 = 18/38 = 18/38 = 
Prob 3 = 20/38*18/38^2 = 810/6859

(b) Find E[X].
-.1


(c) Are you convinced that the strategy is indeed a “winning” strategy?

A negative expected outcome is certainly a bad strategy.

The number of times that a person contracts a cold in a given year is a Poisson random variable with parameter λ = 5. Suppose that a new wonder drug (based on large quantities of vitamin C) has just been marketed that reduces the Poisson parameter to λ = 3 for 75 percent of the population. For the other 25 percent of the population, the drug has no appreciable effect on colds. If an individual tries the drug for a year and has 2 colds in that time, how likely is it that the drug is beneficial for him or her?

(Random Variable - Poisson + Conditional Probability)

if part of 75% P(2)=exp(-3)*3^2/2! = 22.4%
if part of 25% P(2)=exp(-5)*5^2/2! = 8.4%
P(Beneficial|2 colds) = P(Beneficial)*P(2 colds|Beneficial)/P(2 colds)
=.75* .224/.084 = 2 somehow i messed up but I think the right method

Suppose that X is a normal random variable with mean 5. If P(X > 9) = .2, approximately what is Var(X )? Use the normal distribution function table. 

(Random Variable - Normal + CDF)

Var x = sigma^2
Z = (X-5)/sigma
Var(X) = ((X-5)/Z)^2

The forecast says that in the next five days the chance of rain for each day is 25%. Suppose that the weather on each day does not depend on the weather on the other days. What is the probability that it will rain for at least two days in the next five days? For how many days on average will it rain in the next five days?

(Random Variable - Binomial)

(5choose2)*.25^2(.75)^3 = 26.4%
mean = 5*.25 = 1.25 days or on average 1 day

The number of years a radio functions is exponentially distributed with parameter λ = 1 / 8 . If Jones buys a used radio, what is the probability that it will be working after an additional 8 years?

(Random Variable - Exponential)

1/8exp(-1/8*8) = 4.6%