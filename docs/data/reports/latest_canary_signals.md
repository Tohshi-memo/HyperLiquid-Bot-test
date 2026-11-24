# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T22:22:43.721849+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0286` n `13`; crypto_alt avg `0.0129` n `239`; crypto_major avg `-0.0317` n `8`; equity avg `0.1316` n `168`; fx avg `0.0035` n `6`; index avg `-0.0079` n `27`; metal avg `0.0047` n `20`; unknown avg `-0.0267` n `1263`
- 1h: commodity avg `-0.0239` n `13`; crypto_alt avg `-0.1268` n `239`; crypto_major avg `0.0429` n `8`; equity avg `0.1715` n `168`; fx avg `-0.0078` n `6`; index avg `-0.0087` n `27`; metal avg `0.0262` n `20`; unknown avg `21.8783` n `1253`
- 4h: commodity avg `-0.0363` n `13`; crypto_alt avg `-0.6278` n `239`; crypto_major avg `-0.2595` n `8`; equity avg `0.1644` n `168`; fx avg `-0.0476` n `6`; index avg `-0.0224` n `27`; metal avg `0.0207` n `20`; unknown avg `398.7943` n `1205`
- 24h: commodity avg `0.5784` n `13`; crypto_alt avg `-2.5824` n `239`; crypto_major avg `-2.5192` n `8`; equity avg `-4.0412` n `167`; fx avg `0.2191` n `6`; index avg `-0.293` n `27`; metal avg `-1.062` n `20`; unknown avg `426.263` n `1111`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
