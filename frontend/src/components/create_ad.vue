<template >
    <div>
        
  <div class="container mt-5">
    <h2>Create Ad</h2>
    <form >
        <div class="form-group mb-3">
            <label for="ad_name">Ad name</label>
            <input type="text" class="form-control" v-model="this.ad_name" required>
        </div>
        <div class="form-group mb-3">
            <label for="ad_req">Ad Requirement</label>
            <input type="text" class="form-control" v-model="this.ad_req" required>
        </div>
        <div class="form-group mb-3">
            <label for="terms">Terms</label>
            <input type="text" class="form-control" v-model="this.terms" required>
        </div>
        <div class="form-group mb-3">
            <label for="ad_budget">Budget</label>
            <input type="number" class="form-control" v-model="this.ad_budget" required>
        </div>    
        <div class="form-group mb-3"> 
          <input type="hidden" value="Pending"  v-model="this.status">
        </div>
        
        <div class="form-group mb-3">
            <label for="pref_inf_category">Preferred Influenecer Category</label>
            <input type="text" class="form-control" v-model="this.pref_inf_category" required>
        </div>

            <div class="mb-3"></div>
            <button type="button" class="btn btn-primary" @click="AddAdDetails">Add</button>
            <button type="button" class="btn btn-primary" @click="cancelEditAd">Cancel</button>
        </form>
</div>
</div>
</template>
<script>
import axios from 'axios';

export default {
    
    name: 'create_ad',
  data() {
    return {
        cam_id: null,
        ad_name: '',
        ad_req: '',
        terms: '',
        status: '',
        pref_inf_category: '',
        ad_budget: null
    };
  },
  methods: {
    
    AddAdDetails() {
    axios
        .post('http://127.0.0.1:5000/api/AdResource', 
        {
        cam_id: this.id,
        ad_name: this.ad_name,
        ad_req: this.ad_req,
        terms: this.terms,
        pref_inf_category: this.pref_inf_category,
        ad_budget: this.ad_budget,
        status: "pending",
        },
        {headers: {Authorization: `${this.token}`}})
        .then(response => {
            console.log("response block", response)
            if (response.status == 201) {
                this.$router.push({
                    name: 'viewCampaignDetail', 
                    params:{cam_id: this.id}
                });
            }
        })
        .catch(error => {
            console.log("error block", error)
        })
    },
    cancelEditAd(){
        this.$router.push({
                    name: 'viewCampaignDetail', 
                    params:{cam_id: this.cam_id}
                });
    }
  },
  created() {
    this.token = localStorage.getItem('authToken');
    this.id = this.$route.params.cam_id;

    if (!this.token) {
        this.$router.push('/')
    }
    this.roles = localStorage.getItem('roles');
  },
}
</script>
<style lang="">
    
</style>