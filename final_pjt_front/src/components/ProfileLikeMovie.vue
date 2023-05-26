<template>
    <div>
        <div class= 'col'>
            <router-link :to="{ name: 'MovieDetail', params: { id: movie?.id } }" >
                <div class="card">
                        <img :src="movie?.poster_path" alt="" class="card-img-top">
                </div>
            </router-link>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
    data(){
        return{
            movie:null
        }
    },
    props:{
        likemovie:Number
    },
    created(){
        this.loadMovie()
    },
    methods:{
        loadMovie(){
            axios({
                method: "GET",
                url: `${API_URL}/api/v1/movies/${this.likemovie}/`
            })
            .then((res)=>{
                console.log(res)
                this.movie=res.data
                
            })
            .catch((err)=>{
                console.log(err)
            })
        }
    },

    
}
</script>