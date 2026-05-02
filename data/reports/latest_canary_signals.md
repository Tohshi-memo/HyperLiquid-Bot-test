# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T19:40:14.510488+00:00`
- Correlation status: `ready`
- Asset price records: `101`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0092` n `7`; crypto_alt avg `0.0689` n `223`; crypto_major avg `-0.047` n `7`; equity avg `0.0547` n `42`; fx avg `0.0053` n `4`; index avg `0.0048` n `9`; metal avg `0.0078` n `7`; unknown avg `-0.052` n `313`
- 1h: commodity avg `-0.0236` n `7`; crypto_alt avg `0.2166` n `223`; crypto_major avg `0.0605` n `7`; equity avg `0.1001` n `42`; fx avg `0.0032` n `4`; index avg `0.021` n `9`; metal avg `-0.0041` n `7`; unknown avg `-0.0126` n `313`
- 4h: commodity avg `-0.1792` n `7`; crypto_alt avg `0.6029` n `223`; crypto_major avg `0.1394` n `7`; equity avg `0.315` n `42`; fx avg `0.0498` n `4`; index avg `0.0598` n `9`; metal avg `-0.0401` n `7`; unknown avg `0.0781` n `313`
- 24h: commodity avg `0.0097` n `7`; crypto_alt avg `1.5139` n `223`; crypto_major avg `0.2541` n `7`; equity avg `0.8485` n `42`; fx avg `-0.0255` n `4`; index avg `0.1042` n `9`; metal avg `-0.2824` n `7`; unknown avg `0.3985` n `311`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.5256`, n `93`, strong_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5099`, n `97`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.4975`, n `93`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4922`, n `97`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4508`, n `93`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.428`, n `93`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4248`, n `93`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4236`, n `97`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.4216`, n `93`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4167`, n `93`, moderate_sample_signal
