<template>
  <div class="like">
    <button class="heart-button" :class="{ active: liked }" @click="movieLike">
      <div class="heart-flip"></div>
      <span>{{ likes_count }}</span>
    </button>
  </div>
</template>

<script>
import axios from "axios";

const API_URL = 'http://127.0.0.1:8000';

export default {
  props: {
    movie: Object,
    liked: Boolean,
    likes_count: Number,
  },

  methods: {
    movieLike() {
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/movies/${this.movie.id}/like/`,
        data: {},
        headers: {
          Authorization: `Token ${this.$store.state.loginStore.token}`,
        },
      })
        .then((res) => {
          console.log(res);
          this.$emit('getmovielike');
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },

  mounted() {
    document
      .querySelectorAll(".heart, .heart-button")
      .forEach((button) =>
        button.addEventListener("click", () =>
          button.classList.toggle("active")
        )
      );
  },
};
</script>

<style scoped>
.heart,
.heart-button {
  cursor: pointer;
  outline: none;
  -webkit-appearance: none;
  -webkit-tap-highlight-color: transparent;
}
.heart-button[liked="true"] {
  --button-background: var(--background-active);
}
.heart .heart-flip,
.heart-button .heart-flip {
  --base: 32px;
  --duration: 0.6s;
  --active: #ea4673;
  --inactive: #d1d6ee;
  width: var(--base);
  height: calc(var(--base) + var(--base) / 2);
  border-radius: calc(var(--base) / 2) calc(var(--base) / 2) 0 0;
  position: relative;
  transform-origin: 50% 66.66%;
  transform-style: preserve-3d;
  transform: rotate(var(--rotate, -45deg));
  transition: background var(--duration), transform var(--duration) ease;
  background: var(--heart-background, var(--inactive));
}
.heart .heart-flip:before, .heart .heart-flip:after,
.heart-button .heart-flip:before,
.heart-button .heart-flip:after {
  content: "";
  width: calc(var(--base) / 2);
  height: var(--base);
  border-radius: var(--pseudo-border-radius, calc(var(--base) / 2) 0 0 calc(var(--base) / 2));
  position: absolute;
  left: var(--pseudo-left, -50%);
  transform-origin: var(--pseudo-origin, 100%) 50%;
  bottom: 0;
  background: var(--heart-background, var(--inactive));
  filter: brightness(var(--pseudo-filter, 50%));
  transform: translateX(1%) rotateY(var(--pseudo-rotate, 90deg)) translateZ(0);
  transition: background var(--duration), transform var(--duration) ease, filter var(--duration);
}
.heart .heart-flip:after,
.heart-button .heart-flip:after {
  --pseudo-border-radius: 0 calc(var(--base) / 2)
      calc(var(--base) / 2) 0;
  --pseudo-left: 100%;
  --pseudo-origin: 0;
  filter: brightness(var(--pseudo-filter-second, 100%));
  transform: translateX(-1%) rotateY(var(--pseudo-rotate-second, 0deg)) translateZ(0);
}
.heart.active .heart-flip,
.heart-button.active .heart-flip {
  --rotate: 45deg;
  --pseudo-filter: 100%;
  --pseudo-filter-second: 50%;
  --pseudo-rotate: 0deg;
  --pseudo-rotate-second: 90deg;
  --heart-background: var(--active);
}

.heart {
  background: none;
  border: none;
  padding: 0;
  transform: scale(var(--button-scale, 1)) translateZ(0);
  transition: transform 0.2s;
}
.heart:active {
  --button-scale: 0.95;
}

.heart-button {
  --duration: 0.4s;
  --color: #404660;
  --color-hover: #2b3044;
  --color-active: #fff;
  --border: #d1d6ee;
  --border-hover: #bbc1e1;
  --border-active: #ea4673;
  --background: #fff;
  --background-active: #ea4673;
  font-family: inherit;
  font-size: 14px;
  line-height: 1.6;
  font-weight: 600;
  padding: 6px 16px;
  border-radius: 7px;
  color: var(--button-color, var(--color));
  border: 1px solid var(--button-border, var(--border));
  background: var(--button-background, var(--background));
  transform: scale(var(--button-scale, 1)) translateZ(0);
  transition: background var(--duration), border-color var(--duration), color var(--duration), transform 0.2s;
  border-radius: 50px;
}
.heart-button .heart-flip {
  --base: 8px;
  --active: #fff;
  --inactive: #bbc1e1;
  display: inline-block;
  vertical-align: top;
  margin: 4px 6px 0 0;
}
.heart-button span {
  display: inline-block;
  vertical-align: top;
}
.heart-button > span {
  transform: translateX(var(--text-x, 4px));
  transition: transform var(--duration);
}
.heart-button > span span {
  display: inline-block;
  vertical-align: top;
  opacity: var(--span-opacity, 0);
  transform: translateX(var(--span-x, 4px));
  transition: opacity var(--duration), transform var(--duration);
}
.heart-button:active {
  --button-scale: 0.95;
}
.heart-button:hover {
  --button-color: var(--color-hover);
  --button-border: var(--border-hover);
}
.heart-button.active {
  --text-x: 0;
  --button-color: var(--color-active);
  --button-border: var(--border-active);
  --button-background: var(--background-active);
  --span-opacity: 1;
  --span-x: 0;
}

html {
  box-sizing: border-box;
  -webkit-font-smoothing: antialiased;
}

* {
  box-sizing: inherit;
}
*:before, *:after {
  box-sizing: inherit;
}

body {
  font-family: "Inter", Arial;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  background: #f6f8ff;
}

body .dribbble {
  position: fixed;
  display: block;
  right: 20px;
  bottom: 20px;
}
body .dribbble img {
  display: block;
  height: 28px;
}
body .twitter {
  position: fixed;
  display: block;
  right: 64px;
  bottom: 14px;
}
body .twitter svg {
  width: 32px;
  height: 32px;
  fill: #1da1f2;
}
</style>