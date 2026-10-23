# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T07:07:34.409778+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0215` n `13`; crypto_alt avg `-0.1126` n `237`; crypto_major avg `-0.1009` n `8`; equity avg `-0.0408` n `152`; fx avg `-0.0138` n `6`; index avg `-0.0161` n `26`; metal avg `-0.0486` n `20`; unknown avg `1.0667` n `1231`
- 1h: commodity avg `-0.0291` n `13`; crypto_alt avg `0.0691` n `237`; crypto_major avg `0.1682` n `8`; equity avg `0.4087` n `152`; fx avg `0.003` n `6`; index avg `0.0271` n `26`; metal avg `-0.0746` n `20`; unknown avg `1.0021` n `1231`
- 4h: commodity avg `0.0149` n `13`; crypto_alt avg `0.3505` n `237`; crypto_major avg `0.246` n `8`; equity avg `1.5071` n `152`; fx avg `0.0035` n `6`; index avg `0.1397` n `26`; metal avg `-0.0035` n `20`; unknown avg `-0.056` n `1204`
- 24h: commodity avg `0.1706` n `13`; crypto_alt avg `-0.2883` n `237`; crypto_major avg `-0.2394` n `8`; equity avg `-1.0167` n `152`; fx avg `-0.0544` n `6`; index avg `-0.0826` n `26`; metal avg `-0.4983` n `20`; unknown avg `52.1765` n `898`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1785`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1556`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1487`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1428`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
