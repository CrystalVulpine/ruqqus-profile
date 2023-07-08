## [GitHub pages site](https://crystalvulpine.github.io/ruqqus-profile/)

This is an archive site meant to bring back all my ruqqus posts since the site shut down. It uses nunjucks to render ruqqus's jinja2 templates with static json data plugged in.

Some data might be missing or corrupted, and much of the usual functionality of ruqqus is broken or bugged. Also some information is not included, such as badges, rep, join dates, and user titles (though this one can be found in the JSON files). Some accounts have snapshots on archive.org or archive.is where you can see that. This project is only meant to provide a full set of data.

Some posts were skipped by the API. If it had no comments, it will not render on the site but you can find JSON data here:

[CrystalVulpine](https://crystalvulpine.github.io/ruqqus-profile/CrystalVulpine_missing_posts.json)  
[sfrohne](https://crystalvulpine.github.io/ruqqus-profile/sfrohne_missing_posts.json)  
[foxite](https://crystalvulpine.github.io/ruqqus-profile/foxite_missing_posts.json)  
[ExperiBass](https://crystalvulpine.github.io/ruqqus-profile/ExperiBass_missing_posts.json)

These posts should appear on searchvoat.co, but its ruqqus search seems to be broken right now.

You can click on any of my posts or comments to browse the rest of that post as well.

---

If you want to try an account for yourself, you do `python3 find.py username`. Then you run `make_listing.sh`.

You'll have to download and un7zip the data first:

https://archive.org/download/ruqqus-public-dataset/submissions.f1.2021-10-30.txt.sort.2021-11-10.7z

https://archive.org/download/ruqqus-public-dataset/comments.fx.2021-10-30.txt.sort.2021-11-08.7z

https://archive.org/download/ruqqus-public-dataset/ruqqus.submf.2021-10-14.json
