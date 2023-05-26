<template>
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container">
          <h5>팔로잉</h5>
          <hr>
          <br>
          <div v-for="(following, index) in followings" :key="index" @click="navigateToProfile(followings_name[index])">
            <div>{{ followings_name[index] }}</div>
            <br>
          </div>
          <div>
            <button @click="$emit('endFollowingViewed')" class="btn btn-dark mt-3">닫기</button>
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
      followings_name: []
    };
  },
  computed: {
    ...mapGetters(['getUsername']),
  },
  props: {
    followings: Array
  },
  created() {
    this.loadNames();
  },
  methods: {
    loadNames() {
      const requests = this.followings.map((following) =>
        axios
          .get(`${API_URL}/accounts/profile/id/${following}`)
          .then((res) => res.data.username)
          .catch((err) => console.log(err))
      );

      Promise.all(requests)
        .then((names) => {
          this.followings_name = names;
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
