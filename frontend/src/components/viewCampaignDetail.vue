<template>
<div class="container mt-5">
    <div class="row justify-content-center">
        <div v-for="(cam, index) in campaign_details" :key="index">
            <!-- Card 1 -->
            <div class="col-md-*">
                <div class="card">
                    <div class="card-header">
                        <h2>Campaign Details</h2>
                    </div>
                    <div class="card-body d-flex justify-content-between align-items-center">
                        <div class="card-body">
                            <p class="card-text"><b>Campaign Name:</b> {{ cam['cam_name'] }}</p>
                            <p class="card-text"><b>Descrption:</b> {{ cam['cam_desc'] }}</p>
                            <p class="card-text"><b>Category:</b> {{ cam['cam_category'] }}</p>
                            <p class="card-text"><b>Start Date:</b> {{ cam['cam_start_date'] }}</p>
                            <p class="card-text"><b>End Date:</b> {{ cam['cam_end_date'] }}</p>
                            <p class="card-text"><b>Budget:</b> {{ cam['cam_budget'] }}</p>
                            <p class="card-text"><b>Goals:</b> {{ cam['goals'] }}</p>
                            <p class="card-text"><b>Visibility:</b> {{ cam['visibility'] }}</p>
                            <p v-if="this.roles=='sponsor'">
                            <router-link  class="btn btn-primary" :to="{name: 'create_ad', params: {cam_id: cam['cam_id']}}">Create Ad</router-link> 
                            <router-link  class="btn btn-primary" :to="{name: 'edit_campaign', params: {cam_id: cam['cam_id']}}">Edit Campaign</router-link> 
                            <button class="btn btn-danger" @click="deleteCampaign">Delete Campaign</button> 
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
<br>

<br>
    <div class="container mt-4 mb-4">
        <h3>Ads created for the Campaign</h3>
        <br>

        <div class="row row-cols-4 row-cols-md-8 g-8 mb-4 justify-content-center">
            <div v-for="(ad, index) in ad_details" :key="index">
                <div class="card" style="height: 100%"   >
                    <div class="card-header" style="height: 75px"><b>{{ ad['ad_name'] }}</b></div>
                    <div class="card-body">
                        <p class="card-text">Ad Requirement: {{ ad['ad_req'] }}</p>
                        <p class="card-text">Ad Terms: {{ ad['terms'] }}</p>
                        <p class="card-text">Ad Budget: {{ ad['ad_budget'] }}</p>
                        <p class="card-text">Ad Status: {{ ad['status'] }}</p>
                        <p class="card-text">Preferred Influencer Category: {{ ad['pref_inf_category'] }}</p>
                        <div class="mb-6">
                            <p v-if="this.roles=='sponsor'">
                        <router-link  class="btn btn-primary" :to="{name: 'edit_ad', params: {ad_id: ad['ad_id']}}">Edit Ad Details</router-link> 
                        <button class="btn btn-danger" @click="deleteAd(ad['ad_id'])">Delete Ad</button> 
                        </p>
                        </div>

                    </div>
            </div>    
        </div>
    </div>    
    </div>



</template>
<script>
import axios from 'axios';

export default {

  name: 'viewCampaignDetails',
  data() {
    return {
      campaign_details: [],
      token: null,
      roles:[],
      id:null,
      ad_details: []
        }
  },
  methods: {

    viewCampaigns() {
        axios
        .get(`http://127.0.0.1:5000/api/CampaignSpecific/${this.id}`,
                {headers: {Authorization: `${this.token}`}})
        .then((response) => {
            console.log("response block", response)
            if (response.status == 200) {
                this.campaign_details = response.data.data
            }
            })
            .catch((error) => {
            console.error(error);
            });
        },
    viewAds() {
        axios
        .get(`http://127.0.0.1:5000/api/AdResource/${this.id}`,
        {headers: {Authorization: `${this.token}`}}
        )
        .then((response) => {
        console.log("response block", response)
        if (response.status == 200) {
            this.ad_details = response.data.data;
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
    deleteCampaign(){
        axios
        .delete(`http://127.0.0.1:5000/api/CampaignSpecific/${this.id}`,
        {headers: {Authorization: `${this.token}`}}
        )
        .then((response) => {
        console.log("response block", response)
        if (response.status == 201) {
            this.$router.push('/campaign_home')
        }
            
        })
        .catch((error) => {
            console.error(error);
        });
    },
    deleteAd(ad_id){
        axios
        .delete(`http://127.0.0.1:5000/api/AdSpecific/${ad_id}`,
        {headers: {Authorization: `${this.token}`}}
        )
        .then((response) => {
        console.log("response block", response)
        if (response.status == 201) {
            this.$router.push({
                    name: 'viewCampaignDetail', 
                    params:{cam_id: this.id}
                });
                location.reload();
            }
            
        })
        .catch((error) => {
            console.error(error);
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

            this.viewCampaigns() ;
            this.viewAds() ;

        },
}
</script>
<style lang="">
    
</style>