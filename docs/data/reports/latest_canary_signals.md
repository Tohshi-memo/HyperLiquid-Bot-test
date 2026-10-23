# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T15:07:30.526099+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0495` n `13`; crypto_alt avg `-0.233` n `237`; crypto_major avg `-0.224` n `8`; equity avg `-0.2219` n `152`; fx avg `-0.0116` n `6`; index avg `-0.0281` n `26`; metal avg `-0.0147` n `20`; unknown avg `0.2187` n `1231`
- 1h: commodity avg `-0.1045` n `13`; crypto_alt avg `-0.1415` n `237`; crypto_major avg `-0.213` n `8`; equity avg `0.3258` n `152`; fx avg `0.007` n `6`; index avg `0.0893` n `26`; metal avg `0.0112` n `20`; unknown avg `0.1062` n `1229`
- 4h: commodity avg `-0.098` n `13`; crypto_alt avg `0.2192` n `237`; crypto_major avg `0.2791` n `8`; equity avg `0.2759` n `152`; fx avg `0.0108` n `6`; index avg `0.0778` n `26`; metal avg `-0.0842` n `20`; unknown avg `-0.2308` n `1161`
- 24h: commodity avg `0.2209` n `13`; crypto_alt avg `0.8137` n `237`; crypto_major avg `0.3686` n `8`; equity avg `0.2313` n `152`; fx avg `-0.0541` n `6`; index avg `0.0385` n `26`; metal avg `-0.2846` n `20`; unknown avg `-0.436` n `992`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1932`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.157`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1431`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
