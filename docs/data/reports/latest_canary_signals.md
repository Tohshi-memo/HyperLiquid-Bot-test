# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T01:52:31.134445+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.079` n `13`; crypto_alt avg `0.4603` n `237`; crypto_major avg `0.3733` n `8`; equity avg `0.1458` n `152`; fx avg `0.0038` n `6`; index avg `0.0134` n `26`; metal avg `0.0171` n `20`; unknown avg `0.4987` n `1230`
- 1h: commodity avg `-0.1062` n `13`; crypto_alt avg `0.4542` n `237`; crypto_major avg `0.3505` n `8`; equity avg `0.1601` n `152`; fx avg `0.0024` n `6`; index avg `0.0182` n `26`; metal avg `0.0213` n `20`; unknown avg `4.0071` n `1230`
- 4h: commodity avg `-0.0438` n `13`; crypto_alt avg `-0.6615` n `237`; crypto_major avg `-0.583` n `8`; equity avg `-0.1023` n `152`; fx avg `-0.0057` n `6`; index avg `-0.0342` n `26`; metal avg `-0.0482` n `20`; unknown avg `16.5641` n `1210`
- 24h: commodity avg `0.3363` n `13`; crypto_alt avg `-1.1519` n `237`; crypto_major avg `-0.7518` n `8`; equity avg `0.599` n `152`; fx avg `-0.0386` n `6`; index avg `0.0526` n `26`; metal avg `-0.0179` n `20`; unknown avg `205.1125` n `1018`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1945`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1818`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1501`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
