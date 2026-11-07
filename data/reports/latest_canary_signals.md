# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T01:22:27.838993+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0158` n `13`; crypto_alt avg `-0.0799` n `239`; crypto_major avg `-0.0244` n `8`; equity avg `-0.3867` n `158`; fx avg `-0.001` n `6`; index avg `-0.0267` n `27`; metal avg `-0.0032` n `20`; unknown avg `0.1984` n `1261`
- 1h: commodity avg `-0.015` n `13`; crypto_alt avg `0.1892` n `239`; crypto_major avg `0.0326` n `8`; equity avg `-0.1096` n `158`; fx avg `0.0012` n `6`; index avg `0.0098` n `27`; metal avg `0.0089` n `20`; unknown avg `1.8199` n `1255`
- 4h: commodity avg `0.0442` n `13`; crypto_alt avg `-0.3196` n `239`; crypto_major avg `0.1176` n `8`; equity avg `-0.1505` n `158`; fx avg `-0.0052` n `6`; index avg `-0.0133` n `27`; metal avg `0.0423` n `20`; unknown avg `-0.3111` n `1201`
- 24h: commodity avg `0.0073` n `13`; crypto_alt avg `1.4485` n `239`; crypto_major avg `0.1323` n `8`; equity avg `2.0462` n `158`; fx avg `-0.0593` n `6`; index avg `0.339` n `27`; metal avg `0.0774` n `20`; unknown avg `8.6054` n `1022`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1599`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
