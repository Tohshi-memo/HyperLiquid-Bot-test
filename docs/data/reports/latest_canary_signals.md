# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T03:45:17.868437+00:00`
- Correlation status: `ready`
- Asset price records: `134`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0076` n `7`; crypto_alt avg `0.1254` n `223`; crypto_major avg `0.0486` n `7`; equity avg `0.0207` n `42`; fx avg `0.0016` n `4`; index avg `0.0004` n `9`; metal avg `0.0005` n `7`; unknown avg `0.0329` n `313`
- 1h: commodity avg `0.0286` n `7`; crypto_alt avg `-0.0445` n `223`; crypto_major avg `0.0834` n `7`; equity avg `0.0153` n `42`; fx avg `0.0013` n `4`; index avg `-0.0098` n `9`; metal avg `0.0185` n `7`; unknown avg `-0.015` n `313`
- 4h: commodity avg `0.0048` n `7`; crypto_alt avg `-1.341` n `223`; crypto_major avg `-0.7178` n `7`; equity avg `-0.1198` n `42`; fx avg `0.0011` n `4`; index avg `-0.0286` n `9`; metal avg `0.0163` n `7`; unknown avg `0.1642` n `313`
- 24h: commodity avg `-0.1241` n `7`; crypto_alt avg `0.7483` n `223`; crypto_major avg `-0.2803` n `7`; equity avg `0.5212` n `42`; fx avg `0.0147` n `4`; index avg `-0.0095` n `9`; metal avg `0.0566` n `7`; unknown avg `0.301` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4479`, n `130`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4327`, n `130`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.4292`, n `130`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.4214`, n `130`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.4185`, n `130`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4129`, n `126`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4104`, n `126`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4039`, n `130`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.402`, n `126`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3968`, n `126`, moderate_sample_signal
