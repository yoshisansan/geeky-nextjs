import { createClient, SupabaseClient } from "@supabase/supabase-js";

const PROJECT_URL = Deno.env.get("PROJECT_URL") || "YOUR_PROJECT_URL";
const ANNON_KEY = Deno.env.get("SERVICE_KEY") || "ANNON";

const supabaseClient: SupabaseClient = createClient(PROJECT_URL, ANNON_KEY);

export default supabaseClient;
