# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T17:00:29.021241+00:00`
- Correlation status: `ready`
- Asset price records: `91`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0097` n `7`; crypto_alt avg `0.2846` n `223`; crypto_major avg `0.0957` n `7`; equity avg `-0.0133` n `42`; fx avg `0.0319` n `4`; index avg `0.0023` n `9`; metal avg `0.0006` n `7`; unknown avg `0.0304` n `313`
- 1h: commodity avg `-0.0139` n `7`; crypto_alt avg `0.365` n `223`; crypto_major avg `0.0878` n `7`; equity avg `0.0066` n `42`; fx avg `0.0373` n `4`; index avg `-0.0052` n `9`; metal avg `0.0108` n `7`; unknown avg `-0.0319` n `313`
- 4h: commodity avg `-0.0343` n `7`; crypto_alt avg `1.5662` n `223`; crypto_major avg `0.4703` n `7`; equity avg `0.0388` n `42`; fx avg `0.0786` n `4`; index avg `-0.001` n `9`; metal avg `-0.025` n `7`; unknown avg `0.1221` n `313`
- 24h: commodity avg `0.612` n `7`; crypto_alt avg `1.509` n `223`; crypto_major avg `0.2228` n `7`; equity avg `0.3312` n `42`; fx avg `-0.0497` n `4`; index avg `0.1859` n `9`; metal avg `-0.6601` n `7`; unknown avg `0.6501` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5266`, n `87`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5236`, n `83`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5082`, n `87`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.4952`, n `83`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4748`, n `83`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4734`, n `83`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4604`, n `83`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4543`, n `87`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4267`, n `83`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4261`, n `87`, moderate_sample_signal
