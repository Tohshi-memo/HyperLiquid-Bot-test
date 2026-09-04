# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T05:07:59.547390+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0374` n `12`; crypto_alt avg `-0.0487` n `232`; crypto_major avg `-0.0026` n `8`; equity avg `0.0937` n `133`; fx avg `-0.0069` n `6`; index avg `0.0155` n `26`; metal avg `-0.0128` n `20`; unknown avg `-0.2689` n `791`
- 1h: commodity avg `-0.0887` n `12`; crypto_alt avg `-0.0939` n `232`; crypto_major avg `0.1071` n `8`; equity avg `0.2684` n `133`; fx avg `-0.0115` n `6`; index avg `0.0444` n `26`; metal avg `0.0511` n `20`; unknown avg `12.4823` n `791`
- 4h: commodity avg `-0.024` n `12`; crypto_alt avg `-0.201` n `232`; crypto_major avg `0.1381` n `8`; equity avg `0.2902` n `133`; fx avg `-0.0016` n `6`; index avg `0.0728` n `26`; metal avg `-0.0214` n `20`; unknown avg `8.7291` n `791`
- 24h: commodity avg `-0.1188` n `12`; crypto_alt avg `2.1468` n `232`; crypto_major avg `4.0782` n `8`; equity avg `1.8178` n `133`; fx avg `-0.1367` n `6`; index avg `0.2997` n `26`; metal avg `0.49` n `20`; unknown avg `23.7621` n `736`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
