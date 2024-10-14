<template>
    <div>
        <div class="container mt-5">
            <div class="card">
                <div class="card-header">
                    <h2>Sponsor Profile Details</h2>
                </div>
                <div class="card-body d-flex justify-content-between align-items-center">
                    <div class="card-body">
                        <p class="card-text"><b>Name:</b> {{ this.s_name}}</p>
                        <p class="card-text"><b>Organisation:</b> {{ this.org_name }}</p>
                        <p class="card-text"><b>Organisation Type:</b> {{ this.org_type  }}</p>
                        <p class="card-text"><b>Organisation Size:</b> {{ this.org_size }}</p>
                        <p class="card-text"><b>Industry:</b> {{ this.s_industry  }}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>
<script>
import axios from 'axios';

export default {

    name: 'sponsor_profile',
  data() {
    return {
        s_name : '',
        org_name:'',
        org_type:'',
        s_industry:'',
        org_size:null,
        token: null,
        roles:[],
        userid:null,
        }
  },

  methods: {
    viewSponsorProfile() {
        axios
        .get(`http://127.0.0.1:5000/api/SponsorResource/${this.userid}`,
        {headers: {Authorization: `${this.token}`}}
        )
        .then((response) => {
        console.log("response block", response)
        if (response.status == 200) {
            this.var12 = response.data;
            this.s_name = response.data.data[0].s_name;
            this.org_name = response.data.data[0].org_name;
            this.org_type = response.data.data[0].org_type;
            this.s_industry = response.data.data[0].s_industry;
            this.org_size = response.data.data[0].org_size;

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
    
},
created() {
            this.token = localStorage.getItem('authToken');
            this.userid = localStorage.getItem('user_id');

            if (!this.token) {
                this.$router.push('/')
            }
            this.roles = localStorage.getItem('roles');
            if (this.roles=='sponsor'){
                this.userid = localStorage.getItem('user_id');
            }
            else if (this.roles =='admin'){
                this.userid = this.$route.params.id;
            }

            this.viewSponsorProfile() ;
        },
}
</script>
<style lang="">
    
</style>