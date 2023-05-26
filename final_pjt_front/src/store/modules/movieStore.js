
import axios from 'axios'


const API_URL = 'http://127.0.0.1:8000'

const movieStore = {
    state: {
        totalMovies: [],
        genres: []
    },
    getters: {

    },
    mutations: {
        LOAD_TOTAL_MOVIES: function (state, results) {
        state.totalMovies = results;
        },
        LOAD_TOTAL_GENRES: function (state, genres) {
            state.genres = genres;
        },
    },
    actions: {
        loadTotalMovies: function(context){
        axios({
            method:'get',
            url :`${API_URL}/api/v1/movies/`,
        })
            .then((res)=>{
            console.log(res)
            context.commit('LOAD_TOTAL_MOVIES',res.data)
            })
            .catch((error)=>{
            console.log(error)
            })
        },
        loadTotalGenres: function (context) {
            axios.get(`${API_URL}/api/v1/genres/`)
                .then((res) => {
                    context.commit('LOAD_TOTAL_GENRES', res.data);
                })
                .catch((error) => {
                    console.log(error);
                });
        }
    },
    modules: {
    }
}

export default movieStore