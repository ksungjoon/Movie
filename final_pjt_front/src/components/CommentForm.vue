<template>

<div class="comment_form">
  <div class="d-flex justify-content-start flex-row mb-2 star-rating">
    <form name="myform" id="myform" method="post" action="./save">
      <fieldset>
        <input type="radio" name="rating" value="5" id="rate1" v-model="score" @change="updateScore">
        <label for="rate1">⭐</label>
        <input type="radio" name="rating" value="4" id="rate2" v-model="score" @change="updateScore">
        <label for="rate2">⭐</label>
        <input type="radio" name="rating" value="3" id="rate3" v-model="score" @change="updateScore">
        <label for="rate3">⭐</label>
        <input type="radio" name="rating" value="2" id="rate4" v-model="score" @change="updateScore">
        <label for="rate4">⭐</label>
        <input type="radio" name="rating" value="1" id="rate5" v-model="score" @change="updateScore">
        <label for="rate5">⭐</label>
      </fieldset>
    </form>
  </div>

  <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"
    v-model.trim="comment"
    @keyup.enter="createComment"
    placeholder="댓글을 작성해주세요."
  ></textarea>
</div>


</template>

<script>
import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "CommentForm",
  props: {
    movie: Object,
  },
  data() {
    return {
      comment: null,
      score: null,
    }
  },
  methods: {
    createComment() {
      const comment = this.comment;
      const score = this.score;
      if (!comment) {
        alert("내용을 입력하세요!");
        return;
      }
      axios({
        method: "post",
        url: `${API_URL}/api/v1/movies/${this.movie.id}/comments/`,
        data: {
          content: comment,
          score: score,
        },
        headers: {
          Authorization: `Token ${this.$store.state.loginStore.token}`,
        },
      })
        .then((res) => {
          console.log(res);
          this.$emit("create-comment", res);
        })
        .catch((err) => {
          console.log(err);
        });
      this.comment = null;
      this.score = null;
    },
    updateScore() {
      // 별점 변경 시 score 값을 업데이트합니다.
      this.score = document.querySelector('input[name="rating"]:checked').value;
    },
  }
}
</script>
<style scoped>
#myform fieldset{
    display: inline-block; /* 하위 별점 이미지들이 있는 영역만 자리를 차지함.*/
    border: 0; /* 필드셋 테두리 제거 */
}
#myform input[type=radio]{
    display: none; /* 라디오박스 감춤 */
}
#myform label{
    font-size: 1em; /* 이모지 크기 */
    color: transparent; /* 기존 이모지 컬러 제거 */
    text-shadow: 0 0 0 #f0f0f0; /* 새 이모지 색상 부여 */
}
#myform label:hover{
    text-shadow: 0 0 0 rgb(249, 222, 47); /* 마우스 호버 */
}
#myform label:hover ~ label{
    text-shadow: 0 0 0 rgb(249, 222, 47); /* 마우스 호버 뒤에오는 이모지들 */
}
#myform fieldset{
    display: inline-block; /* 하위 별점 이미지들이 있는 영역만 자리를 차지함.*/
    direction: rtl; /* 이모지 순서 반전 */
    border: 0; /* 필드셋 테두리 제거 */
}
#myform fieldset legend{
    text-align: left;
}
#myform input[type=radio]:checked ~ label{
    text-shadow: 0 0 0 rgb(249, 222, 47); /* 마우스 클릭 체크 */
}
.comment_form{
  width: 95%;
  margin: 0 auto;
}
.form-control{
  margin-bottom: 10px;
}
</style>