# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T17:38:54.363461+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.07` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0093` n `12`; crypto_alt avg `0.2193` n `228`; crypto_major avg `0.1661` n `8`; equity avg `0.0299` n `65`; fx avg `0.0` n `5`; index avg `0.0132` n `23`; metal avg `-0.0055` n `18`; unknown avg `0.1184` n `376`
- 1h: commodity avg `-0.0116` n `12`; crypto_alt avg `0.6928` n `228`; crypto_major avg `0.3429` n `8`; equity avg `0.1123` n `65`; fx avg `0.0` n `5`; index avg `0.0178` n `23`; metal avg `0.0158` n `18`; unknown avg `0.449` n `376`
- 4h: commodity avg `0.3272` n `12`; crypto_alt avg `0.4052` n `228`; crypto_major avg `0.1444` n `8`; equity avg `0.111` n `65`; fx avg `-0.0011` n `5`; index avg `0.0452` n `23`; metal avg `-0.0209` n `18`; unknown avg `0.0253` n `376`
- 24h: commodity avg `-0.0326` n `12`; crypto_alt avg `1.0966` n `228`; crypto_major avg `0.904` n `8`; equity avg `1.4686` n `65`; fx avg `0.0007` n `5`; index avg `0.356` n `23`; metal avg `-0.1257` n `18`; unknown avg `0.088` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
