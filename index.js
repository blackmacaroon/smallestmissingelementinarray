function smallest_missing(array){
    let smallest = 0
    if(array.length){
        for(let i = 0; i < array.length; i++){
            if(array[i] != i){
            smallest = i
            return smallest
            } else {
                smallest = i + 1
            }
        }
    }
    return smallest
}

console.log(smallest_missing([1, 2, 3, 6]))
console.log(smallest_missing([]))
console.log(smallest_missing([0, 1, 2, 3, 5]))