# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T11:37:27.519726+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0037` n `13`; crypto_alt avg `-0.0496` n `239`; crypto_major avg `-0.1405` n `8`; equity avg `-0.0357` n `158`; fx avg `0.0056` n `6`; index avg `-0.0008` n `27`; metal avg `0.0711` n `20`; unknown avg `0.3001` n `1263`
- 1h: commodity avg `-0.4596` n `13`; crypto_alt avg `0.5834` n `239`; crypto_major avg `0.5588` n `8`; equity avg `0.1411` n `158`; fx avg `-0.0509` n `6`; index avg `0.0359` n `27`; metal avg `0.0834` n `20`; unknown avg `1.3302` n `1257`
- 4h: commodity avg `-0.2536` n `13`; crypto_alt avg `1.7688` n `239`; crypto_major avg `0.5401` n `8`; equity avg `1.2046` n `158`; fx avg `0.0226` n `6`; index avg `0.1628` n `27`; metal avg `0.1813` n `20`; unknown avg `170.0483` n `1137`
- 24h: commodity avg `-0.5917` n `13`; crypto_alt avg `-1.42` n `239`; crypto_major avg `-3.3989` n `8`; equity avg `-0.2693` n `158`; fx avg `-0.1498` n `6`; index avg `-0.0005` n `27`; metal avg `0.3539` n `20`; unknown avg `0.9049` n `1028`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1773`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1613`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
