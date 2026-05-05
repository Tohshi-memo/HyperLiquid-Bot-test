# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T02:45:25.960354+00:00`
- Correlation status: `ready`
- Asset price records: `321`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1058` n `7`; crypto_alt avg `-0.0186` n `223`; crypto_major avg `0.3287` n `7`; equity avg `0.0387` n `47`; fx avg `0.0021` n `4`; index avg `0.0142` n `6`; metal avg `0.0709` n `7`; unknown avg `-0.2158` n `312`
- 1h: commodity avg `-0.2444` n `7`; crypto_alt avg `0.3712` n `223`; crypto_major avg `0.5322` n `7`; equity avg `0.1569` n `47`; fx avg `0.0051` n `4`; index avg `0.0503` n `6`; metal avg `0.418` n `7`; unknown avg `-0.0069` n `312`
- 4h: commodity avg `-0.3229` n `7`; crypto_alt avg `0.7259` n `223`; crypto_major avg `0.7709` n `7`; equity avg `0.3567` n `47`; fx avg `-0.0021` n `4`; index avg `0.1096` n `6`; metal avg `0.667` n `7`; unknown avg `0.0427` n `312`
- 24h: commodity avg `0.9519` n `7`; crypto_alt avg `1.006` n `223`; crypto_major avg `-0.1203` n `7`; equity avg `-0.8646` n `47`; fx avg `-0.0637` n `4`; index avg `-0.1528` n `6`; metal avg `-1.5669` n `7`; unknown avg `-1.3618` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2274`, n `317`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2208`, n `317`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1514`, n `317`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1499`, n `313`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1476`, n `313`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1426`, n `317`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1377`, n `317`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1284`, n `317`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1255`, n `317`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1233`, n `313`, weak_sample_signal
