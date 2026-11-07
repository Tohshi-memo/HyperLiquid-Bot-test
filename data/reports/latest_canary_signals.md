# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T10:22:23.201551+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0039` n `13`; crypto_alt avg `-0.075` n `239`; crypto_major avg `-0.0701` n `8`; equity avg `-0.0292` n `158`; fx avg `0.0001` n `6`; index avg `-0.0067` n `27`; metal avg `0.0065` n `20`; unknown avg `0.0177` n `1261`
- 1h: commodity avg `0.0344` n `13`; crypto_alt avg `-0.3427` n `239`; crypto_major avg `-0.1823` n `8`; equity avg `-0.1531` n `158`; fx avg `0.0012` n `6`; index avg `-0.0265` n `27`; metal avg `0.0077` n `20`; unknown avg `1.8566` n `1255`
- 4h: commodity avg `0.0833` n `13`; crypto_alt avg `-0.4143` n `239`; crypto_major avg `-0.1367` n `8`; equity avg `0.0535` n `158`; fx avg `-0.0046` n `6`; index avg `-0.0012` n `27`; metal avg `0.0026` n `20`; unknown avg `136.8001` n `1193`
- 24h: commodity avg `0.0784` n `13`; crypto_alt avg `-1.0887` n `239`; crypto_major avg `-0.3042` n `8`; equity avg `-0.1863` n `158`; fx avg `0.0325` n `6`; index avg `-0.0047` n `27`; metal avg `0.1065` n `20`; unknown avg `7.9111` n `1046`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1562`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
