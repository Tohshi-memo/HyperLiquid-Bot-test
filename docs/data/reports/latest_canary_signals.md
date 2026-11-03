# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T05:22:33.037167+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0001` n `13`; crypto_alt avg `0.0836` n `239`; crypto_major avg `0.0785` n `8`; equity avg `0.0269` n `157`; fx avg `0.0055` n `6`; index avg `0.0105` n `27`; metal avg `0.0004` n `20`; unknown avg `0.3163` n `1264`
- 1h: commodity avg `0.0904` n `13`; crypto_alt avg `-0.0148` n `239`; crypto_major avg `-0.0008` n `8`; equity avg `-0.0824` n `157`; fx avg `0.0156` n `6`; index avg `0.0101` n `27`; metal avg `-0.0399` n `20`; unknown avg `16.7142` n `1248`
- 4h: commodity avg `0.1364` n `13`; crypto_alt avg `-0.4649` n `239`; crypto_major avg `-0.4382` n `8`; equity avg `-0.8395` n `157`; fx avg `-0.0207` n `6`; index avg `-0.1189` n `27`; metal avg `-0.391` n `20`; unknown avg `19.5945` n `1192`
- 24h: commodity avg `-0.7347` n `13`; crypto_alt avg `-2.9786` n `238`; crypto_major avg `-1.9248` n `8`; equity avg `-4.3338` n `157`; fx avg `0.0174` n `6`; index avg `-0.3956` n `27`; metal avg `-0.2459` n `20`; unknown avg `7.918` n `958`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1655`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1622`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1581`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1509`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
