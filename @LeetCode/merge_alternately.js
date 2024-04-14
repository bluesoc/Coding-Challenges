/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {
    let l1 = word1.length
    let l2 = word2.length
    // Max iteration
    let arr_sz = (l1+l2)
    let aux = ''
    // for i, j in word1, word2
    for (let i=0; i < arr_sz; i++) {
        if ( word1[i]) {
            aux += word1[i]
        }
        if ( word2[i]) {
            aux += word2[i]
        }
    }
    return aux
};
