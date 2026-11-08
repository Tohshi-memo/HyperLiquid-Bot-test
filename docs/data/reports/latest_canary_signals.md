# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T17:37:31.452496+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0202` n `13`; crypto_alt avg `-0.1146` n `239`; crypto_major avg `-0.0767` n `8`; equity avg `-0.0056` n `158`; fx avg `0.0034` n `6`; index avg `0.0016` n `27`; metal avg `0.0008` n `20`; unknown avg `3.9337` n `1262`
- 1h: commodity avg `-0.0032` n `13`; crypto_alt avg `-0.7109` n `239`; crypto_major avg `-0.4392` n `8`; equity avg `-0.0655` n `158`; fx avg `-0.0001` n `6`; index avg `0.0022` n `27`; metal avg `-0.0104` n `20`; unknown avg `0.8299` n `1224`
- 4h: commodity avg `0.0133` n `13`; crypto_alt avg `-0.7905` n `239`; crypto_major avg `-0.6032` n `8`; equity avg `-0.2144` n `158`; fx avg `0.0284` n `6`; index avg `-0.0067` n `27`; metal avg `-0.0356` n `20`; unknown avg `-0.0238` n `1202`
- 24h: commodity avg `0.0562` n `13`; crypto_alt avg `-2.2654` n `239`; crypto_major avg `-0.5906` n `8`; equity avg `0.0473` n `158`; fx avg `0.0685` n `6`; index avg `-0.0136` n `27`; metal avg `-0.0508` n `20`; unknown avg `12.3558` n `1054`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
