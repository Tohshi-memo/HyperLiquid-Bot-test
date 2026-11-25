# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T23:22:32.684455+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.042` n `13`; crypto_alt avg `0.2076` n `239`; crypto_major avg `0.2268` n `8`; equity avg `0.229` n `168`; fx avg `0.0006` n `6`; index avg `0.0194` n `27`; metal avg `0.0681` n `20`; unknown avg `2.9442` n `1267`
- 1h: commodity avg `0.0057` n `13`; crypto_alt avg `-0.016` n `239`; crypto_major avg `-0.0557` n `8`; equity avg `0.2269` n `168`; fx avg `0.0043` n `6`; index avg `0.0141` n `27`; metal avg `-0.0294` n `20`; unknown avg `39.6759` n `1207`
- 4h: commodity avg `0.0645` n `13`; crypto_alt avg `-0.3032` n `239`; crypto_major avg `-0.5558` n `8`; equity avg `0.1452` n `168`; fx avg `-0.0196` n `6`; index avg `-0.0046` n `27`; metal avg `0.2632` n `20`; unknown avg `457.6224` n `1143`
- 24h: commodity avg `0.4064` n `13`; crypto_alt avg `2.1624` n `239`; crypto_major avg `0.6764` n `8`; equity avg `-0.4694` n `168`; fx avg `0.0509` n `6`; index avg `-0.0708` n `27`; metal avg `0.1874` n `20`; unknown avg `771.1411` n `1017`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1807`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
