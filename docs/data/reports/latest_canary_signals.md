# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T04:07:32.507459+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0143` n `13`; crypto_alt avg `-0.4544` n `239`; crypto_major avg `-0.6028` n `8`; equity avg `-0.2942` n `165`; fx avg `-0.0002` n `6`; index avg `-0.0505` n `27`; metal avg `-0.1056` n `20`; unknown avg `1.674` n `1246`
- 1h: commodity avg `0.0643` n `13`; crypto_alt avg `-0.3404` n `239`; crypto_major avg `-0.1472` n `8`; equity avg `0.3314` n `165`; fx avg `0.0071` n `6`; index avg `-0.0113` n `27`; metal avg `0.086` n `20`; unknown avg `1.6969` n `1252`
- 4h: commodity avg `0.0077` n `13`; crypto_alt avg `-1.8443` n `239`; crypto_major avg `-1.0487` n `8`; equity avg `-0.8954` n `165`; fx avg `0.0039` n `6`; index avg `-0.1599` n `27`; metal avg `-0.6466` n `20`; unknown avg `0.4648` n `1250`
- 24h: commodity avg `0.0342` n `13`; crypto_alt avg `-3.7058` n `239`; crypto_major avg `-2.4363` n `8`; equity avg `-5.8158` n `165`; fx avg `0.0429` n `6`; index avg `-0.5389` n `27`; metal avg `-1.6327` n `20`; unknown avg `75.9716` n `1169`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
