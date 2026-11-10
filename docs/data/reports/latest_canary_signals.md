# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T00:52:34.413328+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0127` n `13`; crypto_alt avg `0.085` n `239`; crypto_major avg `0.0241` n `8`; equity avg `-0.3811` n `160`; fx avg `-0.0002` n `6`; index avg `-0.0426` n `27`; metal avg `-0.0099` n `20`; unknown avg `0.4312` n `1261`
- 1h: commodity avg `0.0428` n `13`; crypto_alt avg `-0.0387` n `239`; crypto_major avg `-0.286` n `8`; equity avg `-0.4819` n `160`; fx avg `0.0226` n `6`; index avg `-0.088` n `27`; metal avg `-0.1144` n `20`; unknown avg `0.5386` n `1249`
- 4h: commodity avg `-0.0433` n `13`; crypto_alt avg `-0.6873` n `239`; crypto_major avg `-0.2467` n `8`; equity avg `-0.173` n `160`; fx avg `0.0654` n `6`; index avg `-0.1009` n `27`; metal avg `-0.1256` n `20`; unknown avg `0.1919` n `1209`
- 24h: commodity avg `-0.3887` n `13`; crypto_alt avg `0.793` n `239`; crypto_major avg `-0.5535` n `8`; equity avg `4.5549` n `160`; fx avg `-0.0182` n `6`; index avg `0.4866` n `27`; metal avg `0.1672` n `20`; unknown avg `5.0508` n `1064`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1689`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
