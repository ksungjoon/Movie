<template>
    <div class="container detail">
        <div class="row">
            <div class="col-md-4">
                <div class="image-box">
                <img :src="movie?.poster_path" class="rounded image-thumbnail" alt="">
                </div>
                <div v-if="isLogin" class="loginarea">
        
                    <MovieLike :movie='movie' :likes_count='likes_count' :liked='liked' @getmovielike="getMovieLike"/>
                    <MovieWatched :movie='movie' :watched='watched' @getmoviewatched="getMovieWatched"/> 
                    
                </div>
            </div>
            <div class="col-md-8 content">
                <div>
                <h1>{{ movie?.title }}</h1>
                <button v-for="genre in movie.genres" :key="genre.id" class="w-btn w-btn-indigo">
                    <span>{{ genre.name }}</span>
                </button>
                <div class="four">
                <p><img src="@/assets/star.png" alt="" class='star'>{{ movie?.vote_average }}</p>
                </div>
                
                <p>{{ movie?.overview }}</p>
                </div>
                <div class="comment">
                    <p>Comments</p>
                <CommentList :movie="movie" :comments='comments'/>
                <CommentForm @create-comment="createComment" :movie="movie"/>
                </div>
            </div>
        </div>
        
        <!-- {{liked}} {{likes_count}}
        {{watched}} -->
    </div>
</template>

<script>
import axios from 'axios'
import CommentForm from '@/components/CommentForm'
import CommentList from '@/components/CommentList'
import MovieLike from '@/components/MovieLike'
import MovieWatched from '@/components/MovieWatched'
import { mapGetters } from 'vuex';

const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'MovieDetail',
    components:{
        CommentForm,
        CommentList,
        MovieLike,
        MovieWatched

    },
    data() {
        return {
        movie: null,
        comments:[],
        likes_count:0,
        liked:false,
        watched:false,
        }
    },
    created() {
        this.getMovieDetail()
    },
    computed: {
    ...mapGetters(['isLogin', 'getUsername']),
    },

    methods: {
        getComments() {
        axios({
            method: "get",
            url: `${API_URL}/api/v1/comments/list/${this.movie.id}/`,
        }).then((res) => {
            this.comments = res.data;
            console.log(this.comments);
        })
        .catch((err)=>{
            console.log(err);
            this.comments = []
        });
        },
        getMovieDetail() {
        axios({
            method: 'get',
            url: `${API_URL}/api/v1/movies/${ this.$route.params.id }/`,
        })
        .then((res) => {
            console.log(res)
            this.movie = res.data
            this.getComments();
            this.getMovieLike()
            this.getMovieWatched()
        })
        .catch((err) => {
            console.log(err)
        })
        },
        createComment(res){
            this.comments.push(res.data)
        },

        getMovieLike(){
        axios({
          method:'get',
          url:`${API_URL}/api/v1/movies/${ this.movie.id}/like/count`,
          headers: {
                Authorization: `Token ${this.$store.state.loginStore.token}`,
            },
        })
        .then((res)=>{
        //   console.log(res)
          this.likes_count = res.data.likes_count
          this.liked = res.data.liked
        })
        .catch((err)=>{
          console.log(err)
        })
        },
        getMovieWatched(){
        axios({
          method:'get',
          url:`${API_URL}/api/v1/movies/${ this.movie.id}/watched/count`,
          headers: {
                Authorization: `Token ${this.$store.state.loginStore.token}`,
            },
        })
        .then((res)=>{
          console.log(res)
          this.watched = res.data.watched
        })
        .catch((err)=>{
          console.log(err)
        })
      }

    }
}
</script>
<style scoped>
.detail {
    background-color: rgba(255, 255, 255, 0.6);
  border-radius: 5px;
  margin-top: 50px;
  margin-bottom: 50px;
  padding-right: 30px;
}
.image-thumbnail {
    width:90%;
    height:90%;
    object-fit:cover;
    margin-top: 30px;

}
.star {
    height:25px;
    width: 25px;
    margin-right: 10px;
    margin-bottom: 5px;
}
.content{
    margin-top: 40px;
}
.four {
  text-align: right;
}
.loginarea{
   display: flex;
    flex-direction: row;
    justify-content: center; /* 가로 중앙 정렬 */
    align-items: center;
    
}
.loginarea > *{
    margin: 20px 20px;
    
}

.w-btn {
    position: relative;
    border: none;
    display: inline-block;
    padding: 5px 10px;
    border-radius: 15px;
    font-family: "paybooc-Light", sans-serif;
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
    text-decoration: none;
    font-weight: 600;
    transition: 0.25s;
    margin: 0 5px;
}
.w-btn-indigo {
    background-color: aliceblue;
    color: #1e6b7b;
}

.comment{
    width: 100%;
    background-color: rgba(143, 135, 135, 0.5); 
    border-radius: 5px;
    padding-bottom: 5px;
}

.comment p{
    font-size: 30px;
    margin-left: 10px; /* 기본 왼쪽 여백 제거 */
    text-align: left;

}
</style>