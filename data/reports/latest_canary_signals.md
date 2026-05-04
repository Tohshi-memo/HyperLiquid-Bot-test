# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T06:45:18.371623+00:00`
- Correlation status: `ready`
- Asset price records: `242`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.3777` n `7`; crypto_alt avg `0.14` n `223`; crypto_major avg `0.1612` n `7`; equity avg `-0.0587` n `42`; fx avg `0.0066` n `4`; index avg `0.0034` n `9`; metal avg `-0.2444` n `7`; unknown avg `0.0534` n `314`
- 1h: commodity avg `0.4947` n `7`; crypto_alt avg `-0.382` n `223`; crypto_major avg `-0.6475` n `7`; equity avg `-0.1539` n `42`; fx avg `0.0205` n `4`; index avg `0.0417` n `9`; metal avg `-0.3554` n `7`; unknown avg `-0.308` n `312`
- 4h: commodity avg `0.3049` n `7`; crypto_alt avg `0.0228` n `223`; crypto_major avg `-0.3732` n `7`; equity avg `-0.3503` n `42`; fx avg `-0.0326` n `4`; index avg `0.2752` n `9`; metal avg `-0.5136` n `7`; unknown avg `-0.2968` n `312`
- 24h: commodity avg `0.4409` n `7`; crypto_alt avg `2.364` n `223`; crypto_major avg `2.3551` n `7`; equity avg `0.9851` n `42`; fx avg `-0.0191` n `4`; index avg `0.9791` n `9`; metal avg `-0.2965` n `7`; unknown avg `0.1257` n `311`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.407`, n `234`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3975`, n `234`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.358`, n `238`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3443`, n `238`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.207`, n `234`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1969`, n `234`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1782`, n `238`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1723`, n `238`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1671`, n `238`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.166`, n `234`, weak_sample_signal
