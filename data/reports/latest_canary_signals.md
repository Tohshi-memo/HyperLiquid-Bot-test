# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T06:45:43.961958+00:00`
- Correlation status: `ready`
- Asset price records: `431`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1142` n `7`; crypto_alt avg `0.2181` n `223`; crypto_major avg `0.161` n `7`; equity avg `0.0011` n `47`; fx avg `-0.0044` n `4`; index avg `-0.0156` n `6`; metal avg `-0.1162` n `7`; unknown avg `0.0962` n `313`
- 1h: commodity avg `-0.031` n `7`; crypto_alt avg `0.3958` n `223`; crypto_major avg `0.334` n `7`; equity avg `-0.0069` n `47`; fx avg `-0.0309` n `4`; index avg `0.0024` n `6`; metal avg `0.0427` n `7`; unknown avg `0.4431` n `311`
- 4h: commodity avg `0.0906` n `7`; crypto_alt avg `0.5758` n `223`; crypto_major avg `0.5881` n `7`; equity avg `0.694` n `47`; fx avg `-0.2379` n `4`; index avg `0.3577` n `6`; metal avg `0.4944` n `7`; unknown avg `0.8397` n `311`
- 24h: commodity avg `-1.4763` n `7`; crypto_alt avg `2.8133` n `223`; crypto_major avg `1.909` n `7`; equity avg `2.6805` n `47`; fx avg `-0.4065` n `4`; index avg `2.1704` n `6`; metal avg `2.0653` n `7`; unknown avg `1.73` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1805`, n `427`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1742`, n `427`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1289`, n `427`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1261`, n `427`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1223`, n `427`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.112`, n `427`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.102`, n `423`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.097`, n `423`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0954`, n `427`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0946`, n `427`, weak_sample_signal
