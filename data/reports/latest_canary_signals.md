# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T17:45:19.263983+00:00`
- Correlation status: `ready`
- Asset price records: `94`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0651` n `7`; crypto_alt avg `-0.0981` n `223`; crypto_major avg `-0.0596` n `7`; equity avg `0.0238` n `42`; fx avg `0.0` n `4`; index avg `0.0012` n `9`; metal avg `-0.0221` n `7`; unknown avg `-0.0285` n `313`
- 1h: commodity avg `-0.1131` n `7`; crypto_alt avg `-0.0025` n `223`; crypto_major avg `-0.0711` n `7`; equity avg `0.0184` n `42`; fx avg `0.0298` n `4`; index avg `0.0083` n `9`; metal avg `-0.0172` n `7`; unknown avg `-0.0138` n `313`
- 4h: commodity avg `-0.1368` n `7`; crypto_alt avg `0.9843` n `223`; crypto_major avg `0.0518` n `7`; equity avg `0.0012` n `42`; fx avg `0.093` n `4`; index avg `0.0031` n `9`; metal avg `-0.0082` n `7`; unknown avg `0.0393` n `313`
- 24h: commodity avg `0.2466` n `7`; crypto_alt avg `1.4628` n `223`; crypto_major avg `0.3199` n `7`; equity avg `0.6613` n `42`; fx avg `-0.0447` n `4`; index avg `0.136` n `9`; metal avg `-0.4793` n `7`; unknown avg `0.8427` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5269`, n `90`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5194`, n `86`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5085`, n `90`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.4897`, n `86`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4686`, n `86`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4559`, n `86`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.451`, n `90`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4488`, n `86`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4184`, n `90`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4124`, n `86`, moderate_sample_signal
