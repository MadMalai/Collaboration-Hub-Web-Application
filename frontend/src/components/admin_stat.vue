<template>
    <div>
      <h3>Admin Statistics</h3>
      <br>
      <div class="container">
        <div class="row align-items-start">
          <div class="row">
            <!-- Sponsors KPI -->
            <div class="col-md-6">
              <div class="kpi-box">
                <div class="kpi-title">Sponsors</div>
                <div class="kpi-value">{{ kpi_data.spon_count }}</div>
              </div>
            </div>
            <!-- Influencers KPI -->
            <div class="col-md-6">
              <div class="kpi-box">
                <div class="kpi-title">Influencers</div>
                <div class="kpi-value">{{ kpi_data.inf_count }}</div>
              </div>
            </div>
            <!-- Campaigns KPI -->
            <div class="col-md-6">
              <div class="kpi-box">
                <div class="kpi-title">Campaigns</div>
                <div class="kpi-value">{{ kpi_data.cam_count }}</div>
              </div>
            </div>
            <!-- Advertisements KPI -->
            <div class="col-md-6">
              <div class="kpi-box">
                <div class="kpi-title">Advertisements</div>
                <div class="kpi-value">{{ kpi_data.ad_count }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>   
</template>

  <script>
  import axios from 'axios';
  import { Chart } from 'chart.js';
  
  export default {
    name: 'admin_stat',
    data() {
      return {
        kpi_data: {
          spon_count: 0,
          inf_count: 0,
          cam_count: 0,
          ad_count: 0
        },
      };
    },
    methods: {
      fetchKpiData() {
        const path = 'http://127.0.0.1:5000/api/AdminStat';
        axios
          .get(path, {
            headers: { Authorization: `${this.token}` },
          })
          .then((response) => {
            if (response.status === 200) {
              this.kpi_data = response.data.kpi_data;
            }
          })                                                                                                                          
          .catch((error) => {
            console.error(error);
          });
    },
  },
  created() {
    this.token = localStorage.getItem('authToken');
    if (!this.token) {
      this.$router.push('/');
    }
    this.fetchKpiData();
  },
  };
  </script> 
      
  <style scoped>
    .kpi-box {
    padding: 20px;
    background-color: #9669ea;
    border-radius: 8px;
    margin-bottom: 20px;
    text-align: center;
  }
  
  .kpi-title {
    font-size: 18px;
    font-weight: bold;
  }
  
  .kpi-value {
    font-size: 24px;
    font-weight: bold;
    color: #17e759;
  }
  
  .chart-container {
    margin-top: 40px;
  }
  
  canvas {
    max-width: 100%;
    height: auto;
  }
  </style>
  