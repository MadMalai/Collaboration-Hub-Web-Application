<template>
    <div>
        <div class="container mt-5">
            <div class="card">
                <div class="card-header">
                    <h2>Create New Campaign</h2>
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
                        <select type="text" class="form-select" v-model=this.visibility >
                            <option value="Public">Public</option>
                            <option value="Private">Private</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="cam_category">Campaign Category</label>
                        <input type="text" class="form-control" v-model=this.cam_category >
                    </div>
                    <div class="form-group">
                        <label for="goals">Goals</label>
                        <input type="text" class="form-control" v-model=this.goals >
                    </div>
                    <button class="btn btn-primary" @click="create_campaign" >Save</button>
                    <button type="button" class="btn btn-primary" @click="cancelCreateCampaign">Cancel</button>
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
    name: 'create_campaign',
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
    
    create_campaign(){
        axios
        .post('http://127.0.0.1:5000/api/CampaignResource',
        {
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
           this.$router.push('/campaign_home');
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
    cancelCreateCampaign(){
        this.$router.push('/campaign_home')
    }
    
    },
    created() {
        this.token = localStorage.getItem('authToken');

        if (!this.token) {
            this.$router.push('/')
        }
        this.roles = localStorage.getItem('roles');
    },
}
</script>
<style lang="">
    
</style>