# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T03:30:32.645734+00:00`
- Correlation status: `ready`
- Asset price records: `229`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.0037` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0308` n `7`; crypto_alt avg `-0.1605` n `223`; crypto_major avg `-0.2467` n `7`; equity avg `-0.0754` n `42`; fx avg `-0.0045` n `4`; index avg `-0.0924` n `9`; metal avg `-0.0434` n `7`; unknown avg `0.2852` n `314`
- 1h: commodity avg `-0.0788` n `7`; crypto_alt avg `0.2482` n `223`; crypto_major avg `0.3381` n `7`; equity avg `0.312` n `42`; fx avg `0.0114` n `4`; index avg `0.2197` n `9`; metal avg `0.3804` n `7`; unknown avg `0.0671` n `314`
- 4h: commodity avg `0.082` n `7`; crypto_alt avg `1.7677` n `223`; crypto_major avg `1.9485` n `7`; equity avg `1.2267` n `42`; fx avg `0.0443` n `4`; index avg `0.6287` n `9`; metal avg `-0.0552` n `7`; unknown avg `0.0689` n `314`
- 24h: commodity avg `0.0659` n `7`; crypto_alt avg `2.6491` n `223`; crypto_major avg `2.6736` n `7`; equity avg `1.2703` n `42`; fx avg `0.0239` n `4`; index avg `0.7798` n `9`; metal avg `0.3538` n `7`; unknown avg `0.5428` n `311`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3936`, n `221`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3835`, n `221`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3665`, n `225`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3509`, n `225`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.2161`, n `221`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1994`, n `221`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1947`, n `225`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1884`, n `225`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1828`, n `225`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1406`, n `225`, weak_sample_signal
