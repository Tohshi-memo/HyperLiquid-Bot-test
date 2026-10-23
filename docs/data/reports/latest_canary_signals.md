# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T22:22:26.855076+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0351` n `13`; crypto_alt avg `-0.2101` n `237`; crypto_major avg `-0.0807` n `8`; equity avg `-0.0231` n `152`; fx avg `0.034` n `6`; index avg `0.0041` n `26`; metal avg `0.0005` n `20`; unknown avg `0.4945` n `1230`
- 1h: commodity avg `0.0765` n `13`; crypto_alt avg `-0.225` n `237`; crypto_major avg `-0.1129` n `8`; equity avg `-0.0242` n `152`; fx avg `0.0365` n `6`; index avg `-0.0055` n `26`; metal avg `-0.0072` n `20`; unknown avg `0.8013` n `1220`
- 4h: commodity avg `0.1679` n `13`; crypto_alt avg `-1.2777` n `237`; crypto_major avg `-0.4665` n `8`; equity avg `-0.2932` n `152`; fx avg `0.0379` n `6`; index avg `-0.0063` n `26`; metal avg `-0.0538` n `20`; unknown avg `-0.164` n `1134`
- 24h: commodity avg `0.5097` n `13`; crypto_alt avg `0.2114` n `237`; crypto_major avg `0.3725` n `8`; equity avg `1.2755` n `152`; fx avg `-0.0172` n `6`; index avg `0.068` n `26`; metal avg `-0.1658` n `20`; unknown avg `-0.2444` n `1012`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1993`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1808`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1525`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1449`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
