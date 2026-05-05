# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T03:30:28.423003+00:00`
- Correlation status: `ready`
- Asset price records: `324`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0433` n `7`; crypto_alt avg `0.2018` n `223`; crypto_major avg `0.0795` n `7`; equity avg `-0.203` n `47`; fx avg `0.0011` n `4`; index avg `0.0088` n `6`; metal avg `-0.1424` n `7`; unknown avg `-0.0731` n `312`
- 1h: commodity avg `0.0133` n `7`; crypto_alt avg `0.0082` n `223`; crypto_major avg `0.2605` n `7`; equity avg `-0.0447` n `47`; fx avg `-0.0051` n `4`; index avg `0.0532` n `6`; metal avg `-0.1398` n `7`; unknown avg `-0.2207` n `312`
- 4h: commodity avg `-0.2293` n `7`; crypto_alt avg `0.9161` n `223`; crypto_major avg `0.7984` n `7`; equity avg `0.4106` n `47`; fx avg `-0.0136` n `4`; index avg `0.1567` n `6`; metal avg `0.4644` n `7`; unknown avg `0.1559` n `312`
- 24h: commodity avg `1.0774` n `7`; crypto_alt avg `0.9939` n `223`; crypto_major avg `-0.1239` n `7`; equity avg `-1.0326` n `47`; fx avg `-0.0778` n `4`; index avg `-0.221` n `6`; metal avg `-1.8856` n `7`; unknown avg `-1.3702` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2268`, n `320`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2202`, n `320`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1506`, n `320`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1418`, n `320`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1409`, n `316`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1383`, n `316`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.137`, n `320`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1289`, n `320`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1255`, n `320`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1211`, n `316`, weak_sample_signal
