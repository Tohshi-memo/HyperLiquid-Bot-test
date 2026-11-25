# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T01:07:29.273570+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0281` n `13`; crypto_alt avg `-0.2368` n `239`; crypto_major avg `-0.2344` n `8`; equity avg `-0.3903` n `168`; fx avg `-0.0113` n `6`; index avg `-0.0553` n `27`; metal avg `-0.1383` n `20`; unknown avg `-0.1113` n `1253`
- 1h: commodity avg `0.0123` n `13`; crypto_alt avg `-0.306` n `239`; crypto_major avg `-0.3366` n `8`; equity avg `-0.5025` n `168`; fx avg `-0.0241` n `6`; index avg `-0.0499` n `27`; metal avg `-0.1223` n `20`; unknown avg `163.7305` n `1235`
- 4h: commodity avg `0.024` n `13`; crypto_alt avg `-0.3956` n `239`; crypto_major avg `-0.397` n `8`; equity avg `-0.8737` n `168`; fx avg `0.0195` n `6`; index avg `-0.1106` n `27`; metal avg `-0.1487` n `20`; unknown avg `26.0913` n `1163`
- 24h: commodity avg `0.5552` n `13`; crypto_alt avg `-3.4881` n `239`; crypto_major avg `-3.3516` n `8`; equity avg `-5.7861` n `167`; fx avg `0.1559` n `6`; index avg `-0.5473` n `27`; metal avg `-1.3764` n `20`; unknown avg `498.7601` n `1027`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
