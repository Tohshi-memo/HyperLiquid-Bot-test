# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T19:52:29.051120+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0177` n `13`; crypto_alt avg `0.025` n `239`; crypto_major avg `0.0039` n `8`; equity avg `-0.0388` n `158`; fx avg `-0.008` n `6`; index avg `-0.003` n `27`; metal avg `-0.0017` n `20`; unknown avg `0.1994` n `1262`
- 1h: commodity avg `-0.0145` n `13`; crypto_alt avg `-0.1041` n `239`; crypto_major avg `-0.1361` n `8`; equity avg `0.0394` n `158`; fx avg `-0.0027` n `6`; index avg `0.0019` n `27`; metal avg `0.0101` n `20`; unknown avg `0.0737` n `1248`
- 4h: commodity avg `-0.131` n `13`; crypto_alt avg `-0.2277` n `239`; crypto_major avg `-0.216` n `8`; equity avg `0.4001` n `158`; fx avg `0.0031` n `6`; index avg `0.0421` n `27`; metal avg `0.0339` n `20`; unknown avg `0.6158` n `1186`
- 24h: commodity avg `-0.1017` n `13`; crypto_alt avg `-1.3249` n `239`; crypto_major avg `-0.1724` n `8`; equity avg `0.4647` n `158`; fx avg `0.0488` n `6`; index avg `0.0168` n `27`; metal avg `-0.0138` n `20`; unknown avg `-0.1981` n `1038`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1561`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
