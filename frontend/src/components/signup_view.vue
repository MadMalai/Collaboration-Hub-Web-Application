<template>
    <div>
        <div class="container mt-5">
            <div class="row justify-content-center">

            <h2>Signup</h2>
            <form >
                <div class="form-group mb-3">
                    <label for="ad_req">Email</label>
                    <input type="text" class="form-control" v-model="this.email" required>
                </div>
                <div class="form-group mb-3">
                    <label for="terms">Password</label>
                    <input type="text" class="form-control" v-model="this.password" required>
                </div>
                <div class="form-group mb-3">
                    <label for="ad_budget">Role</label>
                    <select class="form-select" v-model="this.role" required>
                    <option value="influencer">Influencer</option>
                    <option value="sponsor">Sponsor</option>
                    </select>
                </div>    
                <div class="mb-3"></div>
                <button type="button" class="btn btn-primary" @click="signup">Signup</button>
                </form>
        </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios';

export default {
  name: 'signup_view',
  data() {
    return {
        email: '',
        password: '',
        role: ''
    };
  },
  methods: {
    
    signup() {
    axios
        .post('http://127.0.0.1:5000/api/signup', 
        {
            email: this.email,
            password: this.password,
            role: this.role
        })
        .then(response => {
            console.log("response block", response)
            if (response.status == 200) {
                this.var12 = response.data
                if (this.role == 'sponsor'){
                    this.$router.push({
                    name: 'create_sponsor_details', 
                    params:{s_id: response.data.id}
                })
            }
                else if (this.role == 'influencer'){
                    this.$router.push({
                    name: 'create_influencer_details', 
                    params:{i_id: response.data.id}
                }) 
            }

            }
        })
        .catch(error => {
            console.log("error block", error)
        })
        },
    },
}
</script>
<style lang="">
    
</style>