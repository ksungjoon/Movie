
import axios from 'axios'
import router from '@/router'

const API_URL = 'http://127.0.0.1:8000'

const loginStore ={
    state: {
        token:null,
        username:null,
        profile: {},
    },
    getters: {
        isLogin(state) {
        return state.token ? true : false
        },
        getUsername(state) {
            return state.username;
          },
        profile (state) {
            return state.profile
        },
    },
    mutations: {
        SAVE_TOKEN(state, { token, username }) {
        state.token = token
        state.username = username
        router.push({name : 'MovieView'}) 
        },
        
        CLEAR_TOKEN(state) {
        state.token = null
        state.username = null
        router.push({ name: 'LogInView' }) 
        },
        SET_PROFILE (state, profile) {
            state.profile = profile
            console.log('hello')
            console.log(profile)
        },
        SET_PROFILE_IMG: (state, profile_img) => state.profile.profile_img = profile_img,
    },
    actions: {
        signUp(context, payload) {
        const username = payload.username
        const password1 = payload.password1
        const password2 = payload.password2

        axios({
            method: 'post',
            url: `${API_URL}/accounts/signup/`,
            data: {
            username, password1, password2
            }
        })
            .then((res) => {
            context.commit('SAVE_TOKEN', { token: res.data.key, username: payload.username })
            })
            .catch((err) => {
            console.log(err)
        })
        },
        login(context, payload) {
        const username = payload.username
        const password = payload.password

            axios({
                method: 'post',
                url: `${API_URL}/accounts/login/`,
                data: {
                username, password
                }
            })
                .then((res) => {
                context.commit('SAVE_TOKEN', { token: res.data.key, username: payload.username })
                })
            .catch((err) => console.log(err))
        },
        logout(context) {
            // 로그아웃 처리 로직
            axios({
                method: 'post',
                url: `${API_URL}/accounts/logout/`,
                headers: {
                Authorization: `Token ${context.state.token}`
                }
            })
                .then(() => {
                context.commit('CLEAR_TOKEN')
                })
                .catch((err) => {
                console.log(err)
                })
        },
        fetchProfile(context, username) {
            return new Promise((resolve, reject) => {
        axios({
        url: `${API_URL}/accounts/profile/${username}/`,
        method: 'get',
        headers: { Authorization: `Token ${context.state.token}` }
        })
        .then(res => {
            context.commit('SET_PROFILE', res.data);
            resolve(); // 업데이트 완료를 알리는 Promise를 resolve
        })
        .catch(err => {
            console.log(err);
            reject(err); // 에러가 발생한 경우에도 reject
        });
    });
},

        
    },
    modules: {
    }
}

export default loginStore
