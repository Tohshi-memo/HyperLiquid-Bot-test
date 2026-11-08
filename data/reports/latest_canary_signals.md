# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T10:37:32.467889+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0374` n `13`; crypto_alt avg `-0.0409` n `239`; crypto_major avg `-0.0266` n `8`; equity avg `-0.0287` n `158`; fx avg `0.0046` n `6`; index avg `-0.0029` n `27`; metal avg `0.0014` n `20`; unknown avg `0.0954` n `1262`
- 1h: commodity avg `0.026` n `13`; crypto_alt avg `-0.1333` n `239`; crypto_major avg `-0.1503` n `8`; equity avg `0.0095` n `158`; fx avg `-0.0047` n `6`; index avg `0.02` n `27`; metal avg `-0.008` n `20`; unknown avg `256.1112` n `1240`
- 4h: commodity avg `0.0595` n `13`; crypto_alt avg `-0.2725` n `239`; crypto_major avg `-0.1611` n `8`; equity avg `0.1785` n `158`; fx avg `0.0035` n `6`; index avg `0.0065` n `27`; metal avg `0.0043` n `20`; unknown avg `274.3672` n `1158`
- 24h: commodity avg `0.1312` n `13`; crypto_alt avg `-1.3501` n `239`; crypto_major avg `-0.5519` n `8`; equity avg `0.1245` n `158`; fx avg `0.0452` n `6`; index avg `0.0366` n `27`; metal avg `-0.0392` n `20`; unknown avg `5.5858` n `1097`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
