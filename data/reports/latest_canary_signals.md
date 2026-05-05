# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T02:30:35.042697+00:00`
- Correlation status: `ready`
- Asset price records: `320`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0264` n `7`; crypto_alt avg `0.1634` n `223`; crypto_major avg `-0.0181` n `7`; equity avg `0.124` n `47`; fx avg `0.0067` n `4`; index avg `0.0238` n `6`; metal avg `0.1001` n `7`; unknown avg `0.1513` n `312`
- 1h: commodity avg `-0.1859` n `7`; crypto_alt avg `0.3875` n `223`; crypto_major avg `0.1741` n `7`; equity avg `0.223` n `47`; fx avg `0.0081` n `4`; index avg `0.0557` n `6`; metal avg `0.3162` n `7`; unknown avg `0.3438` n `312`
- 4h: commodity avg `-0.216` n `7`; crypto_alt avg `0.5264` n `223`; crypto_major avg `0.254` n `7`; equity avg `0.2022` n `47`; fx avg `-0.005` n `4`; index avg `0.0773` n `6`; metal avg `0.5462` n `7`; unknown avg `0.129` n `312`
- 24h: commodity avg `0.9845` n `7`; crypto_alt avg `1.267` n `223`; crypto_major avg `-0.0471` n `7`; equity avg `-0.6712` n `47`; fx avg `-0.0613` n `4`; index avg `-0.1438` n `6`; metal avg `-1.3775` n `7`; unknown avg `-1.0924` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2293`, n `316`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2228`, n `316`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1531`, n `316`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1526`, n `312`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1504`, n `312`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1436`, n `316`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1386`, n `316`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1284`, n `316`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1247`, n `316`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1237`, n `312`, weak_sample_signal
