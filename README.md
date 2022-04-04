# UpdateAliyunFC
> 用于自动将仓库文件action到云函数FC


    name: test  
    on:
        workflow_dispatch:  
    jobs:
        build:
            runs-on: ubuntu-latest
    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
        - name: Run updateFC
        uses: hesgang/UpdateAliyunFC@main
        with:
          access_key_id: ${{ secrets.ACCESS_KEY_ID }}
          access_key_secret: ${{ secrets.ACCESS_KEY_SECRET }}
          account_ID: ${{ secrets.ACCOUNT_ID }}
          server_name: ${{ secrets.SERVER_NAME }}
          function_name: ${{ secrets.FUNCTION_NAME }}
          region: ${{ secrets.REGION }}