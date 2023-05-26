<template>
<div>
  <div class="total">
  <div class="left_area col-4">
    <img :src="getImageUrl" alt="Profile Image">
  </div>
  <div class="rigrt_area col-8">
    <div class="name">
      <h1 >{{ profile.username }}의 프로필</h1>
    </div>
    <div class="fol">
      <div class="fol-item">
        <h4>팔로워</h4>
        <h5>{{followers_count}}</h5>
      </div>
      
      <div class="fol-item">
        <h4>팔로잉</h4>
        <h5>{{followings_count}}</h5>
      </div>
      <div class="fol-item ">
    <button type="button" class="btn btn-primary" @click="followUser">
    {{ followed ? '언팔로우' : '팔로우' }}
  </button>
  </div>
  </div>
</div>
  </div>

</div>
</template>

<script>
import axios from "axios";
import { mapGetters } from 'vuex';

const API_URL = 'http://127.0.0.1:8000'

export default {
    props:{
        followed:Boolean,
        followers_count:Number,
        followings_count:Number,
    },
    computed: {
      ...mapGetters(['getUsername', 'profile']),
      getImageUrl() {
      const defaultProfileImg = require('@/assets/default_profile.jpg');
      if (this.profile && this.profile.profile_img) {
        return `http://localhost:8000${this.profile.profile_img}`;
      } else {
        return defaultProfileImg;
      }
    }
    },
    methods: {
      followUser(){
        
        axios({
          method: 'post',
          url: `${API_URL}/accounts/${this.profile.username}/follow/`,
          data:{
            
          },
          headers: {
          Authorization: `Token ${this.$store.state.loginStore.token}`,
          },
        })
        .then((res)=>{
          console.log(res)
          this.$emit('getuserlike')
        })
      
        .catch((err)=>{
          console.log(err)
        })
      },
    },
};
</script>
<style scoped>
.total {
  display: flex;
}
.left_area {
  flex: 0 0 33.33%; /* Equivalent to col-4 */
}
.left_area img{
  border-radius: 50%;
  margin-top: 30px;
  border-radius: 50%;
  width: 200px;
  height: 200px;
  object-fit: cover;
}
.rigrt_area {
  flex: 0 0 66.67%; /* Equivalent to col-8 */
  margin-left: 30px;
}
.name {
  text-align: left;
  margin-top: 50px;
  margin-bottom: 30px;
}

.fol {
  display: flex;
  align-items: center;
}

.fol-item {
  display: inline-block;
  margin-right: 20px;
}

.fol-item:last-child {
  margin-right: 0;
}

</style>