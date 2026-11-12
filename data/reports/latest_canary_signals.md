# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T19:52:43.734115+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0379` n `13`; crypto_alt avg `0.3414` n `239`; crypto_major avg `0.3281` n `8`; equity avg `0.1368` n `162`; fx avg `-0.002` n `6`; index avg `0.0125` n `27`; metal avg `0.0205` n `20`; unknown avg `1.258` n `1261`
- 1h: commodity avg `0.2156` n `13`; crypto_alt avg `0.4915` n `239`; crypto_major avg `0.3991` n `8`; equity avg `0.0761` n `162`; fx avg `0.01` n `6`; index avg `0.0069` n `27`; metal avg `0.0227` n `20`; unknown avg `0.0801` n `1255`
- 4h: commodity avg `0.7123` n `13`; crypto_alt avg `0.828` n `239`; crypto_major avg `0.5083` n `8`; equity avg `0.1315` n `162`; fx avg `-0.0079` n `6`; index avg `-0.0069` n `27`; metal avg `0.1172` n `20`; unknown avg `62.5594` n `1229`
- 24h: commodity avg `0.9864` n `13`; crypto_alt avg `-2.3539` n `239`; crypto_major avg `-2.8177` n `8`; equity avg `-2.6529` n `162`; fx avg `-0.1394` n `6`; index avg `-0.1698` n `27`; metal avg `-0.7428` n `20`; unknown avg `21.9089` n `1139`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.136`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
