##########
# Edge Function生成&確認用のシェル
# @description
#        XXDeploy - 関数生成
#        POSTXX - リクエストテスト
##########

# chmod 755 ./supabase/deno.sh で実行できるようにする
# Invalid JWTエラーになる場合、echo "ANNON_KEY: ${ANNON_KEY}"で中身が出力されているか確認
export $(cat ./supabase/.env | grep -v ^# | xargs);

# function denoBuild() {
#   deno run --allow-env --env-file ./supabase/.env --allow-net --allow-read --config=./deno.jsonc \
#         --import-map=./functions/import_map.json ./functions/$2/index.ts
# }

# deploy hello-world
function helloWorldDeploy() {
  supabase functions deploy hello-world --project-ref ajytzagixhcjqcrfunjt
}

function postHelloWorld() {
  curl -L -X POST 'https://ajytzagixhcjqcrfunjt.supabase.co/functions/v1/hello-world' \
        -H "Authorization: Bearer ${ANNON_KEY}" \
        -H "Content-Type: application/json" \
        -d '{"name":"やくしまる悦子"}'
  # console.log(`${ANNON_KEY}`);
  # console.log("curl -L -X GET 'https://fyrurrppyislugikvejj.supabase.co/functions/v1/check-email' -H `Authorization: Bearer ${ANNON_KEY}`");
}

function setEnv() {
  supabase secrets set --env-file ./supabase/.env --project-ref ajytzagixhcjqcrfunjt
}



# 関数名と一致 使用例: ./shell.sh checkEmailDep
if [ "$1" == "denoBuild" ]; then
  denoBuild
elif [ "$1" == "checkEmail" ]; then
  checkEmail
elif [ "$1" == "helloWorldDeploy" ]; then
  helloWorldDeploy
elif [ "$1" == "postHelloWorld" ]; then
  postHelloWorld
elif [ "$1" == "setEnv" ]; then
  setEnv
else
  echo "Unknown function: $1"
fi

# curl -L -X POST 'http://localhost:8000' -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZ5cnVycnBweWlzbHVnaWt2ZWpqIiwicm9sZSI6ImFub24iLCJpYXQiOjE2Nzg1NTU1MDcsImV4cCI6MTk5NDEzMTUwN30.YEMGiWDlD3w66X6uTfMyHAfqolLYA5OF-kf4UsoURI8' --data '{"name":"Functions"}'
# curl -L -X GET 'https://fyrurrppyislugikvejj.supabase.co/functions/v1/check-email' -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZ5cnVycnBweWlzbHVnaWt2ZWpqIiwicm9sZSI6ImFub24iLCJpYXQiOjE2Nzg1NTU1MDcsImV4cCI6MTk5NDEzMTUwN30.YEMGiWDlD3w66X6uTfMyHAfqolLYA5OF-kf4UsoURI8'