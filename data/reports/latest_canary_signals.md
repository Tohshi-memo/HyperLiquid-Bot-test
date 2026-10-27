# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T02:37:29.595838+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0132` n `13`; crypto_alt avg `-0.1564` n `237`; crypto_major avg `-0.1573` n `8`; equity avg `-0.1169` n `154`; fx avg `0.0067` n `6`; index avg `-0.022` n `27`; metal avg `-0.0005` n `20`; unknown avg `4.4616` n `1238`
- 1h: commodity avg `0.0303` n `13`; crypto_alt avg `-0.429` n `237`; crypto_major avg `-0.3955` n `8`; equity avg `-0.2492` n `154`; fx avg `-0.0004` n `6`; index avg `-0.0481` n `27`; metal avg `-0.032` n `20`; unknown avg `3.2426` n `1236`
- 4h: commodity avg `-0.0704` n `13`; crypto_alt avg `-0.0844` n `237`; crypto_major avg `0.1893` n `8`; equity avg `0.0633` n `154`; fx avg `-0.019` n `6`; index avg `0.0724` n `27`; metal avg `-0.0227` n `20`; unknown avg `1.9425` n `1220`
- 24h: commodity avg `0.0399` n `13`; crypto_alt avg `0.4709` n `237`; crypto_major avg `0.8605` n `8`; equity avg `2.0832` n `153`; fx avg `0.0075` n `6`; index avg `0.1354` n `27`; metal avg `0.0686` n `20`; unknown avg `999.853` n `1004`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2195`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1987`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1939`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
