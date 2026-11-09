# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T12:22:27.297400+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.006` n `13`; crypto_alt avg `0.2728` n `239`; crypto_major avg `0.2506` n `8`; equity avg `0.0092` n `158`; fx avg `0.0033` n `6`; index avg `0.0062` n `27`; metal avg `0.0338` n `20`; unknown avg `12.8629` n `1263`
- 1h: commodity avg `0.0497` n `13`; crypto_alt avg `0.4696` n `239`; crypto_major avg `0.064` n `8`; equity avg `0.034` n `158`; fx avg `0.0034` n `6`; index avg `-0.0079` n `27`; metal avg `0.0513` n `20`; unknown avg `31.5204` n `1251`
- 4h: commodity avg `-0.2238` n `13`; crypto_alt avg `1.9176` n `239`; crypto_major avg `0.5271` n `8`; equity avg `0.9692` n `158`; fx avg `-0.0264` n `6`; index avg `0.1196` n `27`; metal avg `0.1321` n `20`; unknown avg `169.6471` n `1227`
- 24h: commodity avg `-0.5321` n `13`; crypto_alt avg `-0.7817` n `239`; crypto_major avg `-3.2379` n `8`; equity avg `-0.1686` n `158`; fx avg `-0.1452` n `6`; index avg `0.011` n `27`; metal avg `0.3301` n `20`; unknown avg `15.4022` n `1028`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
