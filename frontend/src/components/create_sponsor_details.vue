<template>
    <div>
        <div class="container mt-5">
            <div class="row justify-content-center">

            <h2>Provide your Profile Details</h2>
            <form >
                <div class="form-group mb-3">
                    <label for="ad_name">Name</label>
                    <input type="text" class="form-control" v-model="this.s_name" required>
                </div>
                <div class="form-group mb-3">
                    <label for="ad_req">Organisation</label>
                    <input type="text" class="form-control" v-model="this.s_industry" required>
                </div>
                <div class="form-group mb-3">
                    <label for="terms">Organisation Type</label>
                    <input type="text" class="form-control" v-model="this.org_name" required>
                </div>
                <div class="form-group mb-3">
                    <label for="ad_budget">Organisation Size</label>
                    <input type="number" class="form-control" v-model="this.org_size" required>
                </div>    
                <div class="form-group mb-3"> 
                <label for="ad_budget">Industry</label>
                <select class="form-select"  v-model="this.org_type">
                    <option value="Corporation">Corporation</option>
                    <option value="Non-profit">Non-profit</option>
                    <option value="Brand">Brand</option>
                    <option value="Agency">Agency</option>
                </select>
                </div>
                    <div class="mb-3"></div>
                    <button type="button" class="btn btn-primary" @click="saveProfileDetails">Save</button>
            </form>
         </div>
    </div>
    </div>
</template>
<script>
import axios from 'axios';

export default {
    
    name: 'create_sponsor_details',
  data() {
    return {
        s_name : '',
        org_name:'',
        org_type:'',
        s_industry:'',
        org_size:null,
        s_id:null
    };
  },
  methods: {
    
    saveProfileDetails() {
    axios
        .post('http://127.0.0.1:5000/api/SponsorResource', 
        {
            s_name: this.s_name,
            org_name: this.org_name,
            org_type: this.org_type,
            s_industry: this.s_industry,
            org_size: this.org_size,
            s_id:this.s_id
        })
        .then(response => {
            console.log("response block", response)
            if (response.status == 201) {
                localStorage.clear()
                this.$router.push('/')
                }
            }
        )
        .catch(error => {
            console.log("error block", error)
        })
    },
  },
  created() {
    this.s_id = this.$route.params.s_id;
  },
}
</script>
<style lang="">
    
</style>