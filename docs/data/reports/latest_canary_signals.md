# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T17:22:26.020741+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0175` n `13`; crypto_alt avg `-0.1693` n `239`; crypto_major avg `-0.1574` n `8`; equity avg `-0.0268` n `158`; fx avg `-0.0079` n `6`; index avg `0.004` n `27`; metal avg `0.0017` n `20`; unknown avg `0.5973` n `1256`
- 1h: commodity avg `0.0183` n `13`; crypto_alt avg `-0.6169` n `239`; crypto_major avg `-0.4166` n `8`; equity avg `-0.0499` n `158`; fx avg `0.0124` n `6`; index avg `0.0059` n `27`; metal avg `-0.0071` n `20`; unknown avg `0.6119` n `1224`
- 4h: commodity avg `0.1108` n `13`; crypto_alt avg `-1.0797` n `239`; crypto_major avg `-0.8433` n `8`; equity avg `-0.256` n `158`; fx avg `0.0154` n `6`; index avg `-0.0099` n `27`; metal avg `-0.0392` n `20`; unknown avg `0.9519` n `1202`
- 24h: commodity avg `0.079` n `13`; crypto_alt avg `-2.0938` n `239`; crypto_major avg `-0.4354` n `8`; equity avg `0.1221` n `158`; fx avg `0.0644` n `6`; index avg `-0.0221` n `27`; metal avg `-0.0501` n `20`; unknown avg `12.2045` n `1054`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1653`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
