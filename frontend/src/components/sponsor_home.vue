<template>

<h3> Welcome Sponsor </h3>
<br>
<br>
<br>
<div class="container-fluid">
  <h5><b>Ongoing Campaign Details</b></h5>

  <div v-for="(cam, index) in campaigns" :key="index">

  <div class="row">
      <div class="col-md-*">
            <!-- Card 1 -->
                <div class="card">
                    <div class="card-body d-flex justify-content-between align-items-center">
                        <div class="card-title"><b>Campaign {{ cam['cam_id'] }} </b> | {{ cam.cam_name }} | Progress {{ cam.progress }} %</div>
                        <router-link  class="btn btn-primary" :to="{name: 'viewCampaignDetail', params: {cam_id: cam['cam_id']}}">View</router-link> 
                    </div>
                </div>
          </div>
        </div>
      </div>
</div>
<div class="container-fluid">



  <div class="row mt-4" >
    <h4>Ad Requests sent to Influencers: </h4>

        <div v-if="this.cam_req_list.length > 0">
                <div v-for="(req, index) in cam_req_list" :key="index">
                  <div class="col-8 col-md-4"> 
                    <div class="card" style="width: 150%;" >
                          <div class="card-body">
                            <p class="card-title"> <b>Campaign :</b> {{ req.cam_name }} <br> <b>Infleuncer:</b> {{ req.i_name }} <br> <b>Profile:</b> {{ req.i_link }} <br> <b>Request Status:</b> {{ req.ad_status }} </p>
                            <!-- <router-link  class="btn btn-primary" :to="{name: 'influencer_profile_with_id', params: {id: req['i_id']}}">View</router-link>  -->
                          </div>  
                    </div>

              </div>
          </div>
        </div>
        <div v-else>
            <p>No Requests sent to influencers..</p>
        </div>
    </div>  
</div>
</template>
<script>
import axios from 'axios';

export default {
    name: 'sponsor_home',
  data() {
    return {
      campaigns: [],
      token: null,
      roles:[],
      cam_req_list:[]
        }
  },
  methods: {

  getCampaigns() {
      const path = 'http://127.0.0.1:5000/api/CampaignResource';
      axios
      .get(path,
            {headers: {Authorization: `${this.token}`}})
      .then((response) => {
        console.log("response block", response)
        if (response.status == 200) {
            this.campaigns = response.data.data;
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
      Ad_request() {
      const path = 'http://127.0.0.1:5000/api/Ad_request';
      axios
      .get(path,
            {headers: {Authorization: `${this.token}`}})
      .then((response) => {
        console.log("response block", response)
        if (response.status == 200) {
            this.cam_req_list = response.data.data;
        }
          
        })
        .catch((error) => {
          console.error(error);
        });
  },
 
    },

  created() {

    this.roles = localStorage.getItem('roles');

    this.token = localStorage.getItem('authToken');
    if (!this.token) {
        this.$router.push('/')
    }

    this.getCampaigns() ;
    this.Ad_request();
  },



}
</script>
<style lang="">
    
</style>