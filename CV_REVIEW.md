# Academic CV revision notes

The revised PDF is generated from `static/uploads/academic-cv.md` with `python3 scripts/build_academic_cv.py`. The existing homepage download URL remains `uploads/resume.pdf`.

## Editorial changes

- Reorganized the resume as an academic CV with research interests, education, detailed research experience, separate publications/manuscript/patent sections, and concise professional experience.
- Removed the full street address, extracurricular descriptions, hobbies, and undated test scores. Test scores can be added to application forms with test dates and validity confirmed.
- Retained metrics from the original PDF without independently validating experiments; avoided adding new findings, supervision, funding, author details, or clinical claims.
- Omitted patent identifiers because both distinct inventions have the same number in the source. No granted status is asserted.
- Avoided assigning the ASL 98.7% result to a particular architecture because the original PDF says ResNet50 while the project page says Swin Transformer.
- Kept the original PDF's employment and research dates rather than inferring new dates from an open-ended web profile.

## Confirm before sending to supervisors

1. **Degrees:** Confirm the exact English degree and program names on all diplomas. UF is MEng in the PDF but MS in the profile; its department name is normalized to Electrical and Computer Engineering in the revision.
2. **Employment:** Confirm Morriox title and start month (original PDF: Web Developer, Aug 2025). Confirm UF research end month (PDF: May 2025; profile: ongoing), and whether the Tsinghua role was formally Research Assistant.
3. **ASL evaluation:** Confirm the model achieving 98.7%, split sizes, subject/session independence, and whether augmentation occurred only after splitting. Confirm what the throughput comparison measured.
4. **MRI evaluation:** Confirm dataset, target structures, split, precise architecture integration, and whether 1.7 refers to absolute Dice percentage points on a 0-100 scale. nnU-Net and Swin-UNet should not be described as a hybrid without the implementation details supporting it.
5. **FER results:** Confirm baseline and evaluation dataset for the 7 percentage point gain and 90.3% result. Confirm 150 participants versus number of collected images, and consent/use permissions if relevant to the application discussion.
6. **Publication:** Verify full author list, official English journal title, year, volume, issue, pages, and DOI against the published paper. The PDF gives an abbreviated author list and the website gives three authors.
7. **Submitted manuscript:** Confirm current status; retain 'submitted' only if the submission is still active. Do not count it as a published paper.
8. **Patents:** Supply separate correct application/publication numbers, complete inventor order, filing dates, and current legal status. Titles currently follow the original English translations; verify against the actual documents.
9. **GPA and honors:** Confirm undergraduate GPA (PDF: 84.6; profile: 84.7) and the stated award percentiles. Confirm whether the UF GPA is rounded.

Website discrepancies are documented here; the website biography, project pages, and publication records have not been rewritten as part of this focused CV revision.
