<template>
  <div>
    <div class="commentItem">
      <div class="divide">
        <div class="top">
          <div class="image_area">
            <img :src="getImageUrl" alt="프로필" class="profile">
            {{this.profile_image}}
            <div class="middle">
              <div class="stars">
                <img src="@/assets/star.png" alt="" class="star" v-for="n in comment.score" :key="n">
              </div>
              <div class="name">
                <p class="nickname" @click="navigateToProfile">{{ comment.user.username }}</p>
                <p class="date">{{ formatDate(comment.created_at) }}</p>
              </div>
            </div>
          </div>
          <div class="last">
            <a href="#" class="myButton" @click="deleteComment">삭제</a> 
          </div>
        </div>
        <div class="under">
          <p>{{ comment.content }}</p>
        </div>  
      </div>
    </div>
  </div>
</template>



<script>
import { mapGetters } from 'vuex';
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";

export default {
  name: "CommentListItem",
  data(){
    return{
      profile_img:null
    }
  },
  props: {
    comment: Object
  },
  computed: {
    ...mapGetters(['getUsername', 'profile']),
    isSameUser() {
      return this.getUsername === this.comment.user.username;
    },
    getImageUrl() {
      const defaultProfileImg = require('@/assets/default_profile.jpg');
      if (this.profile_img) {
        return `http://localhost:8000${this.profile_img}`;
      } else {
        return defaultProfileImg;
      }
    }
  },
  created(){
    this.LoadProfile(this.comment.user.username)

  },
  methods: {
    navigateToProfile() {
      const username = this.comment.user.username;
      if (this.isSameUser) {
        this.$router.push({ name: 'MyProfileView', params: { username: this.getUsername } });
      } else {
        this.$store.dispatch('fetchProfile', username)
          .then(() => {
            this.$router.push({ name: 'ProfileView', params: { username: username } });
          })
          .catch((err) => {
            console.log(err);
          });
      }
    },
    deleteComment() {
      axios({
        method: "delete",
        url: `${API_URL}/api/v1/comments/${this.comment.id}`,
        headers: {
          Authorization: `Token ${this.$store.state.loginStore.token}`,
        },
      })
        .then((res) => {
          console.log(res);
          this.$emit("delete-comment", this.comment.id);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    formatDate(dateTime) {
      const date = new Date(dateTime);
      return date.toLocaleDateString('ko-KR', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
      });
    },
    LoadProfile(username) {
      axios.get(`${API_URL}/accounts/profile/${username}/`)
        .then((res) => {
          if(res.data.profile_img)
          {
            this.profile_img = res.data.profile_img
          } 
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style scoped>
p {
  margin: 0;
}
.stars {
  display: flex;
  align-items: center;
}
.divide {
  display: flex;
  flex-direction: column;
}
.stars img {
    height:15px;
    width: 15px;
    margin: 3px;
}
.top {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.image_area {
  display: flex;
  align-items: center;
  order: 1;
}
.image_area .profile {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  margin-right: 5px;
  margin-left: 10px;
}

.last {
  order: 2; /* 오른쪽에 배치 */
}
.name {
  display: flex;
  flex-direction: row;
  align-items: center;
}

.name p {
  margin-right: 10px; /* 원하는 간격으로 설정 */
}
.nickname {
  font-size: 15px;
  font-weight: bold;
}
.date{
  font-size: 10px;
  color: rgb(233, 218, 218);
}
.under {
  text-align: left;
  margin-bottom: 10px;
}
.under p{
  font-size: 20px;
  margin-left: 10px;
}
.myButton {
	box-shadow:inset 0px 1px 0px 0px #ffffff;
	background:linear-gradient(to bottom, #ffffff 5%, #f6f6f6 100%);
	background-color:#ffffff;
	border-radius:6px;
	border:1px solid #dcdcdc;
	display:inline-block;
	cursor:pointer;
	color:#666666;
	font-family:Arial;
	font-size:10px;
	font-weight:bold;
	padding:3px 8px;
	text-decoration:none;
	text-shadow:0px 1px 0px #ffffff;
  margin-right: 10px;
}
.myButton:hover {
	background:linear-gradient(to bottom, #f6f6f6 5%, #ffffff 100%);
	background-color:#f6f6f6;
}
.myButton:active {
	position:relative;
	top:1px;
}

</style>