# GEMINI.md - Algorithm_26 Project Instructions

이 파일은 `Algorithm_26` 프로젝트 내에서 Gemini CLI의 동작 방식과 개발 원칙을 규정합니다. 모든 작업은 이 지침을 최우선으로 따릅니다.

## 1. 프로젝트 개요 (Project Overview)
이 프로젝트는 2026년 알고리즘 강의를 위한 교육 자료 및 실습 코드를 관리합니다.
- **주요 목적**: 알고리즘 이론 학습, 실습 문제 풀이, 강의 슬라이드 생성 및 관리.
- **주요 기술**:
    - **Python 3.11**: 알고리즘 실습 코드 및 자동화 스크립트 (requests, Upstage API 등 활용).
    - **Slidev (Node.js)**: Markdown 기반의 강의 슬라이드 제작 도구.
    - **Markdown**: 모든 강의 자료 및 설명서 작성.

## 2. Gemini CLI 운영 원칙 (Core Mandates)

### 2.1 작업 범위 및 권한
- **영향 범위**: `Algorithm_26` 디렉토리 내의 모든 하위 폴더와 파일에 대한 접근 및 수정 권한을 가집니다.
- **가상 환경**: 모든 Python 작업은 `algorithm` 이라는 이름의 가상 환경을 사용합니다.
- **설치 및 변경**:
    - 프로젝트 로컬 범위 및 `algorithm` 가상 환경 내에서의 패키지 설치는 자유롭게 수행할 수 있습니다.
    - **단, 유료 옵션 사용이나 시스템 전체(Global)에 영향을 미치는 변경 사항은 반드시 사용자에게 충분히 설명하고 사전에 동의를 구해야 합니다.**

### 2.2 언어 및 기술 표준
- **답변 언어**: 모든 답변과 설명은 **한국어**로 제공합니다.
- **코드 표준**: Python 코드는 **Python 3.11** 버전을 기준으로 작성하며, 최신 문법과 라이브러리 활용을 권장합니다.
- **도구 활용**: Node.js 관련 작업 시 `npm`을 사용하며, `Slidev` 관련 명령어(`dev`, `build`, `export`)를 숙지하여 활용합니다.

## 3. 주요 명령어 (Key Commands)

### 3.1 Slidev (강의 슬라이드)
- **개발 모드 실행**: `npm run dev` (2026-lecture-algorithm 디렉토리 내)
- **빌드**: `npm run build`
- **PDF/이미지 내보내기**: `npm run export`

### 3.2 Python (알고리즘 및 스크립트)
- **가상 환경 활성화**: `conda activate algorithm` 또는 `source algorithm/bin/activate` (환경 구성에 따라 다름)
- **이미지 추출 스크립트**: `python scripts/extract_images.py <pdf_path> <output_dir>`

## 4. 개발 컨벤션 (Development Conventions)
- **문서화**: 강의 자료는 `lectures/weekXX/` 구조에 맞춰 Markdown 형식으로 관리합니다.
- **코드 주석**: 알고리즘 설명 및 복잡도 분석을 주석으로 상세히 기재합니다.
- **이미지 관리**: 교재에서 추출한 이미지는 각 주차의 `images/` 폴더 내에 체계적으로 저장합니다.

---
**주의**: 이 지침은 `Algorithm_26` 프로젝트의 무결성과 효율적인 학습 지원을 위해 작성되었습니다. 모든 작업 시 위 원칙을 준수하십시오.
