# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T17:45:42.670647+00:00`
- Correlation status: `ready`
- Asset price records: `285`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.6977` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0392` n `7`; crypto_alt avg `-0.0031` n `223`; crypto_major avg `-0.0546` n `7`; equity avg `-0.0119` n `42`; fx avg `-0.0` n `4`; index avg `-0.2019` n `9`; metal avg `0.0181` n `7`; unknown avg `0.0549` n `314`
- 1h: commodity avg `-0.2472` n `7`; crypto_alt avg `0.3662` n `223`; crypto_major avg `0.1882` n `7`; equity avg `-0.0021` n `42`; fx avg `0.0123` n `4`; index avg `-0.0033` n `9`; metal avg `0.296` n `7`; unknown avg `0.0821` n `314`
- 4h: commodity avg `0.8306` n `7`; crypto_alt avg `0.8633` n `223`; crypto_major avg `0.9961` n `7`; equity avg `-0.3412` n `42`; fx avg `-0.0132` n `4`; index avg `-0.3011` n `9`; metal avg `-0.7016` n `7`; unknown avg `-0.4144` n `314`
- 24h: commodity avg `1.9658` n `7`; crypto_alt avg `2.0145` n `223`; crypto_major avg `1.3034` n `7`; equity avg `-0.1411` n `42`; fx avg `-0.0836` n `4`; index avg `0.4642` n `9`; metal avg `-2.2246` n `7`; unknown avg `-0.7491` n `312`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2384`, n `281`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2326`, n `281`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1654`, n `277`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1642`, n `277`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1531`, n `281`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1491`, n `281`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1453`, n `277`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1447`, n `277`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1441`, n `281`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1384`, n `277`, weak_sample_signal
