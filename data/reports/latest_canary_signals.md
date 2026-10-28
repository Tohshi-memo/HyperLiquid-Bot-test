# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T21:37:27.589852+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0276` n `13`; crypto_alt avg `-0.4831` n `238`; crypto_major avg `-0.3315` n `8`; equity avg `-0.1352` n `155`; fx avg `-0.0012` n `6`; index avg `-0.0263` n `27`; metal avg `-0.0221` n `20`; unknown avg `3.3064` n `1238`
- 1h: commodity avg `0.0198` n `13`; crypto_alt avg `0.1582` n `238`; crypto_major avg `0.08` n `8`; equity avg `-0.151` n `155`; fx avg `-0.0049` n `6`; index avg `-0.0525` n `27`; metal avg `-0.0065` n `20`; unknown avg `0.5217` n `1216`
- 4h: commodity avg `-0.279` n `13`; crypto_alt avg `1.5153` n `238`; crypto_major avg `0.881` n `8`; equity avg `-0.3332` n `155`; fx avg `-0.0167` n `6`; index avg `-0.0989` n `27`; metal avg `0.1164` n `20`; unknown avg `4.8573` n `1114`
- 24h: commodity avg `0.1355` n `13`; crypto_alt avg `0.437` n `238`; crypto_major avg `0.225` n `8`; equity avg `0.7826` n `154`; fx avg `0.2488` n `6`; index avg `0.1438` n `27`; metal avg `-0.1382` n `20`; unknown avg `26.6591` n `1060`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1493`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1458`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
