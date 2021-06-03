const inputBox = document.querySelector('input')
const searchData = document.querySelector('.search')

inputBox.addEventListener('keyup', async () => {
    query = inputBox.value
    url = `https://www.omdbapi.com/?apikey=69de4384&s=${query}`
    response = await fetch(url)
    data = await response.json()
    if (data['Response'] == 'True') 
        render_data_to_html(data['Search'])
})

function render_data_to_html(movies) {
    let output = ''
    movies.forEach((movie) => {
        output += `<a href='/movie/${movie.imdbID}'><div class='movie'><img src='${movie.Poster}' alt=''><h6>${movie.Title}</h6></div></a>`
    })
    searchData.innerHTML = output
}
