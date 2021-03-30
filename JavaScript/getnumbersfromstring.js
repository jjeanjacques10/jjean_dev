function getNumbers(item) {
    return item ? item.replace(/\D/g, '') : item
}

const rg = getNumbers('29.098.557-2')
const phone = getNumbers('+55 (11) 95592-1099')

console.log(`RG: ${rg}`)
console.log(`Telefone: ${phone}`)