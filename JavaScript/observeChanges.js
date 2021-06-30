const data = {}

Object.defineProperty(data, 'pokemon', {
    set: (value) => {
        console.log(`O valor mudou para: ${value}`)
    }
})

data.pokemon = 'pikachu' // Saída: O valor mudou para pikachu
data.pokemon = 'bulbasaur' // Saída: O valor mudou para bulbasaur