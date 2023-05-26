<template>
  <div>
    <div class="col">
      <router-link :to="{ name: 'MovieDetail', params: { id: movie.id } }">
        <div class="card" :class="{ 'card-hover': isHover }" @mouseover="handleMouseOver" @mouseleave="handleMouseLeave">
          <div class="card-img-container">
            <img :src="movie.poster_path" alt="" class="card-img">
          </div>
        </div>
      </router-link>
    </div>
  </div>
</template>



<script>
export default {
  props: {
    movie: {
      type: Object
    }
  },
  data() {
    return {
      isHover: false
    };
  },
  methods: {
    handleMouseOver() {
      this.isHover = true;
    },
    handleMouseLeave() {
      this.isHover = false;
    }
  }
};
</script>

<style scoped>
.card {
  width: 100%;
  height: 100%;
  transition: transform 0.3s;

}

.card-hover {
  transform: scale(1.1); 
}

/* .card-img-container {
  width: 100%;
  height: 0;
  padding-bottom: 150%; 
  position: relative;
}

.card-img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
} */
</style>
