import { serve } from "https://deno.land/std@0.168.0/http/server.ts";
import supabaseAdmin from "supabaseAdmin";
import { corsHeaders } from "../_shared/cors.ts";

serve(async (req) => {
  // preflight fetch
  if (req.method === "OPTIONS") {
    return new Response("ok", { headers: corsHeaders });
  }

  if (req.method === "POST") {
    const { data, error } = await supabaseAdmin.from("users").select("email");
    const { email } = await req.json();
    const isRegistered = data.some((item: any) => item.email === email);
    const obj = {
      email,
      isRegistered,
    };

    if (error) {
      return new Response(JSON.stringify({ error: error.message }), {
        status: 500,
      });
    }

    return new Response(JSON.stringify(obj), {
      headers: {
        ...corsHeaders,
        "Content-Type": "application/json",
      },
    });
    // return new Response(JSON.stringify(data), {
    //   status: 200,
    //   headers: {
    //     ...corsHeaders,
    //     "Content-Type": "application/json",
    //   },
    // });
  }

  return new Response(JSON.stringify(req.method), {
    status: 200,
    headers: {
      ...corsHeaders,
      "Content-Type": "application/json",
    },
  });
});
