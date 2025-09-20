<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Trip in Scotland - Yacintha & Loufi</title>
  <meta name="description" content="Trip Hub — Itinerary, Program, Pictures, Notes, Expenses, and Checklist for Scotland." />
  <style>
    :root{
      --bg:#0f172a; --panel:#111827; --text:#e5e7eb; --muted:#94a3b8;
      --accent:#22d3ee; --accent-2:#60a5fa; --border:#1f2937; --card:#0b1222;
    }
    *{box-sizing:border-box}
    body{margin:0;background:linear-gradient(180deg,#0b1020, #0f172a 40%);color:var(--text);font-family:system-ui,-apple-system,Segoe UI,Roboto,Ubuntu,Cantarell,Noto Sans,sans-serif}
    .container{max-width:1100px;margin:0 auto;padding:24px}
    header{display:flex;gap:12px;align-items:center;justify-content:space-between;flex-wrap:wrap;margin-bottom:16px}
    h1{font-size:clamp(20px,3vw,28px);margin:0}
    .subtitle{color:var(--muted);font-size:14px}
    .btn{background:rgba(255,255,255,.06);border:1px solid var(--border);color:var(--text);padding:10px 14px;border-radius:12px;cursor:pointer;display:inline-flex;gap:8px;align-items:center}
    .tabs{display:grid;grid-template-columns:repeat(6,1fr);gap:8px;border:1px solid var(--border);border-radius:14px;overflow:hidden}
    .tab{padding:10px 8px;text-align:center;background:rgba(255,255,255,.04);cursor:pointer;color:var(--muted);font-weight:600}
    .tab.active{background:linear-gradient(90deg,rgba(34,211,238,.15),rgba(96,165,250,.15));color:#fff}
    .content{margin-top:16px}
    .card{background:linear-gradient(180deg,rgba(255,255,255,.03),rgba(255,255,255,.015));border:1px solid var(--border);border-radius:16px;box-shadow:0 10px 30px rgba(0,0,0,.25)}
    .card h2{margin:0;padding:16px 18px;border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;gap:14px;font-size:18px}
    .card .body{padding:16px 18px}
    input[type=text], input[type=number], select, textarea{width:100%;background:#0b1222;border:1px solid var(--border);color:var(--text);padding:10px 12px;border-radius:12px}
    textarea{min-height:130px;resize:vertical}
    .row{display:flex;gap:10px;align-items:center;flex-wrap:wrap}
    .badge{background:rgba(255,255,255,.06);border:1px solid var(--border);padding:4px 8px;border-radius:999px;font-size:12px;color:#d1d5db}
    .list{display:grid;gap:10px}
    .list .item{border:1px solid var(--border);border-radius:14px;padding:12px;background:rgba(255,255,255,.02)}
    .muted{color:var(--muted)}
    .grid{display:grid;gap:12px}
    @media(min-width:700px){.grid.cols-2{grid-template-columns:repeat(2,1fr)}.grid.cols-3{grid-template-columns:repeat(3,1fr)}.grid.cols-4{grid-template-columns:repeat(4,1fr)}}
    .drop{border:2px dashed var(--border);border-radius:16px;padding:28px;text-align:center;background:rgba(255,255,255,.02)}
    .gallery{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:12px}
    .gallery figure{border:1px solid var(--border);border-radius:14px;overflow:hidden;background:#081022}
    .gallery img{width:100%;height:180px;object-fit:cover;display:block}
    .progress{height:10px;background:#0b1222;border:1px solid var(--border);border-radius:999px;overflow:hidden}
    .progress > div{height:100%;background:linear-gradient(90deg,var(--accent),var(--accent-2));width:0%}
    footer{color:var(--muted);font-size:12px;margin-top:18px}
    .link{color:#c7d2fe;text-decoration:none}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div>
        <h1>Trip in Scotland — Yacintha & Loufi 🏴</h1>
        <div class="subtitle" id="subtitle">21/09 → 26/09 — Scotland</div>
      </div>
      <div class="row">
        <button class="btn" id="exportBtn">💾 Export</button>
        <button class="btn" id="importBtn">📥 Import</button>
        <input type="file" id="fileInput" accept="application/json" style="display:none" />
      </div>
    </header>

    <nav class="tabs" id="tabs">
      <div class="tab active" data-tab="itinerary">🗺️ Itinerary</div>
      <div class="tab" data-tab="program">🎯 Program</div>
      <div class="tab" data-tab="gallery">📷 Pictures</div>
      <div class="tab" data-tab="notes">📝 Notes</div>
      <div class="tab" data-tab="expenses">💷 Expenses</div>
      <div class="tab" data-tab="checklist">✅ Checklist</div>
    </nav>

    <section class="content">
      <!-- Itinerary -->
      <div id="itinerary" class="card">
        <h2>
          <span>Itinerary (editable)</span>
          <span class="row">
            <input type="text" id="newDayDate" placeholder="Date (e.g. 21/09)" style="width:110px" />
            <input type="text" id="newDayTitle" placeholder="Title" style="width:180px" />
            <input type="text" id="newDayDetails" placeholder="Details (optional)" style="width:260px" />
            <button class="btn" id="addDayBtn">➕ Add day</button>
          </span>
        </h2>
        <div class="body">
          <div class="list" id="itineraryList"></div>
        </div>
      </div>

      <!-- Program -->
      <div id="program" class="card" style="margin-top:16px; display:none">
        <h2>
          <span>Program — suggestions for Edinburgh</span>
          <span class="row">
            <select id="programDaySelect"></select>
            <select id="programPick"><option value="">— Choose —</option></select>
            <button class="btn" id="programAdd">Add</button>
          </span>
        </h2>
        <div class="body">
          <p class="muted">Pick a day, choose a suggestion, and add it — suggestions will be appended to the day's details.</p>
          <div id="programSuggestions" class="grid cols-3"></div>
        </div>
      </div>

      <!-- Gallery -->
      <div id="gallery" class="card" style="margin-top:16px; display:none">
        <h2>
          <span>Pictures</span>
          <span class="row">
            <button class="btn" id="addPhotosBtn">➕ Add</button>
            <input type="file" id="photosInput" accept="image/*" multiple style="display:none" />
          </span>
        </h2>
        <div class="body">
          <div class="drop" id="dropZone">Drag & drop your photos here or click “Add”.</div>
          <div id="galleryGrid" class="gallery" style="margin-top:12px"></div>
          <p id="galleryEmpty" class="muted" style="text-align:center;display:none">No photos yet.</p>
        </div>
      </div>

      <!-- Notes -->
      <div id="notes" class="card" style="margin-top:16px; display:none">
        <h2>
          <span>Notes</span>
          <span class="row muted" style="font-size:12px">Auto timestamp <input type="checkbox" id="autoDate" checked /></span>
        </h2>
        <div class="body">
          <div class="row" style="margin-bottom:8px">
            <button class="btn" data-stamp="🍺">🍺</button>
            <button class="btn" data-stamp="🥧">🥧</button>
            <button class="btn" data-stamp="🏰">🏰</button>
            <button class="btn" data-stamp="🎶">🎶</button>
            <button class="btn" data-stamp="🌊">🌊</button>
          </div>
          <textarea id="notesArea" placeholder="Your notes..."></textarea>
        </div>
      </div>

      <!-- Expenses -->
      <div id="expenses" class="card" style="margin-top:16px; display:none">
        <h2>
          <span>Expenses</span>
          <span class="row">
            <select id="payer"><option>Yacintha</option><option>Loufi</option></select>
            <input type="text" id="expenseWhat" placeholder="What" style="width:160px" />
            <input type="number" id="expenseAmt" placeholder="Amount" step="0.01" style="width:110px" />
            <select id="expenseCat"><option>Food</option><option>Transport</option><option>Accommodation</option><option>Other</option></select>
            <input type="text" id="expenseCur" value="GBP" style="width:90px" />
            <button class="btn" id="expenseAdd">Add</button>
          </span>
        </h2>
        <div class="body">
          <table style="width:100%;border-collapse:collapse">
            <thead><tr style="color:#cbd5e1"><th style="padding:8px;border-bottom:1px solid var(--border)">Date</th><th style="padding:8px;border-bottom:1px solid var(--border)">Payer</th><th style="padding:8px;border-bottom:1px solid var(--border)">What</th><th style="padding:8px;border-bottom:1px solid var(--border)">Category</th><th style="padding:8px;border-bottom:1px solid var(--border)">Amount</th><th></th></tr></thead>
            <tbody id="expenseTbody"></tbody>
          </table>
          <div style="margin-top:12px;display:flex;gap:10px;flex-wrap:wrap">
            <div style="padding:10px;border:1px solid var(--border);border-radius:10px">Total Yacintha: <strong id="totY">0</strong></div>
            <div style="padding:10px;border:1px solid var(--border);border-radius:10px">Total Loufi: <strong id="totL">0</strong></div>
            <div style="padding:10px;border:1px solid var(--border);border-radius:10px">Grand total: <strong id="totAll">0</strong> <span id="totCur"></span></div>
            <div style="padding:10px;border:1px solid var(--border);border-radius:10px">Settlement: <strong id="settlement">—</strong></div>
          </div>
        </div>
      </div>

      <!-- Checklist -->
      <div id="checklist" class="card" style="margin-top:16px; display:none">
        <h2><span>Checklist</span><span class="badge" id="progressBadge">Progress: 0%</span></h2>
        <div class="body">
          <div class="progress"><div id="progressBar"></div></div>
          <div class="row" style="margin-top:12px;margin-bottom:12px">
            <input type="text" id="taskInput" placeholder="Add an item" />
            <button class="btn" id="taskAdd">Add</button>
          </div>
          <div id="taskList" class="list"></div>
        </div>
      </div>

      <footer>Stored locally. Use Export/Import to back up or share.</footer>
    </section>
  </div>

  <script>
    const STORAGE_KEY = "trip-scotland-yacintha-loufi-v1";
    const defaultData = {
      dates:"21/09 → 26/09",
      itinerary:[
        {date:"21/09", title:"Arrival — Hotel — Rest", details:"Arrive in Edinburgh, check-in, relax."},
        {date:"22/09", title:"Edinburgh visit", details:"Old Town, Royal Mile, Edinburgh Castle, Dean Village."},
        {date:"23/09", title:"Campervan pick up", details:"Pick up campervan, groceries, start drive."},
        {date:"24/09", title:"Isle of Skye", details:"Highlights: Fairy Pools, Old Man of Storr, Quiraing."},
        {date:"25/09", title:"Return Edinburgh — Rest", details:"Return van, hotel, calm evening."},
        {date:"26/09", title:"Return Brussels", details:"Flight back to Brussels."}
      ],
      programSuggestions:[
        "Edinburgh Castle guided visit",
        "Arthur's Seat hike (morning)",
        "Dean Village + Water of Leith walk",
        "National Museum of Scotland (free)",
        "Scottish National Gallery",
        "Ghost tour in Old Town (evening)",
        "Calton Hill sunset",
        "Princes Street Gardens picnic",
        "Haggis tasting at a traditional pub",
        "Camera Obscura & World of Illusions"
      ],
      notes:"",
      gallery:[],
      expenses:{currency:"GBP", items:[]},
      checklist:[
        {id:"id",text:"Passport / ID",done:false},
        {id:"tickets",text:"Flight tickets / QR codes",done:false},
        {id:"cards",text:"Bank cards + cash",done:false},
        {id:"rainjacket",text:"Rain jacket",done:false},
        {id:"shoes",text:"Walking shoes",done:false},
        {id:"sleepbag",text:"Sleeping bag (campervan)",done:false},
        {id:"toothbrush",text:"Toothbrushes",done:false},
        {id:"toothpaste",text:"Toothpaste",done:false},
        {id:"adapter",text:"UK plug adapter (Type G)",done:false},
        {id:"chargers",text:"Chargers & powerbank",done:false},
        {id:"meds",text:"Basic meds (ibuprofen, plasters)",done:false}
      ]
    };

    function loadState(){ try{ const r=localStorage.getItem(STORAGE_KEY); return r?JSON.parse(r):defaultData; }catch(e){return defaultData;} }
    function saveState(){ localStorage.setItem(STORAGE_KEY, JSON.stringify(state)); }
    function escapeHtml(s){ return String(s).replace(/[&<>"']/g, m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m])); }

    let state = loadState();
    document.getElementById("subtitle").textContent = state.dates + " — Scotland";

    // Tabs
    document.querySelectorAll(".tab").forEach(t=>{
      t.addEventListener("click",()=>{
        document.querySelectorAll(".tab").forEach(x=>x.classList.remove("active"));
        t.classList.add("active");
        const name = t.dataset.tab;
        document.querySelectorAll(".card").forEach(c=>c.style.display="none");
        document.getElementById(name).style.display = "";
      });
    });

    // Itinerary
    const itineraryList = document.getElementById("itineraryList");
    function renderItinerary(){
      itineraryList.innerHTML = "";
      state.itinerary.forEach((it, idx)=>{
        const wrap = document.createElement("div");
        wrap.className = "item";
        wrap.innerHTML = `<div class="row" style="justify-content:space-between;align-items:center;margin-bottom:8px">
          <div class="row"><span class="badge">${escapeHtml(it.date)}</span><input type="text" value="${escapeHtml(it.title)}" data-k="title" style="min-width:250px" /></div>
          <div class="row"><button class="btn" data-action="up">⬆️</button><button class="btn" data-action="down">⬇️</button><button class="btn" data-action="del">🗑️</button></div>
          </div><textarea data-k="details">${escapeHtml(it.details||"")}</textarea>`;
        wrap.querySelector('[data-action="up"]').onclick = ()=>{ if(idx>0){ const a=state.itinerary[idx-1]; state.itinerary[idx-1]=state.itinerary[idx]; state.itinerary[idx]=a; saveState(); renderItinerary(); bootProgram(); } };
        wrap.querySelector('[data-action="down"]').onclick = ()=>{ if(idx<state.itinerary.length-1){ const a=state.itinerary[idx+1]; state.itinerary[idx+1]=state.itinerary[idx]; state.itinerary[idx]=a; saveState(); renderItinerary(); bootProgram(); } };
        wrap.querySelector('[data-action="del"]').onclick = ()=>{ state.itinerary.splice(idx,1); saveState(); renderItinerary(); bootProgram(); };
        wrap.querySelectorAll("input,textarea").forEach(field=>{ field.addEventListener("input", ()=>{ const k = field.dataset.k; state.itinerary[idx][k] = field.value; saveState(); bootProgram(); }); });
        itineraryList.appendChild(wrap);
      });
    }
    document.getElementById("addDayBtn").onclick = ()=>{
      const d = document.getElementById("newDayDate").value.trim();
      const title = document.getElementById("newDayTitle").value.trim();
      const details = document.getElementById("newDayDetails").value.trim();
      if(!d||!title) return;
      state.itinerary.push({date:d,title,details});
      document.getElementById("newDayDate").value=""; document.getElementById("newDayTitle").value=""; document.getElementById("newDayDetails").value="";
      saveState(); renderItinerary(); bootProgram();
    };

    // Program suggestions
    function bootProgram(){
      const sel = document.getElementById("programDaySelect");
      sel.innerHTML = "";
      state.itinerary.forEach((it, idx)=>{ const o=document.createElement("option"); o.value=idx; o.textContent=(it.date?it.date+" — ":"")+it.title; sel.appendChild(o); });
      const pick = document.getElementById("programPick"); pick.innerHTML = '<option value="">— Choose —</option>';
      state.programSuggestions.forEach((s,i)=>{ const o=document.createElement("option"); o.value=i; o.textContent=s; pick.appendChild(o); });
      const grid = document.getElementById("programSuggestions"); grid.innerHTML = "";
      state.programSuggestions.forEach((s)=>{ const b=document.createElement("button"); b.className="btn"; b.style.margin="6px 6px 6px 0"; b.textContent="＋ "+s; b.onclick=()=>{ const idx=parseInt(document.getElementById("programDaySelect").value||"0",10); if(state.itinerary[idx]){ state.itinerary[idx].details=(state.itinerary[idx].details?state.itinerary[idx].details+"\\n":"")+"• "+s; saveState(); renderItinerary(); } }; grid.appendChild(b); });
    }
    document.getElementById("programAdd").onclick = ()=>{
      const pick = document.getElementById("programPick"); const i=parseInt(pick.value||"-1",10); const sel = document.getElementById("programDaySelect"); const d=parseInt(sel.value||"0",10);
      if(i>=0 && state.itinerary[d]){ const s = state.programSuggestions[i]; state.itinerary[d].details=(state.itinerary[d].details?state.itinerary[d].details+"\\n":"")+"• "+s; saveState(); renderItinerary(); }
    };

    // Gallery
    const galleryGrid = document.getElementById("galleryGrid");
    const galleryEmpty = document.getElementById("galleryEmpty");
    const dropZone = document.getElementById("dropZone");
    function renderGallery(){ galleryGrid.innerHTML=""; galleryEmpty.style.display = state.gallery.length ? "none":"block"; state.gallery.forEach(item=>{ const fig=document.createElement("figure"); fig.innerHTML = `<img src="${item.src}" alt="photo" /><figcaption style="padding:10px;border-top:1px solid var(--border)"><input type="text" value="${escapeHtml(item.caption||'')}" placeholder="Caption..." data-id="${item.id}" class="caption"/><div class="row" style="margin-top:6px;justify-content:space-between;font-size:12px;color:var(--muted)"><span>${item.date}</span><button class="btn" data-del="${item.id}">🗑️</button></div></figcaption>`; fig.querySelector('[data-del]').onclick=()=>{ state.gallery=state.gallery.filter(g=>g.id!==item.id); saveState(); renderGallery(); }; fig.querySelector('.caption').oninput=(e)=>{ const g=state.gallery.find(x=>x.id===item.id); g.caption=e.target.value; saveState(); }; galleryGrid.appendChild(fig); }); }
    function handleFiles(files){ const arr=Array.from(files).slice(0,60); (async ()=>{ for(const f of arr){ if(!f.type.startsWith("image/")) continue; const src = await compressImage(f,1600,1600,0.86); state.gallery.push({id:crypto.randomUUID(), src, caption:"", date:new Date().toLocaleDateString()}); } saveState(); renderGallery(); })(); }
    document.getElementById("addPhotosBtn").onclick = ()=> document.getElementById("photosInput").click();
    document.getElementById("photosInput").addEventListener("change",(e)=> handleFiles(e.target.files));
    ["dragover","dragenter"].forEach(ev=> dropZone.addEventListener(ev,(e)=>{ e.preventDefault(); dropZone.style.background="rgba(255,255,255,.04)"; }));
    ["dragleave","drop"].forEach(ev=> dropZone.addEventListener(ev,(e)=>{ e.preventDefault(); dropZone.style.background=""; }));
    dropZone.addEventListener("drop",(e)=> handleFiles(e.dataTransfer.files));
    function compressImage(file, maxW, maxH, quality=0.85){ return new Promise((resolve,reject)=>{ const img=new Image(); const reader=new FileReader(); reader.onload=()=>{ img.src=reader.result; }; reader.onerror=reject; img.onload=()=>{ const ratio=Math.min(maxW/img.width, maxH/img.height, 1); const canvas=document.createElement("canvas"); canvas.width=Math.round(img.width*ratio); canvas.height=Math.round(img.height*ratio); const ctx=canvas.getContext("2d"); ctx.drawImage(img,0,0,canvas.width,canvas.height); try{ resolve(canvas.toDataURL("image/jpeg", quality)); }catch(e){ reject(e);} }; img.onerror=reject; reader.readAsDataURL(file); }); }

    // Notes
    const notesArea = document.getElementById("notesArea");
    notesArea.value = state.notes || "";
    document.querySelectorAll('#notes [data-stamp]').forEach(btn=>btn.addEventListener("click",()=>{ const stamp=btn.dataset.stamp; const prefix=document.getElementById("autoDate").checked? "\\n["+new Date().toLocaleString()+"] " : "\\n"; notesArea.value += prefix + stamp + " "; state.notes = notesArea.value; saveState(); }));
    notesArea.addEventListener("input",()=>{ state.notes = notesArea.value; saveState(); });

    // Expenses
    function renderExpenses(){ const tbody=document.getElementById("expenseTbody"); tbody.innerHTML=""; let y=0,l=0,cur=state.expenses.currency||"GBP"; state.expenses.items.forEach((ex,idx)=>{ const tr=document.createElement("tr"); tr.innerHTML = `<td style="padding:8px;border-bottom:1px solid var(--border)">${escapeHtml(ex.date||"")}</td><td style="padding:8px;border-bottom:1px solid var(--border)">${escapeHtml(ex.who)}</td><td style="padding:8px;border-bottom:1px solid var(--border)">${escapeHtml(ex.what)}</td><td style="padding:8px;border-bottom:1px solid var(--border)">${escapeHtml(ex.cat)}</td><td style="padding:8px;border-bottom:1px solid var(--border)">${Number(ex.amt).toFixed(2)} ${cur}</td><td style="padding:8px;border-bottom:1px solid var(--border)"><button class="btn" data-del="${idx}">🗑️</button></td>`; tr.querySelector('[data-del]').onclick=()=>{ state.expenses.items.splice(idx,1); saveState(); renderExpenses(); }; tbody.appendChild(tr); if(ex.who==="Yacintha") y+=Number(ex.amt)||0; else l+=Number(ex.amt)||0; }); const all=y+l; document.getElementById("totY").textContent = y.toFixed(2)+" "+cur; document.getElementById("totL").textContent = l.toFixed(2)+" "+cur; document.getElementById("totAll").textContent = all.toFixed(2); document.getElementById("totCur").textContent = cur; const half=all/2; let text="—"; if(all>0){ if(y>half) text="Loufi owes "+(y-half).toFixed(2)+" "+cur+" to Yacintha"; else if(l>half) text="Yacintha owes "+(l-half).toFixed(2)+" "+cur+" to Loufi"; else text="Balanced"; } document.getElementById("settlement").textContent = text; }
    document.getElementById("expenseAdd").onclick = ()=>{ const who=document.getElementById("payer").value; const what=document.getElementById("expenseWhat").value.trim(); const amt=parseFloat(document.getElementById("expenseAmt").value); const cat=document.getElementById("expenseCat").value; const cur=document.getElementById("expenseCur").value.trim()||"GBP"; if(!what||isNaN(amt)) return; state.expenses.currency=cur; state.expenses.items.push({date:new Date().toLocaleDateString(), who, what, cat, amt}); document.getElementById("expenseWhat").value=""; document.getElementById("expenseAmt").value=""; saveState(); renderExpenses(); };

    // Checklist
    const taskList = document.getElementById("taskList");
    function renderChecklist(){ taskList.innerHTML=""; let done=0,total=state.checklist.length||1; state.checklist.forEach(i=>{ if(i.done) done++; }); const pct=Math.round(done/total*100); document.getElementById("progressBadge").textContent="Progress: "+pct+"%"; document.getElementById("progressBar").style.width=pct+"%"; state.checklist.forEach(item=>{ const div=document.createElement("div"); div.className="item row"; div.style.justifyContent="space-between"; div.innerHTML = `<label class="row" style="gap:10px"><input type="checkbox" ${item.done?"checked":""} data-id="${item.id}" /><span style="${item.done?'text-decoration:line-through;color:var(--muted)':''}">${escapeHtml(item.text)}</span></label><button class="btn" data-del="${item.id}">🗑️</button>`; div.querySelector('[data-id]').onchange=(e)=>{ const id=e.target.getAttribute('data-id'); const el=state.checklist.find(c=>c.id===id); el.done=!el.done; saveState(); renderChecklist(); }; div.querySelector('[data-del]').onclick=()=>{ const id=div.querySelector('[data-del]').getAttribute('data-del'); state.checklist=state.checklist.filter(c=>c.id!==id); saveState(); renderChecklist(); }; taskList.appendChild(div); }); }
    document.getElementById("taskAdd").onclick = ()=>{ const val=document.getElementById("taskInput").value.trim(); if(!val) return; state.checklist.push({id:crypto.randomUUID(), text:val, done:false}); document.getElementById("taskInput").value=""; saveState(); renderChecklist(); };

    // Export/Import
    document.getElementById("exportBtn").onclick = ()=>{ const blob=new Blob([JSON.stringify(state,null,2)],{type:"application/json"}); const url=URL.createObjectURL(blob); const a=document.createElement("a"); a.href=url; a.download="trip-scotland-yacintha-loufi.json"; a.click(); URL.revokeObjectURL(url); };
    document.getElementById("importBtn").onclick = ()=> document.getElementById("fileInput").click();
    document.getElementById("fileInput").addEventListener("change",(e)=>{ const f=e.target.files[0]; if(!f) return; const reader=new FileReader(); reader.onload=()=>{ try{ state = {...state, ...JSON.parse(reader.result)}; saveState(); boot(); }catch(err){ alert("Invalid file"); } }; reader.readAsText(f); });

    function boot(){ renderItinerary(); bootProgram(); renderGallery(); renderChecklist(); renderExpenses(); }
    boot();
  </script>
</body>
</html>

