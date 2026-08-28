# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T21:52:22.796507+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0053` n `12`; crypto_alt avg `-0.4756` n `231`; crypto_major avg `-0.396` n `8`; equity avg `0.0309` n `127`; fx avg `0.0518` n `6`; index avg `-0.0004` n `26`; metal avg `0.0014` n `20`; unknown avg `-0.1504` n `793`
- 1h: commodity avg `0.031` n `12`; crypto_alt avg `-0.4286` n `231`; crypto_major avg `-0.2577` n `8`; equity avg `-0.0128` n `127`; fx avg `0.0699` n `6`; index avg `-0.0111` n `26`; metal avg `0.0073` n `20`; unknown avg `0.0492` n `793`
- 4h: commodity avg `0.0058` n `12`; crypto_alt avg `-0.7558` n `231`; crypto_major avg `-0.9232` n `8`; equity avg `-0.1624` n `127`; fx avg `0.0207` n `6`; index avg `-0.0501` n `26`; metal avg `-0.1453` n `20`; unknown avg `-0.3431` n `793`
- 24h: commodity avg `-0.0843` n `12`; crypto_alt avg `-3.6041` n `231`; crypto_major avg `-3.6641` n `8`; equity avg `-2.0543` n `127`; fx avg `-0.0799` n `6`; index avg `-0.201` n `26`; metal avg `-0.3474` n `20`; unknown avg `-0.5623` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
