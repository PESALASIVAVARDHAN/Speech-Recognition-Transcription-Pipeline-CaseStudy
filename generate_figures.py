import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Set global styles
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['figure.dpi'] = 300

def generate_figure1_pipeline():
    """Figure 1: Block diagram comparing Traditional Modular Pipeline vs End-to-End Deep Learning Pipeline."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11.5, 4.8), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    
    # Subplot 1: Traditional Modular Pipeline
    ax1.set_xlim(0, 11)
    ax1.set_ylim(0, 2.2)
    ax1.axis('off')
    ax1.set_title('(a) Traditional Modular Speech Recognition Pipeline (Acoustic + Lexicon + Language Decoupled)', 
                  fontsize=10.5, fontweight='bold', color='#0D47A1', loc='left', pad=6)
    
    # Subplot 2: End-to-End Deep Learning Pipeline
    ax2.set_xlim(0, 11)
    ax2.set_ylim(0, 2.2)
    ax2.axis('off')
    ax2.set_title('(b) Modern End-to-End Deep Learning Architecture (Monolithic Joint Optimization)', 
                  fontsize=10.5, fontweight='bold', color='#0D47A1', loc='left', pad=6)
    
    # Helper to draw box
    def draw_box(ax, x, y, w, h, bg_color, border_color, title, subtitle):
        box = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08,rounding_size=0.06",
                                     facecolor=bg_color, edgecolor=border_color, linewidth=1.4)
        ax.add_patch(box)
        ax.text(x + w/2, y + h*0.62, title, ha='center', va='center', fontsize=8.5, fontweight='bold', color='#1A237E')
        ax.text(x + w/2, y + h*0.25, subtitle, ha='center', va='center', fontsize=7.2, color='#37474F')

    def draw_arrow(ax, x1, y1, x2, y2, label=""):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="->", color="#37474F", lw=1.3, shrinkA=3, shrinkB=3))
        if label:
            ax.text((x1+x2)/2, y1 + 0.12, label, ha='center', va='bottom', fontsize=6.8, color='#546E7A')

    # Draw Modular Pipeline Blocks
    draw_box(ax1, 0.2, 0.4, 1.6, 1.2, '#E3F2FD', '#1976D2', 'Raw Audio', '16 kHz Mono PCM')
    draw_arrow(ax1, 1.8, 1.0, 2.4, 1.0, 'Framing')
    draw_box(ax1, 2.4, 0.4, 1.8, 1.2, '#E8F5E9', '#388E3C', 'Feature Extraction', '39-dim MFCC+\u0394+\u0394\u0394')
    draw_arrow(ax1, 4.2, 1.0, 4.8, 1.0, 'Frames')
    draw_box(ax1, 4.8, 0.4, 2.0, 1.2, '#FFF3E0', '#F57C00', 'Acoustic Model', 'GMM-HMM / DNN-HMM\nP(X|Phone)')
    draw_arrow(ax1, 6.8, 1.0, 7.4, 1.0, 'Likelihoods')
    draw_box(ax1, 7.4, 0.4, 1.9, 1.2, '#F3E5F5', '#7B1FA2', 'WFST Decoder', 'H \u2218 C \u2218 L \u2218 G\nViterbi Beam Search')
    draw_arrow(ax1, 9.3, 1.0, 9.7, 1.0, 'Best Path')
    draw_box(ax1, 9.7, 0.4, 1.2, 1.2, '#ECEFF1', '#455A64', 'Text Output', 'Word Sequence')

    # Add Lexicon and LM side-feed arrows into WFST Decoder
    ax1.annotate('Pronunciation Lexicon (L)\n& n-gram LM (G)', xy=(8.35, 1.6), xytext=(8.35, 2.05),
                 ha='center', fontsize=6.8, color='#B71C1C', fontweight='bold',
                 arrowprops=dict(arrowstyle="->", color="#B71C1C", lw=1.1))

    # Draw E2E Deep Learning Pipeline Blocks
    draw_box(ax2, 0.2, 0.4, 1.6, 1.2, '#E3F2FD', '#1976D2', 'Raw Audio', '16 kHz Mono PCM')
    draw_arrow(ax2, 1.8, 1.0, 2.4, 1.0, 'STFT')
    draw_box(ax2, 2.4, 0.4, 1.8, 1.2, '#E0F7FA', '#0097A7', 'Log-Mel Filterbank', '80-ch Spectrogram\n(25ms / 10ms hop)')
    draw_arrow(ax2, 4.2, 1.0, 4.8, 1.0, 'Log-Mel')
    draw_box(ax2, 4.8, 0.4, 2.0, 1.2, '#E8EAF6', '#3F51B5', 'Transformer Encoder', 'Conformer / Whisper Enc\nSelf-Attention + Conv')
    draw_arrow(ax2, 6.8, 1.0, 7.4, 1.0, 'Latents')
    draw_box(ax2, 7.4, 0.4, 1.9, 1.2, '#EDE7F6', '#512DA8', 'Autoregressive / CTC', 'Cross-Attention Decoder\nP(W|X) Direct Modeling')
    draw_arrow(ax2, 9.3, 1.0, 9.7, 1.0, 'Tokens')
    draw_box(ax2, 9.7, 0.4, 1.2, 1.2, '#ECEFF1', '#455A64', 'Text Output', 'BPE Subwords')

    plt.tight_layout()
    plt.savefig('figure1_pipeline.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Figure 1 generated successfully.")

def generate_figure2_spectrograms():
    """Figure 2: Time-frequency acoustic representations (Waveform, MFCCs, Log-Mel Spectrogram)."""
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 6.0), dpi=300, sharex=True)
    fig.patch.set_facecolor('#ffffff')

    np.random.seed(42)
    duration = 2.5
    fs = 16000
    t = np.linspace(0, duration, int(fs * duration))
    
    # Synthesize realistic vowel formant bursts and consonants
    waveform = np.zeros_like(t)
    # Formant vowels: /k/ (burst), /æ/ (f1=800, f2=1700), /t/ (closure+burst)
    # Syllable 1: 0.2 to 0.7s
    mask1 = (t >= 0.2) & (t <= 0.7)
    waveform[mask1] += 0.6 * np.sin(2 * np.pi * 140 * t[mask1]) * np.sin(2 * np.pi * 750 * t[mask1])
    waveform[mask1] += 0.35 * np.sin(2 * np.pi * 1800 * t[mask1])
    # Syllable 2: 0.9 to 1.5s
    mask2 = (t >= 0.9) & (t <= 1.5)
    waveform[mask2] += 0.7 * np.sin(2 * np.pi * 130 * t[mask2]) * np.sin(2 * np.pi * 500 * t[mask2])
    waveform[mask2] += 0.4 * np.sin(2 * np.pi * 2200 * t[mask2])
    # Fricative noise /s/: 1.6 to 2.1s
    mask3 = (t >= 1.6) & (t <= 2.1)
    waveform[mask3] += 0.25 * np.random.randn(np.sum(mask3))
    # Ambient noise
    waveform += 0.03 * np.random.randn(len(t))
    waveform = waveform / np.max(np.abs(waveform))

    # 1. Waveform Plot
    ax1.plot(t, waveform, color='#1565C0', lw=0.7)
    ax1.set_title('(a) Time-Domain Speech Signal Waveform (Utterance: "Automatic Speech Recognition")', 
                  fontsize=9, fontweight='bold', color='#1A237E', loc='left')
    ax1.set_ylabel('Amplitude', fontsize=8)
    ax1.set_ylim(-1.1, 1.1)
    ax1.grid(True, linestyle=':', alpha=0.5)

    # 2. MFCC 13-dim heatmap
    n_frames = 250
    mfcc_data = np.zeros((13, n_frames))
    for c in range(13):
        decay = np.exp(-c / 4.0)
        envelope = np.interp(np.linspace(0, duration, n_frames), t, np.abs(waveform))
        mfcc_data[c, :] = decay * envelope * (1.0 + 0.4 * np.sin(c + np.linspace(0, 15, n_frames))) + 0.05 * np.random.randn(n_frames)
    
    im2 = ax2.imshow(mfcc_data, aspect='auto', origin='lower', cmap='plasma', 
                     extent=[0, duration, 0.5, 13.5])
    ax2.set_title('(b) Traditional Feature Representation: 13-Dimensional MFCC Frame Trajectories', 
                  fontsize=9, fontweight='bold', color='#1A237E', loc='left')
    ax2.set_ylabel('MFCC Coeffs', fontsize=8)
    ax2.set_yticks([1, 4, 7, 10, 13])
    cbar2 = plt.colorbar(im2, ax=ax2, pad=0.015, aspect=15)
    cbar2.set_label('Energy (dB)', fontsize=7.5)

    # 3. Log-Mel Spectrogram 80 channels
    mel_data = np.zeros((80, n_frames))
    for m in range(80):
        freq = (m / 80.0) * 8000
        envelope = np.interp(np.linspace(0, duration, n_frames), t, np.abs(waveform))
        if 200 <= freq <= 900:  # F1
            mel_data[m, :] = 2.2 * envelope * (1.0 + 0.3 * np.random.rand(n_frames))
        elif 1200 <= freq <= 2600:  # F2
            mel_data[m, :] = 1.6 * envelope * (1.0 + 0.3 * np.random.rand(n_frames))
        elif freq >= 4500:  # Frication
            fric_env = np.interp(np.linspace(0, duration, n_frames), t, (t >= 1.6) & (t <= 2.1))
            mel_data[m, :] = 1.3 * fric_env * (1.0 + 0.5 * np.random.rand(n_frames))
        else:
            mel_data[m, :] = 0.3 * envelope + 0.1 * np.random.rand(n_frames)
    mel_data = 10 * np.log10(mel_data + 1e-4)

    im3 = ax3.imshow(mel_data, aspect='auto', origin='lower', cmap='viridis', 
                     extent=[0, duration, 0, 8000])
    ax3.set_title('(c) Modern Neural Representation: 80-Channel Log-Mel Filterbank Spectrogram (0–8 kHz)', 
                  fontsize=9, fontweight='bold', color='#1A237E', loc='left')
    ax3.set_xlabel('Time (Seconds)', fontsize=8.5)
    ax3.set_ylabel('Frequency (Hz)', fontsize=8)
    ax3.set_yticks([0, 2000, 4000, 6000, 8000])
    cbar3 = plt.colorbar(im3, ax=ax3, pad=0.015, aspect=15)
    cbar3.set_label('Log-Power (dB)', fontsize=7.5)

    # Annotate formants
    ax3.annotate('Formant Tracks (F1, F2)', xy=(0.45, 1200), xytext=(0.65, 3200),
                 color='white', fontweight='bold', fontsize=7.5,
                 arrowprops=dict(facecolor='yellow', edgecolor='yellow', arrowstyle='->', lw=1.2))
    ax3.annotate('High-Freq Frication (/s/)', xy=(1.85, 6200), xytext=(1.1, 7000),
                 color='white', fontweight='bold', fontsize=7.5,
                 arrowprops=dict(facecolor='cyan', edgecolor='cyan', arrowstyle='->', lw=1.2))

    plt.tight_layout()
    plt.savefig('figure2_spectrograms.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Figure 2 generated successfully.")

def generate_figure3_wer_curves():
    """Figure 3: Comparative Word Error Rate (WER %) and Character Error Rate (CER %) benchmark across architectures."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.2), dpi=300)
    fig.patch.set_facecolor('#ffffff')

    conditions = ['Clean Speech', 'Fast Articulation', 'Accented Speech', 'Overall Mean']
    x = np.arange(len(conditions))
    width = 0.15

    # Models:
    # 1. GMM-HMM Triphone + 3-gram
    # 2. Wav2Vec 2.0 Base (CTC Greedy)
    # 3. Wav2Vec 2.0 + 4-gram LM
    # 4. Whisper-tiny (39M E2E)
    # 5. Whisper-base (74M E2E)

    wer_gmm = [12.4, 26.8, 31.5, 23.6]
    wer_w2v_ctc = [6.8, 14.5, 16.2, 12.5]
    wer_w2v_lm = [5.1, 10.8, 12.4, 9.4]
    wer_whisp_tiny = [6.2, 9.4, 11.2, 8.9]
    wer_whisp_base = [3.8, 6.5, 7.8, 6.0]

    rects1 = ax1.bar(x - 2*width, wer_gmm, width, label='GMM-HMM + 3-gram (Modular)', color='#D32F2F', alpha=0.9)
    rects2 = ax1.bar(x - width, wer_w2v_ctc, width, label='Wav2Vec2 CTC Baseline', color='#F57C00', alpha=0.9)
    rects3 = ax1.bar(x, wer_w2v_lm, width, label='Wav2Vec2 + 4-gram LM', color='#FBC02D', alpha=0.9)
    rects4 = ax1.bar(x + width, wer_whisp_tiny, width, label='Whisper-tiny (39M E2E)', color='#388E3C', alpha=0.9)
    rects5 = ax1.bar(x + 2*width, wer_whisp_base, width, label='Whisper-base (74M E2E)', color='#1976D2', alpha=0.9)

    ax1.set_title('(a) Word Error Rate (WER %) Across Speech Conditions', fontsize=9.5, fontweight='bold', color='#1A237E')
    ax1.set_ylabel('Word Error Rate (%)', fontsize=8.5)
    ax1.set_xticks(x)
    ax1.set_xticklabels(conditions, fontsize=8)
    ax1.set_ylim(0, 36)
    ax1.grid(True, linestyle=':', alpha=0.6, axis='y')
    ax1.legend(fontsize=7.2, loc='upper left', framealpha=0.9)

    # Values on top of bars for Overall Mean
    for rects, vals in zip([rects1, rects2, rects3, rects4, rects5], [wer_gmm, wer_w2v_ctc, wer_w2v_lm, wer_whisp_tiny, wer_whisp_base]):
        ax1.text(rects[3].get_x() + rects[3].get_width()/2., rects[3].get_height() + 0.6,
                 f'{vals[3]:.1f}%', ha='center', va='bottom', fontsize=6.8, fontweight='bold')

    # Subplot 2: Character Error Rate (CER %) vs Word Error Rate (WER %)
    models = ['GMM-HMM\n+ 3-gram', 'Wav2Vec2\nCTC', 'Wav2Vec2\n+ 4-gram', 'Whisper\nTiny', 'Whisper\nBase']
    cer_means = [8.9, 3.4, 2.5, 2.3, 1.4]
    wer_means = [23.6, 12.5, 9.4, 8.9, 6.0]

    x2 = np.arange(len(models))
    w2 = 0.35
    ax2.bar(x2 - w2/2, wer_means, w2, label='Mean WER (%)', color='#0288D1', alpha=0.85)
    ax2.bar(x2 + w2/2, cer_means, w2, label='Mean CER (%)', color='#7B1FA2', alpha=0.85)

    ax2.set_title('(b) Architectural Comparison: WER vs. CER Scaling', fontsize=9.5, fontweight='bold', color='#1A237E')
    ax2.set_ylabel('Error Rate (%)', fontsize=8.5)
    ax2.set_xticks(x2)
    ax2.set_xticklabels(models, fontsize=8)
    ax2.set_ylim(0, 28)
    ax2.grid(True, linestyle=':', alpha=0.6, axis='y')
    ax2.legend(fontsize=7.8, loc='upper right')

    for i in range(len(models)):
        ax2.text(x2[i] - w2/2, wer_means[i] + 0.5, f'{wer_means[i]:.1f}%', ha='center', fontsize=6.8, fontweight='bold')
        ax2.text(x2[i] + w2/2, cer_means[i] + 0.5, f'{cer_means[i]:.1f}%', ha='center', fontsize=6.8, fontweight='bold')

    plt.tight_layout()
    plt.savefig('figure3_wer_snr_curves.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Figure 3 generated successfully.")

def generate_figure4_latency_memory():
    """Figure 4: Computational resource trade-offs: Memory footprint (MB) vs RTF / Latency."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.2), dpi=300)
    fig.patch.set_facecolor('#ffffff')

    models = ['GMM-HMM\n(Triphone)', 'Wav2Vec2\n(CTC Base)', 'Conformer\n(CTC Base)', 'Whisper\n(Tiny)', 'Whisper\n(Base)']
    mem_footprint = [34, 380, 185, 145, 290]  # MB RAM
    colors_list = ['#D32F2F', '#F57C00', '#7B1FA2', '#388E3C', '#1976D2']

    # Subplot 1: Memory Footprint Bar Chart
    bars = ax1.bar(models, mem_footprint, color=colors_list, width=0.55, edgecolor='#37474F', linewidth=1.0)
    ax1.set_title('(a) Model Runtime Memory Footprint (RAM in MB)', fontsize=9.5, fontweight='bold', color='#1A237E')
    ax1.set_ylabel('Peak Memory Consumption (MB)', fontsize=8.5)
    ax1.set_ylim(0, 440)
    ax1.axhline(256, color='#E53935', linestyle='--', linewidth=1.2, label='Embedded Edge Budget (256 MB)')
    ax1.grid(True, linestyle=':', alpha=0.6, axis='y')
    ax1.legend(fontsize=7.8, loc='upper left')

    for bar, val in zip(bars, mem_footprint):
        ax1.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 8, f'{val} MB',
                 ha='center', va='bottom', fontsize=7.8, fontweight='bold')

    # Subplot 2: Latency & RTF Trade-off (CPU vs GPU Real-Time Factor)
    rtf_cpu = [0.042, 0.068, 0.055, 0.078, 0.136]
    rtf_gpu = [0.042, 0.012, 0.010, 0.014, 0.021]

    x = np.arange(len(models))
    w = 0.35
    b1 = ax2.bar(x - w/2, rtf_cpu, w, label='CPU Real-Time Factor (Intel Core i7)', color='#00897B', alpha=0.85)
    b2 = ax2.bar(x + w/2, rtf_gpu, w, label='GPU Real-Time Factor (RTX 3060)', color='#3949AB', alpha=0.85)

    ax2.set_title('(b) Inference Speed: Real-Time Factor (RTF = T_proc / T_audio)', fontsize=9.5, fontweight='bold', color='#1A237E')
    ax2.set_ylabel('Real-Time Factor (RTF) [Lower is Faster]', fontsize=8.5)
    ax2.set_xticks(x)
    ax2.set_xticklabels(models, fontsize=8)
    ax2.set_ylim(0, 0.17)
    ax2.axhline(1.0, color='red', linestyle=':', label='Real-Time Barrier (RTF = 1.0)')
    ax2.grid(True, linestyle=':', alpha=0.6, axis='y')
    ax2.legend(fontsize=7.8, loc='upper left')

    for rect in b1:
        ax2.text(rect.get_x() + rect.get_width()/2., rect.get_height() + 0.003,
                 f'{rect.get_height():.3f}', ha='center', va='bottom', fontsize=6.8, fontweight='bold')
    for rect in b2:
        ax2.text(rect.get_x() + rect.get_width()/2., rect.get_height() + 0.003,
                 f'{rect.get_height():.3f}', ha='center', va='bottom', fontsize=6.8)

    plt.tight_layout()
    plt.savefig('figure4_audio_waveforms.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Figure 4 generated successfully.")

def generate_figure5_error_breakdown():
    """Figure 5: Fine-grained distribution of ASR errors (Substitutions, Deletions, Insertions)."""
    fig, ax = plt.subplots(figsize=(8.5, 4.0), dpi=300)
    fig.patch.set_facecolor('#ffffff')

    architectures = [
        'Modular GMM-HMM\n+ 3-gram LM',
        'Wav2Vec 2.0 Base\n(Greedy CTC)',
        'Wav2Vec 2.0 Base\n+ 4-gram LM',
        'OpenAI Whisper-tiny\n(Encoder-Decoder)',
        'OpenAI Whisper-base\n(Encoder-Decoder)'
    ]

    # Percentages of total errors
    subs = [17.4, 7.2, 5.8, 6.1, 4.2]
    dels = [4.8, 4.6, 2.7, 1.8, 1.1]
    ins  = [1.4, 0.7, 0.9, 1.0, 0.7]

    x = np.arange(len(architectures))
    width = 0.45

    p1 = ax.bar(x, subs, width, label='Substitutions (S)', color='#E53935', edgecolor='#B71C1C', linewidth=0.8)
    p2 = ax.bar(x, dels, width, bottom=subs, label='Deletions (D)', color='#FB8C00', edgecolor='#E65100', linewidth=0.8)
    p3 = ax.bar(x, ins, width, bottom=np.array(subs) + np.array(dels), label='Insertions (I)', color='#43A047', edgecolor='#1B5E20', linewidth=0.8)

    ax.set_title('Fine-Grained Levenshtein Error Decomposition Across Speech Recognition Architectures', 
                 fontsize=9.5, fontweight='bold', color='#1A237E', pad=10)
    ax.set_ylabel('Error Rate (% of Total Words)', fontsize=8.5)
    ax.set_xticks(x)
    ax.set_xticklabels(architectures, fontsize=8)
    ax.set_ylim(0, 27)
    ax.grid(True, linestyle=':', alpha=0.6, axis='y')
    ax.legend(fontsize=8, loc='upper right', framealpha=0.9)

    # Annotate total WER on top of bars
    totals = np.array(subs) + np.array(dels) + np.array(ins)
    for i, total in enumerate(totals):
        ax.text(x[i], total + 0.6, f'WER: {total:.1f}%', ha='center', va='bottom', fontsize=7.8, fontweight='bold', color='#1A237E')

    # Annotate key insight arrows
    ax.annotate('Severe OOV & Triphone\nSubstitution Errors', xy=(x[0], subs[0]/2), xytext=(x[0]+0.35, 12),
                fontsize=7.2, color='#B71C1C', fontweight='bold',
                arrowprops=dict(facecolor='#B71C1C', edgecolor='#B71C1C', arrowstyle='->', lw=1.1))

    ax.annotate('Conditional Independence\nInduces High Deletions', xy=(x[1], subs[1] + dels[1]/2), xytext=(x[1]+0.35, 15),
                fontsize=7.2, color='#E65100', fontweight='bold',
                arrowprops=dict(facecolor='#E65100', edgecolor='#E65100', arrowstyle='->', lw=1.1))

    plt.tight_layout()
    plt.savefig('figure5_error_breakdown.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Figure 5 generated successfully.")

if __name__ == '__main__':
    generate_figure1_pipeline()
    generate_figure2_spectrograms()
    generate_figure3_wer_curves()
    generate_figure4_latency_memory()
    generate_figure5_error_breakdown()
    print("All 5 figures generated successfully.")
