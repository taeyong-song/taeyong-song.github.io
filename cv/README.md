# CV update workflow

The homepage and CV share one content source:

`_data/profile.yml`

Update education, publications, projects, honors, or activities there, then run from the repository root:

```powershell
.\scripts\build_cv.cmd
```

The command regenerates both:

- `cv/tae-yong-song-cv.tex`
- `files/cv/tae-yong-song-cv.pdf`

The first run installs PyYAML into the ignored `.cv-tools` directory. The command uses a one-process PowerShell execution-policy bypass, so no system setting is changed. CV-only English wording can be supplied next to a website entry with `cv_title`, `cv_authors`, or `cv_venue`; otherwise the standard profile fields are used automatically.

Typography and page-layout rules live in `cv/tae-yong-song-cv.template.tex`. Do not edit the generated `.tex` file directly.
