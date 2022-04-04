<template>
<div>
  <b-card bg-variant="white" text-variant="black" title="PCR Coverage">
    <b-card-text>
      <b-table striped hover :items="items" :fields="fields">
        <template #cell(percentage)="data">
          <span v-html="data.value"></span>
        </template>
      </b-table>
    </b-card-text>
    <b-container class="bv-example-row">
      <b-row>
        <b-col>
          <div class="overflow-auto">
            <b-pagination
                v-model="table_props.currentPage"
                :total-rows="table_props.item_count"
                :per-page="table_props.page_size"
                first-text="First"
                prev-text="Prev"
                next-text="Next"
                last-text="Last"
            ></b-pagination>
          </div>
        </b-col>
        <b-col>
          <div>
            <b-dropdown size="sm" :text="table_props.page_size.toString()" class="m-2">
              <b-dropdown-item-button @click="update_pagesize(10)">10</b-dropdown-item-button>
              <b-dropdown-item-button @click="update_pagesize(30)">30</b-dropdown-item-button>
              <b-dropdown-item-button @click="update_pagesize(50)">50</b-dropdown-item-button>
            </b-dropdown>
          </div>
        </b-col>
      </b-row>
    </b-container>
  </b-card>
</div>
</template>




<script>
import axios from 'axios'


function renameKey ( obj, oldKey, newKey ) {
  obj[newKey] = obj[oldKey];
  delete obj[oldKey];
}

export default {
  data() {
    return {
      items: [],
      fields: ['name', 'start-end', 'minimum_count', 'maximum_count', 'percentage'],
      table_props:{
        currentPage: 1,
        page_size: 10,
        item_count: 200,
      }
    }
  },
  methods: {
    async load_table(page, pagesize) {
      const req = axios.get('http://127.0.0.1:8000/PCRendpoint/' + '?page=' + page + '&pagesize=' + pagesize)
      const res = await req
      const res_data = res.data
      for (var i = 0; i < res_data.items.length; i++) {
        res_data.items[i].start = res_data.items[i].start + '-' + res_data.items[i].end
        res_data.items[i].percentage = '<progress id="file" max="100" value=' + res_data.items[i].percentage + '> 70% </progress> ' + res_data.items[i].percentage + '%'
      }
      res_data.items.forEach((item) => {
        delete item.forward_count;
        delete item.meandepth;
        delete item.primer_based_count;
        delete item.reverse_count;
        delete item.unique_gene_ids;
        delete item.chromosome;
        delete item.stdev;
        delete item.end;
        renameKey(item, 'start', 'start-end')
      })
      this.items = res_data.items
      this.item_count = res_data.pagination['total_page_count']
    },
    update_pagesize(pagesize){
      this.table_props.page_size = pagesize.toString()
    },
  },
  async mounted() {
    await this.load_table(1, 10)
  },

  watch: {
    table_props: {
      handler: async function () {
        await this.load_table(this.table_props.currentPage, this.table_props.page_size);
      },
      deep:true
    }
  }
}
</script>

<style scoped>
</style>