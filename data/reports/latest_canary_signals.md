# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T18:37:25.004890+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0022` n `13`; crypto_alt avg `-0.0646` n `235`; crypto_major avg `-0.0124` n `8`; equity avg `0.001` n `150`; fx avg `0.0019` n `6`; index avg `-0.0015` n `26`; metal avg `0.0035` n `20`; unknown avg `0.0142` n `1117`
- 1h: commodity avg `0.0084` n `13`; crypto_alt avg `0.0164` n `235`; crypto_major avg `-0.0659` n `8`; equity avg `-0.003` n `150`; fx avg `0.003` n `6`; index avg `-0.0079` n `26`; metal avg `-0.0019` n `20`; unknown avg `0.6922` n `1083`
- 4h: commodity avg `-0.0231` n `13`; crypto_alt avg `0.2428` n `235`; crypto_major avg `-0.4072` n `8`; equity avg `0.0042` n `150`; fx avg `-0.0037` n `6`; index avg `-0.0082` n `26`; metal avg `-0.0193` n `20`; unknown avg `1.27` n `1053`
- 24h: commodity avg `-0.3665` n `13`; crypto_alt avg `2.5223` n `235`; crypto_major avg `0.8326` n `8`; equity avg `0.117` n `150`; fx avg `-0.0087` n `6`; index avg `0.0091` n `26`; metal avg `-0.038` n `20`; unknown avg `0.3855` n `944`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.155`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
