<template>
  <div>
    <h5>Influencer Statistics</h5>

    <div class="container">
      <div class="row align-items-start">
        <div class="row">
          <div class="col-md-6">
            <div class="kpi-box">
              <div class="kpi-title">Campaigns</div>
              <div class="kpi-value">{{ kpi_data.total_campaigns }}</div>
            </div>
          </div>
          <div class="col-md-6">
            <div class="kpi-box">
              <div class="kpi-title">Advertisements</div>
              <div class="kpi-value">{{ kpi_data.total_ads }}</div>
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
  name: 'influencer_stats',
  data() {
    return {
      kpi_data: {
        total_campaigns: 0,
        total_ads: 0        
      }
    };
  },
  methods: {
      fetchKpiData() {
        const path = 'http://127.0.0.1:5000/api/InfluencerStat';
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
