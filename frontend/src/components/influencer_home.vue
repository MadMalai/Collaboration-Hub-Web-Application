<template>
    <h3> Welcome Influencer! </h3>
    <br>
    <br>
    <h4> Active Campaigns </h4>
    <br>
    <div class="container-fluid">
      <div class="row">
        <div v-if="this.cam_list.length > 0">
            <div v-for="(cam, index) in cam_list" :key="index">
            <!-- Card 1 -->
                <div class="col">
                    <div class="card">
                        <div class="card-body d-flex justify-content-between align-items-center">
                            <div class="card-title"><b>Sponsor</b> {{ cam['org_name'] }} | <b>Campaign</b> {{ cam['cam_name'] }} | <b>Ad Name</b> {{ cam['ad_name'] }} | <b>Proress</b>  {{ cam['progress'] }} %</div>
                            <router-link  class="btn btn-primary" :to="{name: 'viewCampaignDetail', params: {cam_id: cam['cam_id']}}">View</router-link> 
                            </div>
                    </div>
                </div>
            </div>
        </div>
        <div v-else>
            <p>No Campaigns active. Please accept Ad to view Camapign details here..</p>
        </div>
          <div>
          </div>
      </div>

      <div class="row mt-4" >
        <h4> New Ad Requests recevied from Sponsors </h4>

        <div class="row mt-4" v-if="this.cam_list.length > 0">
                <div v-for="(cam, index) in cam_req_list" :key="index">
                  <div class="col-8 col-md-4"> 
                    <div class="card" style="width: 100%;" >
                      <div class="card-header"><b>{{ cam.ad_name }}</b></div>
                          <div class="card-body">
                            <p class="card-text"> <b>Campaign :</b> {{ cam.cam_name }} <br> <b>Ad Requirement:</b> {{ cam.ad_req }} <br> <b>Goals:</b> {{ cam.goals }} <br> <b>Sponsor Name:</b> {{ cam.org_name }} </p>
                            <router-link  class="btn btn-primary" :to="{name: 'viewCampaignDetail', params: {cam_id: cam['cam_id']}}">View</router-link> 
                            <button type="button" class="btn btn-primary" @click="updateRequestStatus({reaction:1,r_id:cam.r_id})">Accept</button>
                            <button type="button" class="btn btn-primary" @click="updateRequestStatus({reaction:2,r_id:cam.r_id})">Negotiate</button>
                            <button type="button" class="btn btn-danger" @click="updateRequestStatus({reaction:3,r_id:cam.r_id})">Reject</button>
                          </div>  
                    </div>

              </div>
          </div>
        </div>
        <div v-else>
            <p>No Pendng Requests from Sponsors..</p>
        </div>
      </div>  

    </div>
</template>
<script>
import axios from 'axios';

export default {
    data() {
    return {
      roles:'',
      cam_list: [],
      cam_req_list:[],
      token: null,
      userid:this.userid,
      reaction:null,
      r_id:null,
      req:null

    }
  },
  methods:{
    getCampaigns() {
      axios
      .get(`http://127.0.0.1:5000/api/CampaignInfluencerSpecific/${this.userid}`,
            {headers: {Authorization: `${this.token}`}})
      .then((response) => {
        console.log("response block", response)
        if (response.status == 200) {
            this.cam_list = response.data.data;
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
    getCampaignsRequests() {
    axios
    .get(`http://127.0.0.1:5000/api/Ad_request`,
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
    updateRequestStatus(id) {
    axios
        .put('http://127.0.0.1:5000/api/Inf_ad_req_decision', 
       id,{headers: {Authorization: `${this.token}`}})
        .then(response => {
            console.log("response block", response)
            if (response.status == 201) {
                this.getCampaignsRequests()

                }
            }
        )
        .catch(error => {
            console.log("error block", error)
        })
    },
    },

  created() {
    this.roles = localStorage.getItem('roles');
    this.userid = localStorage.getItem('user_id');
    this.token = localStorage.getItem('authToken');

    if (!this.token) {
        this.$router.push('/')
    }

    this.getCampaigns();
    this.getCampaignsRequests()
},
}
</script>
<style lang="">
    
</style>