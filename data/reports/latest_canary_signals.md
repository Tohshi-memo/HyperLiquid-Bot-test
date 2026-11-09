# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T13:37:27.237225+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0944` n `13`; crypto_alt avg `0.0551` n `239`; crypto_major avg `-0.0357` n `8`; equity avg `0.2227` n `158`; fx avg `-0.0203` n `6`; index avg `0.0418` n `27`; metal avg `-0.0117` n `20`; unknown avg `-0.1203` n `1263`
- 1h: commodity avg `-0.0628` n `13`; crypto_alt avg `0.2137` n `239`; crypto_major avg `-0.2302` n `8`; equity avg `0.3769` n `158`; fx avg `-0.0164` n `6`; index avg `0.0562` n `27`; metal avg `0.013` n `20`; unknown avg `18.7001` n `1257`
- 4h: commodity avg `-0.3573` n `13`; crypto_alt avg `1.2181` n `239`; crypto_major avg `0.0355` n `8`; equity avg `0.8877` n `158`; fx avg `-0.05` n `6`; index avg `0.1304` n `27`; metal avg `0.0833` n `20`; unknown avg `0.3965` n `1251`
- 24h: commodity avg `-0.492` n `13`; crypto_alt avg `-0.0068` n `239`; crypto_major avg `-3.2855` n `8`; equity avg `0.1935` n `158`; fx avg `-0.1441` n `6`; index avg `0.064` n `27`; metal avg `0.3601` n `20`; unknown avg `0.142` n `1028`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1748`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
