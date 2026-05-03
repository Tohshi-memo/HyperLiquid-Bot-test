# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T14:45:22.375992+00:00`
- Correlation status: `ready`
- Asset price records: `178`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0203` n `7`; crypto_alt avg `0.0336` n `223`; crypto_major avg `-0.0154` n `7`; equity avg `0.007` n `42`; fx avg `-0.0053` n `4`; index avg `0.0` n `9`; metal avg `0.001` n `7`; unknown avg `-0.0928` n `313`
- 1h: commodity avg `-0.0253` n `7`; crypto_alt avg `0.0599` n `223`; crypto_major avg `0.1563` n `7`; equity avg `0.0475` n `42`; fx avg `-0.0074` n `4`; index avg `-0.0049` n `9`; metal avg `0.0403` n `7`; unknown avg `-0.0256` n `313`
- 4h: commodity avg `0.0065` n `7`; crypto_alt avg `0.0393` n `223`; crypto_major avg `0.3072` n `7`; equity avg `0.1465` n `42`; fx avg `0.0138` n `4`; index avg `-0.0281` n `9`; metal avg `0.0829` n `7`; unknown avg `-0.2884` n `313`
- 24h: commodity avg `-0.2813` n `7`; crypto_alt avg `0.4846` n `223`; crypto_major avg `0.1675` n `7`; equity avg `0.4292` n `42`; fx avg `0.158` n `4`; index avg `0.021` n `9`; metal avg `0.2272` n `7`; unknown avg `-0.29` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4029`, n `174`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3852`, n `174`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.383`, n `174`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3791`, n `170`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3743`, n `170`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3692`, n `174`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3547`, n `170`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3456`, n `170`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3223`, n `174`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3055`, n `174`, moderate_sample_signal
