# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-21T01:52:28.757007+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0338` n `13`; crypto_alt avg `0.5035` n `237`; crypto_major avg `0.4365` n `8`; equity avg `0.1816` n `151`; fx avg `-0.0013` n `6`; index avg `0.0549` n `26`; metal avg `-0.0392` n `20`; unknown avg `1.2871` n `1199`
- 1h: commodity avg `0.1258` n `13`; crypto_alt avg `0.2998` n `237`; crypto_major avg `0.136` n `8`; equity avg `0.0817` n `151`; fx avg `0.0315` n `6`; index avg `0.0519` n `26`; metal avg `-0.0637` n `20`; unknown avg `0.5168` n `1197`
- 4h: commodity avg `0.1311` n `13`; crypto_alt avg `0.5013` n `237`; crypto_major avg `0.3956` n `8`; equity avg `0.6473` n `151`; fx avg `0.003` n `6`; index avg `0.0821` n `26`; metal avg `-0.0996` n `20`; unknown avg `-0.0249` n `1119`
- 24h: commodity avg `0.0291` n `13`; crypto_alt avg `3.2148` n `237`; crypto_major avg `2.3902` n `8`; equity avg `2.5464` n `151`; fx avg `0.0576` n `6`; index avg `0.3441` n `26`; metal avg `0.0737` n `20`; unknown avg `211.9096` n `988`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1721`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
