# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T01:57:28.353587+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0392` n `13`; crypto_alt avg `-0.0257` n `239`; crypto_major avg `-0.0845` n `8`; equity avg `-0.1374` n `162`; fx avg `-0.0069` n `6`; index avg `-0.0116` n `27`; metal avg `-0.0499` n `20`; unknown avg `0.0427` n `1261`
- 1h: commodity avg `-0.0368` n `13`; crypto_alt avg `-0.7953` n `239`; crypto_major avg `-0.7101` n `8`; equity avg `-1.4919` n `162`; fx avg `0.0104` n `6`; index avg `-0.1764` n `27`; metal avg `-0.4301` n `20`; unknown avg `0.6609` n `1249`
- 4h: commodity avg `-0.2613` n `13`; crypto_alt avg `-0.7374` n `239`; crypto_major avg `-0.9294` n `8`; equity avg `-0.6638` n `162`; fx avg `-0.024` n `6`; index avg `-0.05` n `27`; metal avg `-0.1216` n `20`; unknown avg `0.395` n `1193`
- 24h: commodity avg `-0.3423` n `13`; crypto_alt avg `2.6879` n `239`; crypto_major avg `4.3631` n `8`; equity avg `0.8556` n `162`; fx avg `-0.0045` n `6`; index avg `0.0698` n `27`; metal avg `0.2435` n `20`; unknown avg `2.2225` n `1127`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.134`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
