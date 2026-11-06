# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T21:52:27.094701+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0449` n `13`; crypto_alt avg `0.1094` n `239`; crypto_major avg `0.1602` n `8`; equity avg `0.1413` n `158`; fx avg `-0.0074` n `6`; index avg `-0.0104` n `27`; metal avg `0.0247` n `20`; unknown avg `1.1915` n `1261`
- 1h: commodity avg `0.0321` n `13`; crypto_alt avg `0.0914` n `239`; crypto_major avg `0.0648` n `8`; equity avg `0.3334` n `158`; fx avg `0.0127` n `6`; index avg `0.0175` n `27`; metal avg `0.0231` n `20`; unknown avg `0.9234` n `1193`
- 4h: commodity avg `0.2267` n `13`; crypto_alt avg `0.1174` n `239`; crypto_major avg `0.1984` n `8`; equity avg `1.3831` n `158`; fx avg `0.036` n `6`; index avg `0.0729` n `27`; metal avg `0.0958` n `20`; unknown avg `0.4073` n `1183`
- 24h: commodity avg `0.0529` n `13`; crypto_alt avg `1.5604` n `239`; crypto_major avg `-0.1315` n `8`; equity avg `2.7243` n `158`; fx avg `-0.0773` n `6`; index avg `0.4077` n `27`; metal avg `0.031` n `20`; unknown avg `0.5234` n `1034`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
