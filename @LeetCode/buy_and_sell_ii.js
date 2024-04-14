const prices2 = [1,2,3,4,5]
const prices = [7,1,4,3,6,5]

const maxProfit = (prices) => {
  let max = 0
  let min = 0

  let profit = 0

  for ( let i = 0; i < prices.length-1; i++) {
    if ( max < prices[i] ) {
      max = prices[i]
    }
    min = Math.min(max, prices[i])

    if ( prices[i+1] > min) {
      profit += prices[i+1] - min
    }

  }
  return profit
}

console.log(maxProfit(prices))

