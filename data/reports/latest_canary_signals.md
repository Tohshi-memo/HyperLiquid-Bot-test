# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T21:07:26.791080+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0074` n `13`; crypto_alt avg `-0.0554` n `239`; crypto_major avg `-0.1068` n `8`; equity avg `0.0152` n `158`; fx avg `-0.0057` n `6`; index avg `0.0024` n `27`; metal avg `-0.006` n `20`; unknown avg `0.5386` n `1242`
- 1h: commodity avg `0.0417` n `13`; crypto_alt avg `-0.0133` n `239`; crypto_major avg `-0.162` n `8`; equity avg `-0.294` n `158`; fx avg `-0.012` n `6`; index avg `-0.051` n `27`; metal avg `-0.0183` n `20`; unknown avg `0.5141` n `1232`
- 4h: commodity avg `-0.1097` n `13`; crypto_alt avg `0.0814` n `239`; crypto_major avg `-0.2257` n `8`; equity avg `-0.1616` n `158`; fx avg `-0.0402` n `6`; index avg `-0.035` n `27`; metal avg `0.0142` n `20`; unknown avg `13.382` n `1164`
- 24h: commodity avg `-0.1043` n `13`; crypto_alt avg `-1.0065` n `239`; crypto_major avg `-0.0414` n `8`; equity avg `0.0571` n `158`; fx avg `0.0356` n `6`; index avg `-0.0604` n `27`; metal avg `-0.0304` n `20`; unknown avg `-0.184` n `1028`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1581`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
