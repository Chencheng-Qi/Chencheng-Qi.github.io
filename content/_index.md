---
# Leave the homepage title empty to use the site title
title: ''
date: 2022-10-24
type: landing

design:
  # Default section spacing
  spacing: '6rem'

sections:
  # ─────────────────────────────
  # 1. 个人简介 + 下载简历
  # ─────────────────────────────
  - block: resume-biography-3
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: admin
      text: ''
      # Show a call-to-action button under your biography (optional)
      button:
        text: Download CV
        url: uploads/resume.pdf
      headings:
        about: ''
        education: ''
        interests: ''
    design:
      # Apply a gradient background
      css_class: hbx-bg-gradient
      # Avatar customization
      avatar:
        size: medium   # small, medium, large, xl, xxl
        shape: circle  # circle, square, rounded

  # ─────────────────────────────
  # 2. My Research（研究方向介绍）
  # ─────────────────────────────
  - block: markdown
    content:
      title: '📚 My Research'
      subtitle: ''
      text: |-
        My research focuses on Machine Learning, Computer Vision, and multimodal signal processing. I work on building reliable and efficient learning systems for visual understanding and healthcare-related applications. My recent projects include developing attention-enhanced deep learning models for American Sign Language recognition, improving 3D brain MRI segmentation using hybrid Swin-UNet architectures, and designing robust methods for facial expression recognition under mask occlusion. I have also explored non-contact physiological signal analysis, such as heart-rate estimation from facial video using FastICA and ICEEMDAN.

        Overall, I aim to create machine learning methods that are accurate, interpretable, and deployable in real-world human-centered scenarios 😃
    design:
      columns: '1'

  # ─────────────────────────────
  # 3. Featured Publications（精选论文）
  # ─────────────────────────────
 # - block: collection
 #   id: papers
 #   content:
 #     title: Featured Publications
 #     subtitle: ''
 #     text: ''
 #     filters:
 #       folders:
 #         - publications
 #       featured_only: true
 #   design:
 #     view: article-grid
 #     columns: 2

  # ─────────────────────────────
  # 4. Recent Publications（最近论文）
  # ─────────────────────────────
  - block: collection
    id: recent-publications
    content:
      title: Papers
      subtitle: ''
      text: ''
      filters:
        folders:
          - publications
        exclude_featured: true
    design:
      view: citation
---
