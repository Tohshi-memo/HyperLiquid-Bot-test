# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T02:37:29.491097+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0363` n `13`; crypto_alt avg `0.2554` n `239`; crypto_major avg `0.0964` n `8`; equity avg `0.0792` n `158`; fx avg `-0.0216` n `6`; index avg `0.0064` n `27`; metal avg `-0.0036` n `20`; unknown avg `0.3841` n `1262`
- 1h: commodity avg `0.106` n `13`; crypto_alt avg `0.7708` n `239`; crypto_major avg `0.7369` n `8`; equity avg `1.2268` n `158`; fx avg `-0.074` n `6`; index avg `0.0958` n `27`; metal avg `0.1083` n `20`; unknown avg `0.9795` n `1254`
- 4h: commodity avg `-0.129` n `13`; crypto_alt avg `2.226` n `239`; crypto_major avg `1.432` n `8`; equity avg `1.7836` n `158`; fx avg `-0.0915` n `6`; index avg `0.2522` n `27`; metal avg `0.6466` n `20`; unknown avg `2.6879` n `1222`
- 24h: commodity avg `-0.0053` n `13`; crypto_alt avg `-1.2364` n `239`; crypto_major avg `-1.6761` n `8`; equity avg `0.9546` n `158`; fx avg `-0.081` n `6`; index avg `0.1034` n `27`; metal avg `0.529` n `20`; unknown avg `2.1019` n `994`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
