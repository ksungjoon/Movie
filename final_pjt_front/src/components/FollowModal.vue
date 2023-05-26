<template>
  <transition name="modal">
      <div class="modal-mask">
      <div class="modal-wrapper">
          <div class="modal-container">
              <h5>팔로워</h5>
              <hr>
              <br>
              <div v-for="(follower, index) in followers" :key="index" @click="navigateToProfile(followers_name[index])">
                <div>{{ followers_name[index] }}</div>
                <br>
              </div>
              <div>
                  <button @click="$emit('endFollowerViewed')" class="btn btn-dark mt-3">닫기</button>
              </div>
          </div>
      </div>
      </div>
  </transition>
</template>

<script>
import { mapGetters } from 'vuex';
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";

export default {
  data() {
    return {
      followers_name: []
    };
  },
  computed: {
    ...mapGetters(['getUsername']),
  },
  props:{
    followers:Array
  },
  created() {
    this.loadNames();
  },
  methods: {
    loadNames() {
      const requests = this.followers.map((follower) =>
        axios
          .get(`${API_URL}/accounts/profile/id/${follower}`)
          .then((res) => res.data.username)
          .catch((err) => console.log(err))
      );

      Promise.all(requests)
        .then((names) => {
          this.followers_name = names;
        })
        .catch((err) => console.log(err));
    },
    navigateToProfile(username) {
      if (this.getUsername === username) {
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
  }
};
</script>

<style>
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
</style>

