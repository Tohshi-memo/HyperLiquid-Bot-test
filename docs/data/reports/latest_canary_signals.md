# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T04:00:27.456157+00:00`
- Correlation status: `ready`
- Asset price records: `420`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0803` n `7`; crypto_alt avg `0.0151` n `223`; crypto_major avg `0.1476` n `7`; equity avg `-0.077` n `47`; fx avg `0.0117` n `4`; index avg `0.0097` n `6`; metal avg `-0.0184` n `7`; unknown avg `-0.0769` n `313`
- 1h: commodity avg `0.0353` n `7`; crypto_alt avg `0.0755` n `223`; crypto_major avg `0.3066` n `7`; equity avg `0.1954` n `47`; fx avg `0.0321` n `4`; index avg `0.1718` n `6`; metal avg `0.1099` n `7`; unknown avg `-0.108` n `313`
- 4h: commodity avg `0.0523` n `7`; crypto_alt avg `1.2463` n `223`; crypto_major avg `0.8355` n `7`; equity avg `0.4351` n `47`; fx avg `-0.014` n `4`; index avg `0.5498` n `6`; metal avg `1.1429` n `7`; unknown avg `0.0384` n `313`
- 24h: commodity avg `-1.5008` n `7`; crypto_alt avg `2.6508` n `223`; crypto_major avg `2.0331` n `7`; equity avg `2.925` n `47`; fx avg `-0.1567` n `4`; index avg `2.2813` n `6`; metal avg `2.262` n `7`; unknown avg `1.3983` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1813`, n `416`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.175`, n `416`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1268`, n `416`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1267`, n `416`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.123`, n `416`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1097`, n `416`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1005`, n `412`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.096`, n `416`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0953`, n `416`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0946`, n `412`, weak_sample_signal
