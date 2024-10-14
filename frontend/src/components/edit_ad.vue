<template lang="">
    <div>
        <div class="container mt-5">
        <h2>Edit Ad Details</h2>
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
                <label for="pref_inf_category">Preferred Influenecer Category</label>
                <input type="text" class="form-control" v-model="this.pref_inf_category" required>
            </div>

                <div class="mb-3"></div>
                <button type="button" class="btn btn-primary" @click="saveEditAd">Save</button>
                <button type="button" class="btn btn-primary" @click="cancelEditAd">Cancel</button>
        </form>
    </div> 
    </div>
</template>
<script>
import axios from 'axios';

export default {
    name: 'edit_ad',
    data() {
    return {
        cam_id: null,
        ad_name: '',
        ad_req: '',
        terms: '',
        pref_inf_category: '',
        ad_budget: null
        };
    },

    methods: {
        viewSpecificAd() {
        axios
        .get(`http://127.0.0.1:5000/api/AdSpecific/${this.adid}`,
                {headers: {Authorization: `${this.token}`}})
        .then((response) => {
        console.log("response block", response)
        if (response.status == 200) {
           this.var12 = response.data.data;
           this.ad_name=response.data.data.ad_name,
           this.ad_req=response.data.data.ad_req,
           this.terms=response.data.data.terms,
           this.pref_inf_category=response.data.data.pref_inf_category,
           this.ad_budget=response.data.data.ad_budget
           this.cam_id=response.data.data.cam_id

        }
          
        })
        .catch((error) => {
          console.error(error);
        });
    },
    logoutfn(){
        localStorage.clear()
        this.$router.push('/')
    },
    saveEditAd(){
        axios
        .put(`http://127.0.0.1:5000/api/AdSpecific/${this.adid}`,{

            ad_name: this.ad_name,
            ad_req:this.ad_req,
            terms:this.terms,
            pref_inf_category:this.pref_inf_category,
            ad_budget:this.ad_budget,
        },
        {headers: {Authorization: `${this.token}`}})
        .then((response) => {
        console.log("response block", response)
        if (response.status == 201) {
           this.var12 = response.data;
           this.ad_name='',
           this.ad_req='',
           this.terms='',
           this.pref_inf_category='',
           this.ad_budget=null,
           this.$router.push({
                    name: 'viewCampaignDetail', 
                    params:{cam_id: this.cam_id}
                });
        }
          
        })
        .catch((error) => {
          console.error(error);
        });
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
            this.adid = this.$route.params.ad_id;


            if (!this.token) {
                this.$router.push('/')
            }
            this.roles = localStorage.getItem('roles');

            this.viewSpecificAd() ;

        },
}
</script>
<style lang="">
    
</style>