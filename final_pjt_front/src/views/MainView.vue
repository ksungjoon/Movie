<template>
  <div class="Main">
    <div class="container">
      <div class="genre-buttons-wrapper">
        <div class="scroll-button scroll-left-button" @click="scrollLeft" :class="{ disabled: translateX === 0 || isLeftButtonDisabled }">
          <span>&lt;</span>
        </div>
        <div class="genre-buttons-container" ref="genreContainer">
          <div class="genre-buttons" :style="{ transform: `translateX(${translateX}px)` }">
            <button class="custom-btn btn-2" :class="{ active: genreid === '0' }" @click="changeGenre('0')">전체</button>
            <button
              class="custom-btn btn-2"
              v-for="genre in genres"
              :key="genre.id"
              :class="{ active: genreid === genre.id }"
              @click="changeGenre(genre.id)"
            >
              {{ genre.name }}
            </button>
          </div>
        </div>
        <div class="scroll-button scroll-right-button" @click="scrollRight" :class="{ disabled: isMaxScrollReached }">
          <span>&gt;</span>
        </div>
      </div>
      <div class="row row-cols-1 row-cols-md-3 row-cols-lg-5 g-4">
        <MovieList v-for="movie in displayedMovies" :key="movie.id" :movie="movie" />
      </div>
      <div v-if="totalPages > 1" class="pagination-container">
        <div aria-label="Page navigation">
          <ul class="pagination justify-content-center">
            <li class="page-item" :class="{ disabled: currentPage === 1 }">
              <a class="page-link" href="#" @click="goToPage(currentPage - 1)" aria-label="Previous">
                <span aria-hidden="true">&laquo;</span>
              </a>
            </li>
            <li class="page-item" v-for="pageNumber in visiblePages" :key="pageNumber" :class="{ active: currentPage === pageNumber }">
              <a class="page-link" href="#" @click="goToPage(pageNumber)">{{ pageNumber }}</a>
            </li>
            <li class="page-item" :class="{ disabled: currentPage === totalPages }">
              <a class="page-link" href="#" @click="goToPage(currentPage + 1)" aria-label="Next">
                <span aria-hidden="true">&raquo;</span>
              </a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList.vue';

export default {
  name: 'MovieView',
  components: {
    MovieList
  },
  data() {
   return {
      genreid: '0',
      moviesPerPage: 15,
      currentPage: 1,
      translateX: 0,
      maxScrollWidth: 0,
      genreContainerWidth: 0,
      isLeftButtonDisabled: true
    };
  },
  created() {
  this.$store.dispatch('loadTotalMovies');
  this.$store.dispatch('loadTotalGenres');
  this.$nextTick(() => {
    this.genreContainerWidth = this.$refs.genreContainer.offsetWidth;
  });
},

  computed: {
    genres() {
      return this.$store.state.movieStore.genres;
    },
    filteredMovies() {
      if (this.genreid === '0') {
        return this.$store.state.movieStore.totalMovies;
      } else {
        return this.$store.state.movieStore.totalMovies.filter(movie =>
          movie.genres.some(genre => genre.id === this.genreid)
        );
      }
    },
    totalPages() {
      return Math.ceil(this.filteredMovies.length / this.moviesPerPage);
    },
    visiblePages() {
      const maxVisiblePages = 5;
      let startPage = this.currentPage - Math.floor(maxVisiblePages / 2);
      if (startPage < 1) startPage = 1;
      let endPage = startPage + maxVisiblePages - 1;
      if (endPage > this.totalPages) {
        endPage = this.totalPages;
        startPage = Math.max(endPage - maxVisiblePages + 1, 1);
      }
      return Array.from({ length: endPage - startPage + 1 }, (_, index) => startPage + index);
    },
    displayedMovies() {
      const startIndex = (this.currentPage - 1) * this.moviesPerPage;
      const endIndex = startIndex + this.moviesPerPage;
      return this.filteredMovies.slice(startIndex, endIndex);
    }
  },
  methods: {
    goToPage(pageNumber) {
      if (pageNumber >= 1 && pageNumber <= this.totalPages) {
        this.currentPage = pageNumber;
      }
    },
    changeGenre(genreId) {
      this.genreid = genreId;
      this.currentPage = 1;
    },
    isMaxScrollReached() {
      return this.translateX >= this.maxScrollWidth; // 수정
    },
    scrollLeft() {
      const translateAmount = 200;
      if (this.translateX !== 0) {
        this.translateX = Math.max(this.translateX + translateAmount, 0);
      }
    },

    scrollRight() {
  const translateAmount = 200;
  this.$nextTick(() => {
    const genreContainerWidth = this.$refs.genreContainer.clientWidth;
    const genreButtonsWidth = this.$refs.genreContainer.scrollWidth;
    this.maxScrollWidth = genreButtonsWidth - genreContainerWidth;
    if (this.translateX !== this.maxScrollWidth) {
      this.translateX = Math.min(this.translateX - translateAmount, this.maxScrollWidth);
    }
  });
  }
}
}
</script>

<style scoped>
.pagination-container {
  margin-top: 40px;
  opacity: 0.7;
}

.genre-buttons-wrapper {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
  margin-top: 50px;
  overflow: hidden;
  position: relative;
}

.scroll-button {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 30px;
  height: 30px;
  background-color: #f5f5f5;
  border-radius: 50%;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.scroll-left-button {
  margin-right: 10px;
}

.scroll-right-button {
  margin-left: 10px;
}

.scroll-button:hover {
  background-color: #e0e0e0;
}

.scroll-button span {
  font-size: 20px;
}

.genre-buttons-container {
  flex: 1;
  overflow-x: hidden;
}

.genre-buttons {
  display: flex;
  transition: transform 0.3s ease;
  white-space: nowrap;
}

.genre-buttons button {
  margin-right: 10px;
}

.genre-buttons button.active {
  font-weight: bold;
  background: linear-gradient(0deg, rgb(16, 0, 104) 0%, rgb(61, 33, 218) 100%);
}

.custom-btn {
  width: 130px;
  height: 40px;
  color: #fff;
  border-radius: 50px;
  padding: 7px 15px;
  font-family: "Jua";
  font-weight: 500;
  background: transparent;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  display: inline-block;
  box-shadow: inset 2px 2px 2px 0px rgba(255, 255, 255, .5),
    7px 7px 20px 0px rgba(0, 0, 0, .1),
    4px 4px 5px 0px rgba(0, 0, 0, .1);
  outline: none;
}

.btn-2 {
  background: rgb(116, 51, 221);
  background: linear-gradient(0deg, rgb(34, 87, 221) 0%, rgb(26, 210, 242) 100%);
  border: none;
}

.btn-2:before {
  height: 0%;
  width: 2px;
}
</style>
