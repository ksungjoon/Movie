<template>
  <div class="container search">
    <h1>검색하신 "{{ keyword }}"에 대한 결과는 {{ search_length }}개입니다.</h1>
    <div class="row row-cols-1 row-cols-md-3 row-cols-lg-5 ">
      <MovieList
        v-for="movie in searchedMovies"
        :key="movie.id"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList.vue'
export default {
  name: 'SearchView',
  components: {
    MovieList
  },
  computed: {
    keyword() {
      return this.$route.params.keyword;
    },
    searchedMovies() {
      const movies = this.$store.state.movieStore.totalMovies
      const filteredMovies = movies.filter(movie => movie.title.includes(this.keyword))
      return filteredMovies
    },
    search_length() {
      return this.searchedMovies.length;
    }
  }
};
</script>
<style scoped>
.search {
  background-color: rgba(255, 255, 255, 0.6);
  border-radius: 5px;
  margin-top: 50px;
  margin-bottom: 50px;
  padding-bottom: 20px;
}
.search h1 {
  margin-top: 50px;
  margin-bottom: 50px;
}
</style>
