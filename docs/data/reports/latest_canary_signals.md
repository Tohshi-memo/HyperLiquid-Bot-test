# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T06:52:27.867645+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0065` n `13`; crypto_alt avg `0.1455` n `238`; crypto_major avg `0.158` n `8`; equity avg `0.0353` n `156`; fx avg `0.0032` n `6`; index avg `-0.002` n `27`; metal avg `-0.0041` n `20`; unknown avg `0.0422` n `1262`
- 1h: commodity avg `0.0094` n `13`; crypto_alt avg `0.5068` n `238`; crypto_major avg `0.1795` n `8`; equity avg `0.0351` n `156`; fx avg `0.0005` n `6`; index avg `-0.0004` n `27`; metal avg `0.0251` n `20`; unknown avg `-0.0712` n `1226`
- 4h: commodity avg `0.0192` n `13`; crypto_alt avg `-0.4628` n `238`; crypto_major avg `-0.4585` n `8`; equity avg `0.004` n `156`; fx avg `0.015` n `6`; index avg `-0.0428` n `27`; metal avg `0.026` n `20`; unknown avg `-0.1871` n `1210`
- 24h: commodity avg `0.0289` n `13`; crypto_alt avg `0.8106` n `238`; crypto_major avg `-1.6607` n `8`; equity avg `-2.4922` n `156`; fx avg `-0.0519` n `6`; index avg `-0.2113` n `27`; metal avg `-0.4792` n `20`; unknown avg `3.8848` n `1002`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
