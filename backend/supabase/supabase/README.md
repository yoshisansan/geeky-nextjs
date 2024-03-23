## 用途

SupabaseのAdmin権限専用のAPIを格納したディレクトリ

## 始め方

1. Denoをインストール https://docs.deno.com/runtime/manual/getting_started
2. DenoのVSCode拡張機能をインストール(VSCode使用者の場合)
3. 実行

```
deno run supabase/functions/hello-world/index.ts
```

4. 関数

```
curl -k -X POST -H 'Content-Type: application/json' http://localhost:8000/ -d '{"name": "天丼マン"}'

or

chmod 755 ./supabase/deno.sh
./supabase/deno.sh denoBuild

```

### インストール済みでエラーが出る場合

denoのライブラリをアップデートすれば直るかも

## 注意事項

Denoのimport周りでエラーが生じる場合、.vscode/settings.jsonでのimport_map.jsonのpathが相対パスのためエラーとなっているかも。
import_map.jsonのpathを絶対パスに変更するか別途supabaseフォルダ起点にvscodeを開くと動作すると思います
