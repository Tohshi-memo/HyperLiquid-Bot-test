# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T23:45:29.588728+00:00`
- Correlation status: `ready`
- Asset price records: `118`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0229` n `7`; crypto_alt avg `0.021` n `223`; crypto_major avg `-0.1188` n `7`; equity avg `0.0358` n `42`; fx avg `-0.0021` n `4`; index avg `0.0064` n `9`; metal avg `-0.0009` n `7`; unknown avg `0.0504` n `313`
- 1h: commodity avg `0.0585` n `7`; crypto_alt avg `0.0664` n `223`; crypto_major avg `-0.0338` n `7`; equity avg `0.109` n `42`; fx avg `0.0067` n `4`; index avg `-0.004` n `9`; metal avg `0.0013` n `7`; unknown avg `-0.1458` n `313`
- 4h: commodity avg `0.0837` n `7`; crypto_alt avg `0.098` n `223`; crypto_major avg `0.0029` n `7`; equity avg `0.2887` n `42`; fx avg `0.0351` n `4`; index avg `-0.0235` n `9`; metal avg `0.0121` n `7`; unknown avg `-0.1075` n `313`
- 24h: commodity avg `-0.1709` n `7`; crypto_alt avg `2.2262` n `223`; crypto_major avg `0.6751` n `7`; equity avg `0.7936` n `42`; fx avg `-0.0031` n `4`; index avg `0.0675` n `9`; metal avg `0.035` n `7`; unknown avg `0.3335` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4844`, n `114`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4676`, n `114`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.4566`, n `110`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4163`, n `110`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4142`, n `110`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4073`, n `110`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4032`, n `114`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.4021`, n `110`, moderate_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.394`, n `110`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3853`, n `114`, moderate_sample_signal
