# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T05:22:30.115917+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0363` n `13`; crypto_alt avg `0.0095` n `239`; crypto_major avg `0.0422` n `8`; equity avg `-0.0359` n `158`; fx avg `-0.0035` n `6`; index avg `-0.0034` n `27`; metal avg `0.0016` n `20`; unknown avg `0.1065` n `1261`
- 1h: commodity avg `0.0024` n `13`; crypto_alt avg `0.1376` n `239`; crypto_major avg `0.0211` n `8`; equity avg `-0.0047` n `158`; fx avg `-0.0078` n `6`; index avg `0.0008` n `27`; metal avg `0.0005` n `20`; unknown avg `0.7213` n `1247`
- 4h: commodity avg `-0.1342` n `13`; crypto_alt avg `-0.3935` n `239`; crypto_major avg `-0.3285` n `8`; equity avg `0.1468` n `158`; fx avg `-0.0005` n `6`; index avg `0.008` n `27`; metal avg `-0.0001` n `20`; unknown avg `1.6153` n `1233`
- 24h: commodity avg `-0.1798` n `13`; crypto_alt avg `0.6849` n `239`; crypto_major avg `0.2841` n `8`; equity avg `1.4029` n `158`; fx avg `-0.0825` n `6`; index avg `0.1799` n `27`; metal avg `0.305` n `20`; unknown avg `9.66` n `1006`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
