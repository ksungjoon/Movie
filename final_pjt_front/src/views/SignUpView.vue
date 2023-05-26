<template>
  <div>
    <section>
      <div class="container">
        <div class="background-img">
          <div class="box">
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <div class="content">
              <h1>SignUp</h1>
              <form @submit.prevent="signUp">
                <label for="username">username</label>
                <input type="text" id="username" v-model="username" class="transparent-input"><br>

                <label for="password1">password</label>
                <input type="password" id="password1" v-model="password1" class="transparent-input"><br>

                <label for="password2">password confirmation</label>
                <input type="password" id="password2" v-model="password2" class="transparent-input">
                
                <button type="submit" class="signupbutton">SignUp</button>
              </form>
            </div>  
          </div>
        </div>
      </div>
    </section>
    
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    signUp() {
      // console.log('signup')
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username, password1, password2
      }

      this.$store.dispatch('signUp', payload)

    }
  }
}
</script>
<style scoped>
.container{  padding-top: 20px;
  padding-bottom: 20px;}
body{
  background-color: #111845;
}

.content h1{ 
  margin-bottom: 30px;
}

.box{
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 500px;
  height: 500px;
  background: #111845a6;
  box-sizing: border-box;
  overflow: hidden;
  box-shadow: 0 20px 50px rgb(23, 32, 90);
  border: 2px solid #2a3cad;
  color: white;
  padding: 20px;
}

.box:before{
  content: '';
  position:absolute;
  top:0;
  left:-100%;
  width:100%;
  height:100%;
  background: rgba(255,255,255,0.1);
  transition:0.5s;
  pointer-events: none;
}

.box:hover:before{
  left:-50%;
  transform: skewX(-5deg);
}


.box .content{
  position:absolute;
  top: 50%;
  left: 50%;
  border:1px solid #f0a591;
  padding: 50px 130px;
  transform: translate(-50%, -50%);
  text-align: center;
  box-shadow: 0 5px 10px rgba(9,0,0,0.5);
  
}

.box span{
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: block;
  box-sizing: border-box;
  
}

.box span:nth-child(1)
{
  transform:rotate(0deg);
}

.box span:nth-child(2)
{
  transform:rotate(90deg);
}

.box span:nth-child(3)
{
  transform:rotate(180deg);
}

.box span:nth-child(4)
{
  transform:rotate(270deg);
}

.box span:before
{
  content: '';
  position: absolute;
  width:100%;
  height: 2px;
  background: #50dfdb;
  animation: animate 4s linear infinite;
}

@keyframes animate {
  0% {
  transform:scaleX(0);
  transform-origin: left;
  }
  50%
  {
    transform:scaleX(1);
  transform-origin: left;
  }
  50.1%
  {
    transform:scaleX(1);
  transform-origin: right;
    
  }
  
  100%
  {
    transform:scaleX(0);
  transform-origin: right;
    
  }
}
button.signupbutton {
border: 1px solid #31c9f4;
background-color: transparent;
padding: 5px 10px;
cursor: pointer;
font-size: 15px;
color: #31c9f4;
border-radius: 5px;
margin-top: 5px;
}
input.transparent-input {
  background-color: rgba(255, 255, 255, 0.6);
  border: none;
  padding: 5px;
  font-size: 14px;
  color: #000;
  border-radius: 5px;
  margin: 5px auto 15px;
} 
</style>