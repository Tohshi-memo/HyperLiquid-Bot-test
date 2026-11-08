# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T18:37:27.347815+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0131` n `13`; crypto_alt avg `0.1346` n `239`; crypto_major avg `0.0224` n `8`; equity avg `-0.0247` n `158`; fx avg `-0.0152` n `6`; index avg `-0.0061` n `27`; metal avg `0.0056` n `20`; unknown avg `8.5253` n `1262`
- 1h: commodity avg `-0.175` n `13`; crypto_alt avg `0.7573` n `239`; crypto_major avg `0.4696` n `8`; equity avg `0.4346` n `158`; fx avg `-0.0158` n `6`; index avg `0.0232` n `27`; metal avg `0.0195` n `20`; unknown avg `10.2798` n `1208`
- 4h: commodity avg `-0.1169` n `13`; crypto_alt avg `0.0409` n `239`; crypto_major avg `-0.0892` n `8`; equity avg `0.2464` n `158`; fx avg `0.0223` n `6`; index avg `0.027` n `27`; metal avg `-0.0102` n `20`; unknown avg `9.0051` n `1196`
- 24h: commodity avg `-0.0844` n `13`; crypto_alt avg `-1.6036` n `239`; crypto_major avg `-0.1958` n `8`; equity avg `0.3767` n `158`; fx avg `0.0624` n `6`; index avg `-0.0061` n `27`; metal avg `-0.0346` n `20`; unknown avg `8.2167` n `1048`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
