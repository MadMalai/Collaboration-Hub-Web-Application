<template>
<div class="container mt-5">
    <div class="row justify-content-center">
        <!-- <div v-for="(cam, index) in campaign_details" :key="index"> -->
        <!-- Card 1 -->
            <div class="card">
                <div class="card-header">
                    <h2>Edit Campaign Details</h2>
                </div>
                <div class="card-body d-flex justify-content-between align-items-center">
                    <div class="card-body">
                        <div class="card-body">
                    <div class="form-group">
                        <label for="cam_name">Campaign Name</label>
                        <input type="text" class="form-control" v-model=this.cam_name >
                    </div>
                    <div class="form-group">
                        <label for="cam_desc">Descrption</label>
                        <input type="text" class="form-control" v-model=this.cam_desc >
                    </div>
                    <div class="form-group">
                        <label for="cam_start_date">Start Date</label>
                        <input type="date" class="form-control" v-model=this.cam_start_date >
                    </div> 
                    <div class="form-group">
                        <label for="cam_end_date">End Date</label>
                        <input type="date" class="form-control" v-model=this.cam_end_date >
                    </div>
                    <div class="form-group">
                        <label for="cam_budget">Budget</label>
                        <input type="number" class="form-control" v-model=this.cam_budget >
                    </div>
                    <div class="form-group">
                        <label for="visibility">Visibility</label>
                        <input type="text" class="form-control" v-model=this.visibility >
                    </div>
                    <div class="form-group">
                        <label for="cam_category">Campaign Category</label>
                        <input type="text" class="form-control" v-model=this.cam_category >
                    </div>
                    <div class="form-group">
                        <label for="goals">Goals</label>
                        <input type="text" class="form-control" v-model=this.goals >
                    </div>
                    <button class="btn btn-primary" @click="saveEditCampaign" >Save</button>
                    <router-link  class="btn btn-primary" :to="{name: 'viewCampaignDetail', params: {cam_id: this.cam_id}}">Cancel</router-link> 
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
    name: 'edit_campaign',
  data() {
    return {
      cam_name:'',
      cam_desc:'',
      cam_category:'',
      cam_start_date:'',
      cam_end_date:'',
      cam_budget:'',
      goals:'',
      visibility:'',
      cam_id:null,
      token: null,
      roles:[],
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
           this.var12 = response.data.data;
           this.cam_name=response.data.data[0].cam_name,
           this.cam_desc=response.data.data[0].cam_desc,
           this.cam_category=response.data.data[0].cam_category,
           this.cam_start_date=response.data.data[0].cam_start_date,
           this.cam_end_date=response.data.data[0].cam_end_date,
           this.cam_budget=response.data.data[0].cam_budget,
           this.goals=response.data.data[0].goals,
           this.visibility=response.data.data[0].visibility,
           this.cam_id=this.id
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
    saveEditCampaign(){
        axios
        .put(`http://127.0.0.1:5000/api/CampaignSpecific/${this.id}`,{

            cam_name: this.cam_name,
            cam_desc:this.cam_desc,
            cam_category:this.cam_category,
            cam_start_date:this.cam_start_date,
            cam_end_date:this.cam_end_date,
            cam_budget:this.cam_budget,
            goals:this.goals,
            visibility: this.visibility,
        },
        {headers: {Authorization: `${this.token}`}})
        .then((response) => {
        console.log("response block", response)
        if (response.status == 201) {
           this.var12 = response.data;
           this.cam_name='',
           this.cam_desc='',
           this.cam_category='',
           this.cam_start_date='',
           this.cam_end_date='',
           this.cam_budget='',
           this.goals='',
           this.visibility='',
           this.$router.push({
                    name: 'viewCampaignDetail', 
                    params:{cam_id: this.id}
                });
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
  },

    
}
</script>
<style lang="">
    
</style>