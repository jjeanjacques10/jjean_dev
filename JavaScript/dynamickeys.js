const key = 'dynamic'

const obj = {
    fixed: 'fixed value',
    [key]: 'dynamic value'
}

console.log(obj[key])
console.log(obj.fixed)