# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T12:37:24.660214+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0158` n `13`; crypto_alt avg `0.0019` n `239`; crypto_major avg `-0.0064` n `8`; equity avg `0.083` n `161`; fx avg `0.0149` n `6`; index avg `0.013` n `27`; metal avg `0.0169` n `20`; unknown avg `0.1001` n `1261`
- 1h: commodity avg `0.0834` n `13`; crypto_alt avg `0.1752` n `239`; crypto_major avg `-0.0539` n `8`; equity avg `0.188` n `161`; fx avg `0.0242` n `6`; index avg `0.0158` n `27`; metal avg `-0.059` n `20`; unknown avg `19.3027` n `1249`
- 4h: commodity avg `0.3602` n `13`; crypto_alt avg `0.45` n `239`; crypto_major avg `0.3315` n `8`; equity avg `0.6184` n `161`; fx avg `0.0142` n `6`; index avg `0.0256` n `27`; metal avg `-0.0243` n `20`; unknown avg `40.8174` n `1233`
- 24h: commodity avg `0.9488` n `13`; crypto_alt avg `-0.4991` n `239`; crypto_major avg `-1.1089` n `8`; equity avg `3.4978` n `161`; fx avg `-0.2007` n `6`; index avg `0.3092` n `27`; metal avg `0.2614` n `20`; unknown avg `0.9748` n `1173`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.2695`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1821`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1413`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
