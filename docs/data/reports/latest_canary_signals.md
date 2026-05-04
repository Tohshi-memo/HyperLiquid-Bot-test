# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T19:30:23.901728+00:00`
- Correlation status: `ready`
- Asset price records: `292`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0182` n `7`; crypto_alt avg `-0.0931` n `223`; crypto_major avg `-0.167` n `7`; equity avg `-0.0296` n `42`; fx avg `0.0075` n `4`; index avg `-0.0984` n `9`; metal avg `0.0315` n `7`; unknown avg `0.1483` n `314`
- 1h: commodity avg `-0.2995` n `7`; crypto_alt avg `-0.1683` n `223`; crypto_major avg `-0.3453` n `7`; equity avg `-0.2059` n `42`; fx avg `-0.0091` n `4`; index avg `0.0683` n `9`; metal avg `0.199` n `7`; unknown avg `-0.0818` n `314`
- 4h: commodity avg `-0.1785` n `7`; crypto_alt avg `0.5167` n `223`; crypto_major avg `0.2206` n `7`; equity avg `-0.6288` n `42`; fx avg `-0.0093` n `4`; index avg `-0.215` n `9`; metal avg `-0.0821` n `7`; unknown avg `0.1007` n `314`
- 24h: commodity avg `1.5822` n `7`; crypto_alt avg `1.7028` n `223`; crypto_major avg `0.8285` n `7`; equity avg `-0.3527` n `42`; fx avg `-0.0812` n `4`; index avg `0.519` n `9`; metal avg `-2.2923` n `7`; unknown avg `-1.0117` n `312`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.237`, n `288`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2312`, n `288`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1705`, n `284`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1693`, n `284`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1502`, n `288`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1485`, n `288`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1432`, n `288`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1288`, n `288`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1269`, n `284`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1214`, n `284`, weak_sample_signal
