# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T20:30:28.881783+00:00`
- Correlation status: `ready`
- Asset price records: `201`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0177` n `7`; crypto_alt avg `-0.0079` n `223`; crypto_major avg `0.0127` n `7`; equity avg `-0.0003` n `42`; fx avg `-0.0151` n `4`; index avg `-0.0032` n `9`; metal avg `0.0007` n `7`; unknown avg `0.0487` n `314`
- 1h: commodity avg `0.0484` n `7`; crypto_alt avg `0.1664` n `223`; crypto_major avg `0.0718` n `7`; equity avg `-0.035` n `42`; fx avg `0.0019` n `4`; index avg `0.0026` n `9`; metal avg `-0.0354` n `7`; unknown avg `-0.0128` n `314`
- 4h: commodity avg `0.4463` n `7`; crypto_alt avg `0.5468` n `223`; crypto_major avg `0.3343` n `7`; equity avg `0.128` n `42`; fx avg `-0.0118` n `4`; index avg `0.0105` n `9`; metal avg `0.095` n `7`; unknown avg `0.2013` n `313`
- 24h: commodity avg `0.0021` n `7`; crypto_alt avg `-0.0171` n `223`; crypto_major avg `0.298` n `7`; equity avg `0.2917` n `42`; fx avg `0.0565` n `4`; index avg `0.0639` n `9`; metal avg `0.4374` n `7`; unknown avg `0.0025` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3988`, n `197`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3811`, n `197`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3788`, n `193`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3716`, n `193`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3696`, n `197`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3567`, n `197`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3364`, n `197`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.3183`, n `197`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3061`, n `197`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.2546`, n `193`, moderate_sample_signal
