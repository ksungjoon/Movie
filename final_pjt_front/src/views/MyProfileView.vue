<template>
  <div class="profile-container">
    <transition name="modal" v-if='imgmodal===true'>
      <div class="modal-mask">
        <div class="modal-wrapper">
            <div class="modal-container">
                <h5>이미지 업로드</h5>
                <img :src="getImageUrl" alt="Profile Image">
                <hr>
                    <input type="file" @change="handleFileUpload" ref="upimage">
                    <button @click="uploadImage">이미지 업로드</button>              
                <div>
                    <button @click="endImg" class="btn btn-dark mt-3">닫기</button>
                </div>
            </div>
        </div>
      </div>
    </transition>
    <div>
      <FollowModal v-if='followermodal===true' @endFollowerViewed="endFollowerViewed" :followers='followers'/>
    </div>
    <div>
      <FollowingModal v-if='followingmodal===true' @endFollowingViewed="endFollowingViewed" :followings='followings'/>
    </div>
<div class="total">
  <div class="left_area col-4 image-container">
    <img :src="getImageUrl" alt="Profile Image" @click="startImg">
  </div>
  <div class="rigrt_area col-8">
    <div class="name">
      <p>{{ getUsername }}의 프로필</p>
    </div>
    <div class="fol">
      <div class="fol-item" @click="isFollowerViewed">
        <h4>팔로워</h4>
        <h5>{{ this.followers_length }}</h5>
      </div>
      
      <div class="fol-item" @click="isFollowingViewed">
        <h4>팔로잉</h4>
         <h5>{{ this.followings_length }}</h5>
      </div>
     
    </div>
  </div>
</div>

    <div class="section-title">좋아요한 영화</div>
    <div class="row row-cols-1  row-cols-md-3 row-cols-lg-5 g-4">
      <ProfileLikeMovie
        v-for="likemovie in like_movie"
        :key="likemovie.id"
        :likemovie="likemovie"
      />
    </div>
      <p v-if="!like_movie.length" class="d-flex justify-content-center" >
        <br>
        좋아요 누른 영화가 없어요 ㅠㅠ
        <br>
      </p>
    <div class="section-title">봤던 영화</div>
    <div class="row row-cols-1  row-cols-md-3 row-cols-lg-5 g-4">
      <ProfileWatchedMovie
        v-for="watchedmovie in watched_movie"
        :key="watchedmovie.id"
        :watchedmovie="watchedmovie"
      />
    </div>
      <p v-if="!watched_movie.length"  class="d-flex justify-content-center">
        <br>
        본 영화가 없어요 ㅠㅠ
        <br>
      </p>
  </div>
</template>

<script>
import axios from 'axios'
import FollowingModal from '@/components/FollowingModal.vue'
import FollowModal from '@/components/FollowModal.vue'
// import ImgModal from '@/components/ImgModal.vue'
import ProfileLikeMovie from '@/components/ProfileLikeMovie.vue'
import ProfileWatchedMovie from '@/components/ProfileWatchedMovie.vue'
import { mapGetters } from 'vuex';
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileView',
  data() {
    return {
      followermodal:false,
      followingmodal:false,
      like_movie: null,
      watched_movie: null,
      followers_length:null,
      followings_length:null,
      followers:null,
      follwings:null,
      imageFile: null,
      profile_img: '',
      imgmodal:false,
    }
  },
  components: {
    FollowModal,
    FollowingModal,
    ProfileLikeMovie,
    ProfileWatchedMovie,
    // ImgModal
  },
  created(){
    this.likeMovieList(),
    this.watchedMovieList()
    this.fetchProfile()
  },
  computed: {
    ...mapGetters(['getUsername', 'profile']),
    getImageUrl() {
      const defaultProfileImg = require('@/assets/default_profile.jpg');
      if (this.profile && this.profile_img) {
        return `http://localhost:8000${this.profile_img}`;
      } else {
        return defaultProfileImg;
      }
    }
  },
  methods: {
    likeMovieList() {
      axios.get(`${API_URL}/accounts/profile/${this.getUsername}/`)
        .then((res) => {
          this.like_movie = res.data.like_movies;
          this.profile_img = res.data.profile_img;
        })
        .catch((err) => {
          console.log(err);
          this.like_movie = [];
        });
    },
    watchedMovieList() {
      axios.get(`${API_URL}/accounts/profile/${this.getUsername}/`)
        .then((res) => {
          this.watched_movie = res.data.watched_movies;
        })
        .catch((err) => {
          console.log(err);
          this.watched_movie = [];
        });
    },
    fetchProfile() {
      axios({
      url: `${API_URL}/accounts/profile/${this.getUsername}/`,
      method: 'get',
      headers: { Authorization: `Token ${this.$store.state.loginStore.token}` }
      })
      .then((res) => {
          console.log(res.data)
          console.log('제발')
          this.followers_length=res.data.followers.length;
          this.followings_length=res.data.followings.length;
          this.followers=res.data.followers
          this.followings=res.data.followings
      })
      .catch((err) => {
          console.log(err);
        
      });
    },
    isFollowerViewed(){
      this.followermodal=true
    },
    isFollowingViewed(){
      this.followingmodal=true
    },
    endFollowerViewed(){
      this.followermodal=false
    },
    endFollowingViewed(){
      this.followingmodal=false
    },
    startImg(){
      this.imgmodal=true
    },
    endImg(){
      this.imgmodal=false
    },
    handleFileUpload(event) {
      this.imageFile = event.target.files[0];
      console.log(this.imageFile)
    },
    uploadImage() {
      const file = this.$refs.upimage.files[0];
      console.log(file)
      const formData = new FormData();
      console.log(this.imageFile)
      formData.append('image', file);

      console.log(formData)

      axios.put(`${API_URL}/accounts/upload_img/${this.getUsername}/`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
          Authorization: `Token ${this.$store.state.loginStore.token}`,
        },
      })
      .then((res) => {
        console.log(res.data);
        console.log('확인');
        this.profile_img = res.data.profile_img
        console.log(this.profile_img)
        // 이미지 업로드 성공 후 처리
      })
      .catch((err) => {
        console.error(err);
        // 업로드 실패 시 처리
      });
    }

  }
}

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
.modal-mask {
    position: fixed;
    z-index: 9998;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: table;
    transition: opacity 0.3s ease;
    }

    .modal-wrapper {
    display: table-cell;
    vertical-align: middle;
    }

    .modal-container {
    width: 300px;
    margin: 0px auto;
    padding: 20px 30px;
    background-color: #fff;
    border-radius: 2px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
    transition: all 0.3s ease;
    font-family: Helvetica, Arial, sans-serif;
    }
  .modal-container img {
    width: 200px;
    height:200px;
  }
    .modal-header h3 {
    margin-top: 0;
    color: #42b983;
    }

    .modal-body {
    margin: 20px 0;
    }

    .modal-default-button {
    float: right;
    }
    .modal-enter {
    opacity: 0;
    }

    .modal-leave-active {
    opacity: 0;
    }

    .modal-enter .modal-container,
    .modal-leave-active .modal-container {
    -webkit-transform: scale(1.1);
    transform: scale(1.1);
    }
    .modal-body,
    .modal {
    color: #666 !important;
    }
.fol {
  display: flex;
  align-items: center;
}

.fol-item {
  margin: 0 10px;
}
.total {
  display: flex;
}

.left_area {
  margin-right: 20px;
}

.left_area img {
  margin-top: 30px;
  border-radius: 50%;
  width: 200px;
  height: 200px;
  object-fit: cover;
}
.rigrt_area {
  flex: 1;
}

.name {
  text-align: left;
  margin-top: 50px;
  margin-bottom: 20px;
}

.name p{
  font-size: 40px;
}
.modal-container img{
  border-radius: 50%;
}

</style>