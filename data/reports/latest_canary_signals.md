# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T09:37:40.466314+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0143` n `12`; crypto_alt avg `0.0459` n `230`; crypto_major avg `0.0101` n `8`; equity avg `-0.2087` n `102`; fx avg `0.004` n `6`; index avg `-0.0102` n `25`; metal avg `-0.0543` n `20`; unknown avg `0.0183` n `784`
- 1h: commodity avg `-0.1146` n `12`; crypto_alt avg `0.3479` n `230`; crypto_major avg `0.414` n `8`; equity avg `-0.0076` n `102`; fx avg `0.0126` n `6`; index avg `-0.0207` n `25`; metal avg `-0.0724` n `20`; unknown avg `0.1181` n `784`
- 4h: commodity avg `0.0854` n `12`; crypto_alt avg `-0.0301` n `230`; crypto_major avg `-0.1134` n `8`; equity avg `-0.8184` n `102`; fx avg `0.0423` n `6`; index avg `-0.097` n `25`; metal avg `-0.0448` n `20`; unknown avg `-0.0295` n `768`
- 24h: commodity avg `-0.0722` n `12`; crypto_alt avg `-0.9547` n `230`; crypto_major avg `-0.5377` n `8`; equity avg `-0.1137` n `102`; fx avg `-0.1662` n `6`; index avg `-0.0906` n `25`; metal avg `-0.1492` n `20`; unknown avg `1.0003` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
