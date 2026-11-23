# Speech Recognition & Transcription Pipeline — Case Study

> **Course:** Speech Recognition and Conversational Systems (22AIMLDE24)  
> **Institution:** Jain Deemed-to-be University, Department of CSE (AI & ML)  
> **Option:** C — Traditional Modular Pipelines vs. End-to-End Deep Learning  

---

## 👤 Student Details

| Field | Details |
|-------|---------|
| **Name** | PESALA SIVA VARDHAN REDDY |
| **USN** | 23BTRCL009 |
| **Submission Date** | 23 November 2026 |

---

## 📋 Case Study Topic

**Option C: Traditional Modular Pipelines vs. End-to-End Deep Learning for Speech Recognition**

This case study presents a rigorous comparative analysis between:
- **Traditional Modular Pipelines** — GMM-HMM systems with hand-crafted MFCC features
- **End-to-End Deep Learning Models** — Wav2Vec 2.0 and OpenAI Whisper

Performance is benchmarked across three acoustic conditions (Clean, Noisy @ 10 dB SNR, Far-field) using Word Error Rate (WER), Character Error Rate (CER), Real-Time Factor (RTF), and memory footprint.

---

## 📁 Repository Structure

```
├── 23BTRCL009_PESALA_SIVA_VARDHAN_REDDY_CaseStudy.pdf   # Main submission (15 pages)
├── CaseStudy_Report.md                                   # Full report in Markdown
├── modular_vs_e2e_speech_recognition_experiment.py       # Benchmark experiment script
├── generate_figures.py                                   # Figure generation (Matplotlib)
├── compile_report.py                                     # PDF compilation (ReportLab)
├── benchmark_results.json                                # Benchmark output data
├── requirements.txt                                      # Python dependencies
├── figure1_pipeline.png                                  # Architecture diagram
├── figure2_spectrograms.png                              # Waveform & feature visualization
├── figure3_wer_snr_curves.png                            # WER/CER benchmark bars
├── figure4_audio_waveforms.png                           # Memory & RTF comparison
├── figure5_error_breakdown.png                           # Substitution/Deletion/Insertion breakdown
├── title_logo_0.png                                      # University logo
├── Case_Study_SRCS.pdf                                   # Faculty case study brief
└── Report_Title_Page.pdf                                 # Faculty title page format
```

---

## 📊 Key Findings

| System | WER (Clean) | WER (Noisy) | RTF | Memory |
|--------|-------------|-------------|-----|--------|
| GMM-HMM (Modular) | 18.4% | 42.1% | 0.31× | 180 MB |
| Wav2Vec 2.0 (E2E) | 6.2% | 19.3% | 1.82× | 1.8 GB |
| Whisper-Large (E2E) | 4.1% | 12.7% | 2.14× | 3.1 GB |

**Conclusion:** End-to-end models outperform modular pipelines in accuracy by 50–80% but require significantly more compute. Modular pipelines remain viable for resource-constrained deployments.

---

## 🚀 Running the Experiment

### Prerequisites
```bash
pip install -r requirements.txt
```

### Generate Figures
```bash
python generate_figures.py
```

### Run Benchmark Experiment
```bash
python modular_vs_e2e_speech_recognition_experiment.py
```
Outputs `benchmark_results.json` with WER, CER, RTF, and memory metrics.

### Compile PDF Report
```bash
python compile_report.py
```
Generates `23BTRCL009_PESALA_SIVA_VARDHAN_REDDY_CaseStudy.pdf`.

---

## 📝 Report Structure

1. **Introduction** — Problem context and motivation  
2. **Background & Literature Review** — GMM-HMM, CTC, attention mechanisms  
3. **Methodology** — Dataset, evaluation metrics, experimental setup  
4. **Implementation & Results** — Feature extraction, benchmark results, figures  
5. **Discussion & Analysis** — Trade-offs, error analysis, deployment considerations  
6. **Conclusion & Future Work** — Summary and recommendations  

---

## 📚 References

- Graves, A. et al. (2006). Connectionist Temporal Classification. *ICML.*
- Baevski, A. et al. (2020). wav2vec 2.0. *NeurIPS.*
- Radford, A. et al. (2023). Robust Speech Recognition via Large-Scale Weak Supervision. *ICML.*
- Rabiner, L. R. (1989). A Tutorial on HMMs. *Proceedings of the IEEE.*
- Watanabe, S. et al. (2017). Hybrid CTC/Attention Architecture. *IEEE JSTSP.*

---

*© 2026 PESALA SIVA VARDHAN REDDY | Jain Deemed-to-be University*
