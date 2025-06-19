<template>

<br>
<br>

<div class="col-md-4 mx-auto">


    <div class="container h-100" >
        <div class="row justify-content-center">
            <h2>Login</h2>
            <br>
            <form >
                <div class="mb-3">
                <label for="username" class="form-label">Email</label>
                <input type="text" class="form-control" placeholder="email" v-model="this.email"><br>
                </div>
                <div class="mb-3">
                <label for="userpassword" class="form-label">Password</label>
                <input type="password" class="form-control" placeholder="password" v-model="this.password">
                </div>
                <div class="mb-3"></div>
                <button type="button" @click="handleLogin">Login</button>
                <div class="alert">
                <strong>{{this.message}}</strong>
                </div> 
            </form>
        </div>
    </div>
</div>

</template>
<script>
import axios from 'axios';

export default {
    
    name: 'login_view',
  data() {
    return {
      email: null,
      password:null,
      message:""
    };
  },
  methods: {
    
    handleLogin() {
    axios
        .post('http://127.0.0.1:5000/api/login', {
            email: this.email,
            password: this.password
        })
        .then(response => {
            console.log("response block", response)
            if (response.status == 201) {
                this.var12 = response.data
                this.email = null
                this.password = null
                this.roles = response.data.roles
                localStorage.setItem('authToken', response.data.authToken)
                localStorage.setItem('roles', response.data.roles)
                localStorage.setItem('user_id', response.data.user_id)
                if (this.roles == 'sponsor'){
                    this.$router.push('/sponsor_home')
                }
                else if (this.roles == 'influencer'){
                    this.$router.push('/influencer_home')
                }
                else {
                    this.$router.push('/admin_home')
                }
            }
        })
        .catch(error => {
            console.log("error block", error)
            if (error.response && error.response.status >= 400) {
                this.message=error.response.data.message
                // Refresh the page after a short delay
                setTimeout(() => {
                location.reload();
                }, 2000);
            }
        })
    }
  }
}
</script>
<style scoped>
 .container {
    display: flex;
    justify-content: center;
 }

 .alert {
      padding: 15px;
      color: rgb(246, 21, 21);
    }
</style>