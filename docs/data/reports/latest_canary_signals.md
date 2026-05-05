# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T00:45:18.002813+00:00`
- Correlation status: `ready`
- Asset price records: `313`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0045` n `7`; crypto_alt avg `0.1827` n `223`; crypto_major avg `0.2161` n `7`; equity avg `0.1151` n `47`; fx avg `0.0016` n `4`; index avg `0.0003` n `6`; metal avg `0.1348` n `7`; unknown avg `0.0139` n `312`
- 1h: commodity avg `-0.0675` n `7`; crypto_alt avg `0.3189` n `223`; crypto_major avg `0.3295` n `7`; equity avg `0.3055` n `47`; fx avg `-0.0059` n `4`; index avg `-0.0068` n `6`; metal avg `0.188` n `7`; unknown avg `0.0038` n `312`
- 4h: commodity avg `-0.0007` n `7`; crypto_alt avg `0.3464` n `223`; crypto_major avg `0.2699` n `7`; equity avg `0.1518` n `47`; fx avg `-0.0091` n `4`; index avg `-0.2112` n `6`; metal avg `0.1301` n `7`; unknown avg `-0.1568` n `312`
- 24h: commodity avg `1.3158` n `7`; crypto_alt avg `2.3531` n `223`; crypto_major avg `1.5252` n `7`; equity avg `-0.2493` n `47`; fx avg `-0.0271` n `4`; index avg `-0.0528` n `6`; metal avg `-1.9725` n `7`; unknown avg `-1.2015` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2349`, n `309`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2289`, n `309`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1758`, n `305`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1734`, n `305`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1499`, n `309`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.147`, n `309`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1415`, n `309`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1304`, n `309`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1204`, n `305`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1197`, n `309`, weak_sample_signal
