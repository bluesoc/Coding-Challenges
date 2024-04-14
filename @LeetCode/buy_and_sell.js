let prices = [7,6,4,3,1]

const maxProfit = (prices) => {
  let profit = 0;
  let buy = Number.MAX_SAFE_INTEGER
  let sell = 0

  for (let i = 0; i < prices.length; i++) {
    if (prices[i] < buy) {
      buy = prices[i]
    }
    if ( prices[i] > sell )
    {
      let new_profit = prices[i] - buy
      if ( new_profit > profit){
        profit = new_profit
      }
    }
  }
  return profit
};

profit = maxProfit(prices);
console.log(profit);
