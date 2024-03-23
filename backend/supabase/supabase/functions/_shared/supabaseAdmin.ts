import { createClient, SupabaseClient } from "@supabase/supabase-js";
// import { load } from 'dotenv';
// const env = await load();
// #issue TODO: LocalでDeno.envを使ってenvを取得できるようにする
const PROJECT_URL = Deno.env.get("PROJECT_URL") || "YOUR_PROJECT_URL";
const SUPABASE_SERVICE_KEY = Deno.env.get("SERVICE_KEY") ||
  "YOUR_SERVICE_ROLE_KEY";
// const PROJECT_URL = env['PROJECT_URL'] || 'YOUR_PROJECT_URL';
// const SUPABASE_SERVICE_KEY = env['SUPABASE_SERVICE_KEY'] || 'YOUR_SERVICE_ROLE_KEY';

const supabaseAdmin: SupabaseClient = createClient(
  PROJECT_URL,
  SUPABASE_SERVICE_KEY,
);
// console.log(SUPABASE_SERVICE_KEY);
export default supabaseAdmin;
