# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T04:15:18.886662+00:00`
- Correlation status: `ready`
- Asset price records: `421`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0236` n `7`; crypto_alt avg `0.0329` n `223`; crypto_major avg `0.0033` n `7`; equity avg `0.0167` n `47`; fx avg `-0.0094` n `4`; index avg `0.0312` n `6`; metal avg `0.0363` n `7`; unknown avg `-0.1279` n `313`
- 1h: commodity avg `-0.0538` n `7`; crypto_alt avg `0.3515` n `223`; crypto_major avg `0.3263` n `7`; equity avg `0.3275` n `47`; fx avg `-0.0066` n `4`; index avg `0.2005` n `6`; metal avg `0.0208` n `7`; unknown avg `-0.0755` n `313`
- 4h: commodity avg `-0.1126` n `7`; crypto_alt avg `1.1876` n `223`; crypto_major avg `0.6375` n `7`; equity avg `0.535` n `47`; fx avg `-0.058` n `4`; index avg `0.6038` n `6`; metal avg `1.4296` n `7`; unknown avg `0.1109` n `313`
- 24h: commodity avg `-1.4844` n `7`; crypto_alt avg `2.8325` n `223`; crypto_major avg `2.0642` n `7`; equity avg `3.1795` n `47`; fx avg `-0.1831` n `4`; index avg `2.3036` n `6`; metal avg `2.3557` n `7`; unknown avg `1.5467` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1811`, n `417`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1748`, n `417`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1271`, n `417`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1266`, n `417`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1228`, n `417`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.11`, n `417`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1007`, n `413`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0957`, n `417`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0951`, n `413`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.095`, n `417`, weak_sample_signal
