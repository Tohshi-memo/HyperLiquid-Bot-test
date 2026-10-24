# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T01:56:13.567506+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0818` n `13`; crypto_alt avg `0.4936` n `237`; crypto_major avg `0.3928` n `8`; equity avg `0.1439` n `152`; fx avg `0.0038` n `6`; index avg `0.0144` n `26`; metal avg `0.017` n `20`; unknown avg `0.509` n `1230`
- 1h: commodity avg `-0.1089` n `13`; crypto_alt avg `0.4874` n `237`; crypto_major avg `0.3701` n `8`; equity avg `0.1582` n `152`; fx avg `0.0024` n `6`; index avg `0.0192` n `26`; metal avg `0.0212` n `20`; unknown avg `4.0912` n `1230`
- 4h: commodity avg `-0.0466` n `13`; crypto_alt avg `-0.629` n `237`; crypto_major avg `-0.5637` n `8`; equity avg `-0.1042` n `152`; fx avg `-0.0057` n `6`; index avg `-0.0332` n `26`; metal avg `-0.0483` n `20`; unknown avg `16.6242` n `1210`
- 24h: commodity avg `0.3335` n `13`; crypto_alt avg `-1.1197` n `237`; crypto_major avg `-0.7324` n `8`; equity avg `0.597` n `152`; fx avg `-0.0386` n `6`; index avg `0.0536` n `26`; metal avg `-0.018` n `20`; unknown avg `205.1792` n `1018`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1945`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1818`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.15`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1413`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
