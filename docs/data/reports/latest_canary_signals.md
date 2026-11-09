# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T21:22:30.584470+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0256` n `13`; crypto_alt avg `-0.1074` n `239`; crypto_major avg `0.0113` n `8`; equity avg `0.089` n `160`; fx avg `0.0026` n `6`; index avg `-0.0192` n `27`; metal avg `-0.003` n `20`; unknown avg `-0.1068` n `1255`
- 1h: commodity avg `0.1929` n `13`; crypto_alt avg `-0.6167` n `239`; crypto_major avg `-0.1834` n `8`; equity avg `-0.4973` n `160`; fx avg `0.0193` n `6`; index avg `-0.0378` n `27`; metal avg `-0.0595` n `20`; unknown avg `3.3502` n `1221`
- 4h: commodity avg `-0.1209` n `13`; crypto_alt avg `-0.2358` n `239`; crypto_major avg `0.1412` n `8`; equity avg `-0.0351` n `160`; fx avg `-0.0048` n `6`; index avg `0.0718` n `27`; metal avg `0.2542` n `20`; unknown avg `3.3952` n `1211`
- 24h: commodity avg `-0.2807` n `13`; crypto_alt avg `0.3924` n `239`; crypto_major avg `-2.1541` n `8`; equity avg `4.1636` n `160`; fx avg `-0.1272` n `6`; index avg `0.5696` n `27`; metal avg `0.6357` n `20`; unknown avg `4.1783` n `1064`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1374`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
