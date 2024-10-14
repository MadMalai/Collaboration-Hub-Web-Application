<template>
    <div>
        <div class="container mt-5">
            <div class="row justify-content-center">

            <h2>Provide your Profile Details</h2>
            <form>
                <div class="form-group mb-3">
                    <label for="ad_name">Name</label>
                    <input type="text" class="form-control" v-model="this.i_name" required>
                </div>
                <div class="form-group mb-3"> 
                    <label for="ad_budget">Platform Presence</label>
                    <select class="form-select"  v-model="this.i_presence">
                        <option value="Instagram">Instagram</option>
                        <option value="Youtube">Youtube</option>
                        <option value="Facebook">Facebook</option>
                        <option value="Twitter">Twitter</option>
                    </select>
                </div>
                <div class="form-group mb-3">
                    <label for="terms">Profile Link</label>
                    <input type="url" class="form-control" v-model="this.i_link" required>
                </div>
                <div class="form-group mb-3">
                    <label for="terms">No. of followers/Subscribers</label>
                    <input type="number" class="form-control" v-model="this.i_follow_no" required>
                </div>
                <div class="form-group mb-3">
                    <label for="ad_req">Niche</label>
                    <input type="text" class="form-control" v-model="this.i_niche" required>
                </div>

                <div class="form-group mb-3">
                    <label for="ad_budget">Experience as Influencer(in years)</label>
                    <input type="number" class="form-control" v-model="this.i_exp" required>
                </div>    
                <div class="form-group mb-3">
                    <label for="ad_req">Previous Brand Collabration</label>
                    <input type="text" class="form-control" v-model="this.prev_brand_collab" required>
                </div>
                <div class="form-group mb-3">
                    <label for="ad_req">Location</label>
                    <input type="text" class="form-control" v-model="this.i_location" required>
                </div>
                <div class="form-group mb-3">
                    <label for="ad_req">Languages Spoken</label>
                    <input type="text" class="form-control" v-model="this.i_language" required>
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
        i_name:'',
        i_presence:'',
        i_follow_no:null,
        i_niche:'',
        i_exp:null,
        i_link:'',
        prev_brand_collab:'',
        i_location:'',
        i_language:'',
        i_id : this.i_id
    };
  },
  methods: {
    
    saveProfileDetails() {
    axios
        .post('http://127.0.0.1:5000/api/InfluencerResource', 
        {
            i_name:this.i_name,
            i_presence:this.i_presence,
            i_follow_no:this.i_follow_no,
            i_niche:this.i_niche,
            i_exp:this.i_exp,
            i_link:this.i_link,
            prev_brand_collab:this.prev_brand_collab,
            i_location:this.i_location,
            i_language:this.i_language,
            i_id : this.i_id
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
    this.i_id = this.$route.params.i_id;
  },
}
</script>
<style lang="">
    
</style>