# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T23:07:39.602259+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0002` n `13`; crypto_alt avg `-0.2535` n `236`; crypto_major avg `-0.2829` n `8`; equity avg `-0.1111` n `151`; fx avg `-0.0073` n `6`; index avg `-0.0031` n `26`; metal avg `-0.0077` n `20`; unknown avg `0.1108` n `1134`
- 1h: commodity avg `-0.0746` n `13`; crypto_alt avg `-0.4029` n `236`; crypto_major avg `-0.432` n `8`; equity avg `-0.3442` n `151`; fx avg `-0.0111` n `6`; index avg `-0.0382` n `26`; metal avg `-0.0383` n `20`; unknown avg `0.0124` n `1118`
- 4h: commodity avg `-0.163` n `13`; crypto_alt avg `-0.4339` n `236`; crypto_major avg `-0.3168` n `8`; equity avg `0.461` n `151`; fx avg `-0.0103` n `6`; index avg `0.015` n `26`; metal avg `0.0527` n `20`; unknown avg `-0.1148` n `1020`
- 24h: commodity avg `-0.2516` n `13`; crypto_alt avg `0.3413` n `236`; crypto_major avg `0.4667` n `8`; equity avg `1.0315` n `151`; fx avg `0.1411` n `6`; index avg `0.0158` n `26`; metal avg `0.5008` n `20`; unknown avg `24.9858` n `910`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.0957`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0921`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0873`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0769`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0735`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0705`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0503`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0496`, n `668`, weak_sample_signal
