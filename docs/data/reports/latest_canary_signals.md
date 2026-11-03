# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T05:07:28.466444+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0082` n `13`; crypto_alt avg `-0.2225` n `239`; crypto_major avg `-0.1747` n `8`; equity avg `-0.1264` n `157`; fx avg `0.0133` n `6`; index avg `0.0007` n `27`; metal avg `0.0013` n `20`; unknown avg `0.2824` n `1254`
- 1h: commodity avg `0.0917` n `13`; crypto_alt avg `0.133` n `239`; crypto_major avg `0.0446` n `8`; equity avg `-0.2509` n `157`; fx avg `0.0105` n `6`; index avg `-0.0278` n `27`; metal avg `-0.061` n `20`; unknown avg `5.1212` n `1200`
- 4h: commodity avg `0.1093` n `13`; crypto_alt avg `-0.5262` n `239`; crypto_major avg `-0.4908` n `8`; equity avg `-0.8759` n `157`; fx avg `-0.0266` n `6`; index avg `-0.124` n `27`; metal avg `-0.3435` n `20`; unknown avg `-0.3168` n `1192`
- 24h: commodity avg `-0.7653` n `13`; crypto_alt avg `-3.1963` n `238`; crypto_major avg `-2.1391` n `8`; equity avg `-4.3972` n `157`; fx avg `-0.0011` n `6`; index avg `-0.3479` n `27`; metal avg `-0.2065` n `20`; unknown avg `8.1424` n `958`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1654`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1625`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.158`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1513`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
