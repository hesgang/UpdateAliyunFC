# UpdateAliyunFC
> 用于自动将仓库文件action到云函数FC

### 示例
    name: updateFC

    # Controls when the workflow will run
    on:
      # Allows you to run this workflow manually from the Actions tab
      workflow_dispatch:

    # A workflow run is made up of one or more jobs that can run sequentially or in parallel
    jobs:
      # This workflow contains a single job called "build"
      build:
        # The type of runner that the job will run on
        runs-on: ubuntu-latest

        # Steps represent a sequence of tasks that will be executed as part of the job
        steps:
          - name: sync
            uses: hesgang/UpdateAliyunFC@main
            with:
              access_key_id: ${{ secrets.ACCESS_KEY_ID }}
              access_key_secret: ${{ secrets.ACCESS_KEY_SECRET }}
              account_ID: ${{ secrets.ACCOUNT_ID }}
              server_name: ${{ secrets.SERVER_NAME }}
              function_name: ${{ secrets.FUNCTION_NAME }}
              region: cn-beijing
              repo_name: username/reponame
              token: ${{ secrets.TOKEN }}

> public repo 请勿明文AK、SK等关键信息  
> private repo 随意

### 参考
- [hub-mirror-action](https://github.com/Yikun/hub-mirror-action) :将GitHub repo 同步到 gitee repo
