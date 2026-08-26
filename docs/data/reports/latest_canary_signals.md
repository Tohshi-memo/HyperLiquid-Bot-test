# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T11:18:15.455825+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0089` n `12`; crypto_alt avg `0.0514` n `231`; crypto_major avg `-0.141` n `8`; equity avg `0.0401` n `122`; fx avg `0.0027` n `6`; index avg `0.0079` n `25`; metal avg `0.0249` n `20`; unknown avg `0.0524` n `797`
- 1h: commodity avg `0.055` n `12`; crypto_alt avg `0.6145` n `231`; crypto_major avg `0.5892` n `8`; equity avg `0.195` n `122`; fx avg `0.0051` n `6`; index avg `0.0576` n `25`; metal avg `0.0463` n `20`; unknown avg `0.0438` n `797`
- 4h: commodity avg `0.0373` n `12`; crypto_alt avg `0.0305` n `231`; crypto_major avg `0.0937` n `8`; equity avg `0.2025` n `122`; fx avg `-0.0188` n `6`; index avg `0.0185` n `25`; metal avg `-0.0417` n `20`; unknown avg `0.1395` n `797`
- 24h: commodity avg `-0.3034` n `12`; crypto_alt avg `-1.1302` n `231`; crypto_major avg `-0.7574` n `8`; equity avg `0.4476` n `122`; fx avg `-0.0247` n `6`; index avg `0.0097` n `25`; metal avg `0.1613` n `20`; unknown avg `0.7196` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.184`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
