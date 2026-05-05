# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T05:00:31.019227+00:00`
- Correlation status: `ready`
- Asset price records: `330`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0748` n `7`; crypto_alt avg `-0.1253` n `223`; crypto_major avg `0.0644` n `7`; equity avg `0.0901` n `47`; fx avg `-0.0107` n `4`; index avg `-0.0457` n `6`; metal avg `-0.0707` n `7`; unknown avg `-0.1794` n `312`
- 1h: commodity avg `-0.0709` n `7`; crypto_alt avg `-0.1914` n `223`; crypto_major avg `-0.1261` n `7`; equity avg `0.1039` n `47`; fx avg `-0.0091` n `4`; index avg `0.0624` n `6`; metal avg `-0.0496` n `7`; unknown avg `-0.0476` n `312`
- 4h: commodity avg `-0.2098` n `7`; crypto_alt avg `0.3974` n `223`; crypto_major avg `0.6633` n `7`; equity avg `0.37` n `47`; fx avg `-0.0142` n `4`; index avg `0.2147` n `6`; metal avg `0.1079` n `7`; unknown avg `0.2494` n `312`
- 24h: commodity avg `0.9853` n `7`; crypto_alt avg `0.1383` n `223`; crypto_major avg `-0.718` n `7`; equity avg `-0.7239` n `47`; fx avg `-0.0167` n `4`; index avg `-0.1458` n `6`; metal avg `-1.8947` n `7`; unknown avg `-1.2577` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.227`, n `326`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2206`, n `326`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1534`, n `326`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1408`, n `326`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1393`, n `322`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1366`, n `322`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1362`, n `326`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1294`, n `326`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1226`, n `326`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1203`, n `326`, weak_sample_signal
