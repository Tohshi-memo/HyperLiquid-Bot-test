# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T08:37:31.266507+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1541` n `13`; crypto_alt avg `0.0059` n `239`; crypto_major avg `0.0083` n `8`; equity avg `0.0236` n `158`; fx avg `-0.0038` n `6`; index avg `-0.0105` n `27`; metal avg `-0.0002` n `20`; unknown avg `0.0452` n `1262`
- 1h: commodity avg `0.1563` n `13`; crypto_alt avg `-0.0812` n `239`; crypto_major avg `0.0167` n `8`; equity avg `0.0536` n `158`; fx avg `-0.0088` n `6`; index avg `0.0232` n `27`; metal avg `0.0043` n `20`; unknown avg `201.6755` n `1240`
- 4h: commodity avg `0.205` n `13`; crypto_alt avg `0.0324` n `239`; crypto_major avg `0.0246` n `8`; equity avg `0.1721` n `158`; fx avg `0.0096` n `6`; index avg `0.03` n `27`; metal avg `0.0128` n `20`; unknown avg `0.0124` n `1204`
- 24h: commodity avg `0.309` n `13`; crypto_alt avg `-1.7124` n `239`; crypto_major avg `-0.8168` n `8`; equity avg `-0.0136` n `158`; fx avg `0.066` n `6`; index avg `0.0433` n `27`; metal avg `-0.0398` n `20`; unknown avg `157.0978` n `1093`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1555`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
