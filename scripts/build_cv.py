#!/usr/bin/env python3
"""Generate Tae Yong Song's LaTeX CV and PDF from _data/profile.yml."""

from __future__ import annotations

import argparse
import calendar
import datetime as dt
import shutil
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError as exc:
    raise SystemExit(
        "PyYAML is required. Run scripts/build_cv.ps1, which installs it locally."
    ) from exc


ROOT = Path(__file__).resolve().parents[1]
PROFILE_PATH = ROOT / "_data" / "profile.yml"
TEMPLATE_PATH = ROOT / "cv" / "tae-yong-song-cv.template.tex"
TEX_PATH = ROOT / "cv" / "tae-yong-song-cv.tex"
PDF_PATH = ROOT / "files" / "cv" / "tae-yong-song-cv.pdf"
BUILD_DIR = ROOT / "tmp" / "pdfs" / "cv-build"


def tex_escape(value: object) -> str:
    text = str(value or "")
    text = (
        text.replace("–", "--")
        .replace("—", "---")
        .replace("’", "'")
        .replace("“", "``")
        .replace("”", "''")
        .replace(" ", " ")
    )
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(char, char) for char in text)


def href(url: str, label: str) -> str:
    if not url:
        return label
    safe_url = str(url).replace("{", "").replace("}", "")
    return rf"\href{{\detokenize{{{safe_url}}}}}{{{label}}}"


def bold_self(authors: object, self_names: list[str]) -> str:
    result = tex_escape(authors)
    for name in self_names:
        escaped = tex_escape(name)
        result = result.replace(escaped, rf"\textbf{{{escaped}}}")
    return result


def load_profile() -> dict:
    with PROFILE_PATH.open("r", encoding="utf-8") as stream:
        profile = yaml.safe_load(stream) or {}
    required = ("cv", "education", "publications", "projects", "honors", "activities")
    missing = [key for key in required if key not in profile]
    if missing:
        raise ValueError(f"Missing profile.yml sections: {', '.join(missing)}")
    return profile


def render_header(meta: dict) -> str:
    links = [
        ("Website", meta.get("website")),
        ("Google Scholar", meta.get("google_scholar")),
        ("GitHub", meta.get("github")),
        ("LinkedIn", meta.get("linkedin")),
    ]
    link_text = r"\enspace|\enspace".join(
        href(url, tex_escape(label)) for label, url in links if url
    )
    affiliation = (r"\\[1pt]" + "\n  ").join(
        rf"{{\small {tex_escape(line)}}}" for line in meta.get("affiliation", [])
    )
    return rf"""\begin{{center}}
  {{\fontsize{{23}}{{27}}\selectfont\bfseries {tex_escape(meta.get('name'))}}}\\[3pt]
  {{\normalsize {tex_escape(meta.get('headline'))}}}\\[2pt]
  {affiliation}\\[4pt]
  {{\small {link_text}}}
\end{{center}}

\vspace{{1pt}}
\hrule
\vspace{{5pt}}"""


def render_education(entries: list[dict]) -> str:
    blocks = [r"\section{Education}"]
    for item in entries:
        degree_line = (
            rf"\textbf{{{tex_escape(item.get('degree'))}}}, "
            + tex_escape(item.get("institution"))
        )
        details = []
        if item.get("advisor"):
            details.append(f"Advisor: {tex_escape(item['advisor'])}")
        if item.get("thesis"):
            details.append(f"Thesis: ``{tex_escape(item['thesis'])}''")
        period = tex_escape(item.get("period"))
        if details:
            blocks.append(
                rf"\entry{{{period}}}" + "\n"
                rf"  {{{degree_line}}}" + "\n"
                rf"  {{{r'\newline '.join(details)}}}"
            )
        else:
            blocks.append(rf"\singleentry{{{period}}}" + "\n" + rf"  {{{degree_line}}}")
    return "\n".join(blocks)


CATEGORY_LABELS = {
    "international_journal": "International Journal Articles",
    "domestic_journal": "Domestic Journal Articles",
    "international_conference": "International Conference Papers",
    "domestic_conference": "Domestic Conference Papers",
}


def render_publications(entries: list[dict], self_names: list[str]) -> str:
    blocks = [r"\section{Publications}"]
    for category, label in CATEGORY_LABELS.items():
        category_entries = [item for item in entries if item.get("category") == category]
        if not category_entries:
            continue
        category_entries.sort(key=lambda item: int(item.get("year", 0)), reverse=True)
        blocks.append(
            rf"\textbf{{\color{{slate}}{tex_escape(label)}}}\par\vspace{{2pt}}"
        )
        for item in category_entries:
            title = tex_escape(item.get("cv_title") or item.get("title"))
            link = item.get("doi") or item.get("scholar_url") or ""
            title = href(link, title)
            authors = bold_self(item.get("cv_authors") or item.get("authors"), self_names)
            venue = tex_escape(item.get("cv_venue") or item.get("venue")).rstrip(".")
            details = f"{authors}. \\textit{{{venue}}}."
            if item.get("award"):
                details += rf" \textbf{{{tex_escape(item['award'])}.}}"
            blocks.append(
                rf"\publication{{{tex_escape(item.get('year'))}}}" + "\n"
                rf"  {{{title}}}" + "\n"
                rf"  {{{details}}}"
            )
        blocks.append(r"\vspace{2pt}")
    if blocks[-1] == r"\vspace{2pt}":
        blocks.pop()
    return "\n".join(blocks)


def render_projects(entries: list[dict]) -> str:
    blocks = [r"\newpage", r"\section{Research Projects}"]
    for item in sorted(entries, key=lambda row: str(row.get("sort_date", "")), reverse=True):
        blocks.append(
            rf"\project{{{tex_escape(item.get('period'))}}}" + "\n"
            rf"  {{{tex_escape(item.get('title'))}}}" + "\n"
            rf"  {{{tex_escape(item.get('sponsor'))}}}"
        )
    return "\n".join(blocks)


def render_activities(groups: list[dict]) -> str:
    blocks = []
    for group in groups:
        items = group.get("items") or []
        if not items:
            continue
        section_name = "Teaching Experience" if group.get("category") == "Teaching" else group.get("category")
        blocks.append(rf"\section{{{tex_escape(section_name)}}}")
        for item in items:
            blocks.append(
                rf"\entry{{{tex_escape(item.get('year'))}}}" + "\n"
                rf"  {{\textbf{{{tex_escape(item.get('title'))}}}, Seoul National University}}" + "\n"
                rf"  {{{tex_escape(item.get('description'))}}}"
            )
    return "\n".join(blocks)


def render_honors(entries: list[dict], website: str) -> str:
    blocks = [r"\section{Honors}"]
    for item in sorted(entries, key=lambda row: int(row.get("year", 0)), reverse=True):
        certificate = str(item.get("certificate_url") or "")
        if certificate.startswith("/"):
            certificate = website.rstrip("/") + certificate
        title = href(certificate, rf"\textbf{{{tex_escape(item.get('title'))}}}")
        blocks.append(
            rf"\entry{{{tex_escape(item.get('year'))}}}" + "\n"
            rf"  {{{title}}}" + "\n"
            rf"  {{{tex_escape(item.get('proceedings'))}}}"
        )
    return "\n".join(blocks)


def render_footer(meta: dict) -> str:
    updated = meta.get("last_updated")
    if not updated:
        today = dt.date.today()
        updated = f"{calendar.month_name[today.month]} {today.year}"
    website = str(meta.get("website") or "")
    display_url = website.removeprefix("https://").removeprefix("http://").rstrip("/")
    return (
        r"\vfill" + "\n"
        + rf"{{\footnotesize\color{{slate}}Last updated: {tex_escape(updated)} \hfill "
        + "Full publication details and project updates: "
        + href(website, tex_escape(display_url))
        + "}"
    )


def generate_tex(profile: dict) -> str:
    meta = profile["cv"]
    content = "\n\n".join(
        [
            render_header(meta),
            render_education(profile["education"]),
            render_publications(profile["publications"], meta.get("self_names", [])),
            render_projects(profile["projects"]),
            render_activities(profile["activities"]),
            render_honors(profile["honors"], str(meta.get("website") or "")),
            render_footer(meta),
        ]
    )
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    generated_notice = (
        "% AUTO-GENERATED from _data/profile.yml by scripts/build_cv.py.\n"
        "% Edit profile.yml or the .template.tex file, not this generated file.\n"
    )
    return generated_notice + template.replace(
        "@@FOOTER_NAME@@", tex_escape(meta.get("name"))
    ).replace("@@CONTENT@@", content)


def compile_pdf() -> None:
    xelatex = shutil.which("xelatex")
    if not xelatex:
        raise RuntimeError("xelatex was not found on PATH; the .tex file was generated only.")
    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    command = [
        xelatex,
        "-interaction=nonstopmode",
        "-halt-on-error",
        "-output-directory=tmp/pdfs/cv-build",
        "cv/tae-yong-song-cv.tex",
    ]
    for _ in range(2):
        result = subprocess.run(
            command,
            cwd=ROOT,
            text=True,
            encoding="utf-8",
            errors="replace",
            capture_output=True,
        )
        if result.returncode:
            combined_log = (result.stdout or "") + "\n" + (result.stderr or "")
            log_tail = "\n".join(combined_log.splitlines()[-35:])
            raise RuntimeError(f"xelatex failed:\n{log_tail}")
    built_pdf = BUILD_DIR / TEX_PATH.with_suffix(".pdf").name
    PDF_PATH.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(built_pdf, PDF_PATH)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--generate-only", action="store_true", help="Write .tex without compiling PDF")
    args = parser.parse_args()
    profile = load_profile()
    TEX_PATH.write_text(generate_tex(profile), encoding="utf-8", newline="\n")
    print(f"Generated {TEX_PATH.relative_to(ROOT)}")
    if not args.generate_only:
        compile_pdf()
        print(f"Generated {PDF_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
