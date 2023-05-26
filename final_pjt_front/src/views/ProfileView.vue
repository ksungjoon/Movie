<template>

  <div class="profile-container">
    
    <div>
      <ProfileItem :followed='followed' :followers_count='followers_count' :followings_count='followings_count' @getuserlike="getUserLike"/>
    </div>
    
    <div class="section-title">좋아요한 영화</div>
    <div class="row row-cols-1  row-cols-md-3 row-cols-lg-5 g-4">
    <ProfileLikeMovie
      v-for="likemovie in like_movie"
      :key="likemovie.id"
      :likemovie="likemovie"
    />
    </div>
    <br>
    <br>
      <p v-if="!like_movie.length" class="d-flex justify-content-center">
        좋아요 누른 영화가 없어요 ㅠㅠ
      </p>
    <br>
    <br>
    <div class="section-title">봤던 영화</div>
    <div class="row row-cols-1  row-cols-md-3 row-cols-lg-5 g-4">
    <ProfileWatchedMovie
      v-for="watchedmovie in watched_movie"
      :key="watchedmovie.id"
      :watchedmovie="watchedmovie"
    />
    </div>
    <br>
    <br>
      <p v-if="!watched_movie.length"  class="d-flex justify-content-center">
        본 영화가 없어요 ㅠㅠ
      </p>
    <br>
    <br>
  </div>
</template>

<script>
import axios from 'axios'
import ProfileItem from '@/components/ProfileItem.vue'
import ProfileLikeMovie from '@/components/ProfileLikeMovie.vue'
import ProfileWatchedMovie from '@/components/ProfileWatchedMovie.vue'
import { mapGetters } from 'vuex';
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileView',
  data() {
    return {
      like_movie: null,
      watched_movie: null,
      followed:false,
      followers_count: 0,
      followings_count: 0,
    }
  },
  components: {
    ProfileItem,
    ProfileLikeMovie,
    ProfileWatchedMovie
  },
  created(){
    this.likeMovieList(),
    this.watchedMovieList()
    this.getUserLike()
  },
  computed: {
    ...mapGetters(['getUsername', 'profile']),
  },
  methods: {
    likeMovieList() {
      axios.get(`${API_URL}/accounts/profile/${this.profile.username}/`)
        .then((res) => {
          this.like_movie = res.data.like_movies;
        })
        .catch((err) => {
          console.log(err);
          this.like_movie = [];
        });
    },
    watchedMovieList() {
      axios.get(`${API_URL}/accounts/profile/${this.profile.username}/`)
        .then((res) => {
          this.watched_movie = res.data.watched_movies;
        })
        .catch((err) => {
          console.log(err);
          this.watched_movie = [];
        });
    },
    getUserLike(){
      axios({
        method:'get',
        url:`${API_URL}/accounts/${ this.profile.username}/followcount/`,
        headers: {
              Authorization: `Token ${this.$store.state.loginStore.token}`,
          },
      })
      .then((res)=>{
  
  
        this.followed = res.data.followed
        this.followers_count= res.data.followers_count
        this.followings_count= res.data.followings_count
      })
      .catch((err)=>{
        console.log(err)
      })
      },
  }
};
</script>

<style scoped>
.profile-container {
  width: 80%;
  margin: 50px auto;
  padding: 20px;
  background-color: rgba(255, 255, 255, 0.6);
  border-radius: 5px;
}

h1 {
  font-size: 24px;
  margin-bottom: 20px;
  text-align: center;
}

.section-title {
  font-size: 20px;
  font-weight: bold;
  margin: 20px 0;
}

/* Customize ProfileItem component styles */
/* Example styles */
.profile-item {
  background-color: #f5f5f5;
  padding: 10px;
  border-radius: 5px;
  margin-bottom: 20px;
}

.profile-item h2 {
  font-size: 18px;
  margin-bottom: 10px;
}

.profile-item p {
  font-size: 14px;
  color: #666;
}

/* Customize ProfileLikeMovie component styles */
/* Example styles */
.profile-like-movie {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.profile-like-movie img {
  width: 100px;
  height: 150px;
  object-fit: cover;
  margin-right: 10px;
}

.profile-like-movie h3 {
  font-size: 16px;
}

/* Customize ProfileWatchedMovie component styles */
/* Example styles */
.profile-watched-movie {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.profile-watched-movie img {
  width: 100px;
  height: 150px;
  object-fit: cover;
  margin-right: 10px;
}

.profile-watched-movie h3 {
  font-size: 16px;
}

</style>