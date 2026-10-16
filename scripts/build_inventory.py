"""Record actual artifact files and explicit remaining production work."""
import hashlib
from common import ROOT, chapters, read_json, write_json, artifact_hash

for folder,meta in chapters():
    if not meta['publish']:continue
    meta['video_mode']='edit cuts awaiting author-recorded narration'
    write_json(folder/'chapter.json',meta)
    inventory=[]
    for directory in ['source','artwork','book','audio','video','social','web','previews']:
        for path in sorted((folder/directory).rglob('*')):
            if path.is_file():inventory.append({'path':path.relative_to(folder).as_posix(),'bytes_at_build':path.stat().st_size,'sha256_normalized_text_lf':artifact_hash(path)})
    write_json(folder/'docs/INVENTORY.json',inventory)
    products=[
       {'product':'Selected prose','state':'ready','path':meta['canonical_text']},
       {'product':'Source illustration and scene crops','state':'ready as supplied-art derivatives','path':'artwork/scenes/index.json'},
       {'product':'Illustrated A5 chapter','state':'editorial proof','path':'book/chapter-A5-proof.pdf'},
       {'product':'Interactive website','state':'ready for deployment','path':'web/index.html'},
       {'product':'Instagram carousel (five 3:4 cards)','state':'ready','path':'social/instagram/slide-01.jpg'},
       {'product':'Facebook image and copy','state':'ready','path':'social/facebook/post.jpg'},
       {'product':'YouTube thumbnail and description','state':'ready','path':'social/youtube/thumbnail.jpg'},
       {'product':'TikTok cover and caption','state':'ready','path':'social/tiktok/cover.jpg'},
       {'product':'9:16 discovery cut','state':'edit preview; author narration pending','path':'video/discovery-9x16.mp4'},
       {'product':'9:16 YouTube cut','state':'edit preview; author narration pending','path':'video/youtube-9x16.mp4'},
       {'product':'3:4 feed cut','state':'edit preview; author narration pending','path':'video/feed-3x4.mp4'},
       {'product':'SRT/VTT text timings','state':'provisional; retime to recorded narration','path':'video/timeline.json'},
       {'product':'Author reading script','state':'ready for recording','path':'audio/reading-script.md'},
    ]
    for product in products:
        if not (folder/product['path']).is_file():product['state']='missing'
    write_json(folder/'docs/PRODUCTS.json',{'chapter':meta['slug'],'products':products,'remaining':['Jason recorded narration and final timing/mix','Printer specifications and high-resolution art for certified print production','Physical-device and human screen-reader review','Author-managed social uploads; QR remains deferred']})
    table=['# Product set — '+meta['title'],'','| Product | Actual state | File |','|---|---|---|']
    table += [f'| {p["product"]} | {p["state"]} | [{p["path"]}](../{p["path"]}) |' for p in products]
    table += ['','Remaining: author recording, retimed narration captions, print-specific production and human device review. Social files are prepared; no platform post is claimed.','',f'Inventory: {len(inventory)} files, {sum(p["bytes_at_build"] for p in inventory):,} bytes. Checksums use LF-normalized text and raw binary bytes.']
    (folder/'docs/PRODUCT_SET.md').write_text('\n'.join(table)+'\n',encoding='utf-8')
    print(meta['slug'],len(inventory),'files inventoried')
