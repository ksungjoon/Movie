<template>
    <div class ="container recommand">
        <br>
        <div class="title">{{ getUsername }}님을 위한 추천 영화</div>
        <br>
        <RecommandList :recommand_genre="recommand_genre"/>
       
    </div>
</template>

<script>
import axios from 'axios'
import { mapGetters } from 'vuex';
import RecommandList from '@/components/RecommandList.vue'
const API_URL = 'http://127.0.0.1:8000'

export default {
    data(){
        return{
            watched_like_movie:[],
            genre:[],
            recommand_genre:null
        }
    },
    components:{
        RecommandList
    },
    computed: {
        ...mapGetters(['getUsername', 'profile']),
    },
    created(){
        this.likeMovieList()
        // this.watchedMovieList()
        // this.loadMovies()
    },
    
    methods: {
    likeMovieList() {
      axios.get(`${API_URL}/accounts/profile/${this.getUsername}/`)
        .then((res) => {
            const likeMovies = res.data.like_movies;
            this.watched_like_movie = this.watched_like_movie.concat(likeMovies);
            this.watchedMovieList()
        })
        .catch((err) => {
          console.log(err);

        });
    },
    watchedMovieList() {
      axios.get(`${API_URL}/accounts/profile/${this.getUsername}/`)
        .then((res) => {
            const watchedMovies = res.data.watched_movies;
            this.watched_like_movie = this.watched_like_movie.concat(watchedMovies)
            this.loadMovies()
        })
        .catch((err) => {
          console.log(err);
      
        });
    },
    loadMovie(likemovie) {
      axios({
        method: "GET",
        url: `${API_URL}/api/v1/movies/${likemovie}/`
      })
        .then((res) => {
          console.log(res)
            res.data.genres.forEach((genre) => {
            this.genre.push(genre.id);
            });
        // console.log(this.genre)
        this.recommand_genre  = this.getMostFrequentGenre();
        // console.log(this.recommand_genre)
        //   this.genre.push(res.data.)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    loadMovies() {
      for (let i = 0; i < this.watched_like_movie.length; i++) {
        this.loadMovie(this.watched_like_movie[i]);
      }
    },
    getMostFrequentGenre() {
        const frequencyMap = {};
        let maxFrequency = 0;
        let mostFrequentGenre = null;

        this.genre.forEach((genre) => {
            if (frequencyMap[genre]) {
            frequencyMap[genre]++;
            } else {
            frequencyMap[genre] = 1;
            }

            if (frequencyMap[genre] > maxFrequency) {
            maxFrequency = frequencyMap[genre];
            mostFrequentGenre = genre;
            }
        });

        return mostFrequentGenre;
    },
  }
}
</script>
<style scoped>
.title{
  font-size: 40px;
  margin-top: 20px;
  color:white;
}
</style>