<template>
<div>
  <button @click="movieWatched" class='btn btn-success'>
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-toggles" viewBox="0 0 16 16">
      <path d="M4.5 9a3.5 3.5 0 1 0 0 7h7a3.5 3.5 0 1 0 0-7h-7zm7 6a2.5 2.5 0 1 1 0-5 2.5 2.5 0 0 1 0 5zm-7-14a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5zm2.45 0A3.49 3.49 0 0 1 8 3.5 3.49 3.49 0 0 1 6.95 6h4.55a2.5 2.5 0 0 0 0-5H6.95zM4.5 0h7a3.5 3.5 0 1 1 0 7h-7a3.5 3.5 0 1 1 0-7z"/>
    </svg>
    {{ watched ? '안봤어요!!' : '봤어요!!' }}
  </button>
</div>
  
</template>

<script>
import axios from "axios";

const API_URL = 'http://127.0.0.1:8000'

export default {
    props:{
        movie:Object,
        watched:Boolean,
    },

    methods: {
      movieWatched(){
        
        axios({
          method: 'post',
          url: `${API_URL}/api/v1/movies/${this.movie.id}/watched/`,
          data:{
            
          },
          headers: {
          Authorization: `Token ${this.$store.state.loginStore.token}`,
          },
        })
        .then((res)=>{
          console.log(res)
          this.$emit('getmoviewatched')
        })
      
        .catch((err)=>{
          console.log(err)
        })
      },
    },
};
</script>
<style scoped>
.btn {
  border-radius: 50px;

}
</style>