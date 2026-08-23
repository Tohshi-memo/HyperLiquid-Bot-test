# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T09:07:25.441950+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0065` n `12`; crypto_alt avg `0.2729` n `230`; crypto_major avg `-0.026` n `8`; equity avg `-0.0103` n `121`; fx avg `0.0064` n `6`; index avg `0.0001` n `25`; metal avg `-0.0004` n `20`; unknown avg `-0.0415` n `794`
- 1h: commodity avg `-0.0406` n `12`; crypto_alt avg `0.5821` n `230`; crypto_major avg `0.3276` n `8`; equity avg `0.0279` n `121`; fx avg `-0.0032` n `6`; index avg `0.0037` n `25`; metal avg `-0.0083` n `20`; unknown avg `0.013` n `794`
- 4h: commodity avg `-0.0165` n `12`; crypto_alt avg `2.3323` n `230`; crypto_major avg `1.0142` n `8`; equity avg `0.0582` n `121`; fx avg `-0.0354` n `6`; index avg `-0.0135` n `25`; metal avg `0.0041` n `20`; unknown avg `0.5665` n `778`
- 24h: commodity avg `-0.0289` n `12`; crypto_alt avg `-1.191` n `230`; crypto_major avg `-0.0625` n `8`; equity avg `0.1836` n `121`; fx avg `0.0619` n `6`; index avg `0.0117` n `25`; metal avg `0.0508` n `20`; unknown avg `2.6431` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
