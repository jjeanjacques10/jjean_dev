const value = 2021

const realConverter = (value) => {
    let options = {
        style: 'currency',
        currency: 'BRL'
    }

    return value.toLocaleString('pt-BR', options)
}

console.log(realConverter(value)) //R$ 2.021,00