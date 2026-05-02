# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T21:00:25.989282+00:00`
- Correlation status: `ready`
- Asset price records: `107`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0298` n `7`; crypto_alt avg `0.0845` n `223`; crypto_major avg `0.0768` n `7`; equity avg `0.1365` n `42`; fx avg `0.0064` n `4`; index avg `0.0032` n `9`; metal avg `-0.0011` n `7`; unknown avg `-0.0037` n `313`
- 1h: commodity avg `0.0224` n `7`; crypto_alt avg `-0.0264` n `223`; crypto_major avg `0.0437` n `7`; equity avg `0.2466` n `42`; fx avg `0.0112` n `4`; index avg `0.0105` n `9`; metal avg `-0.007` n `7`; unknown avg `0.1312` n `313`
- 4h: commodity avg `-0.1463` n `7`; crypto_alt avg `0.09` n `223`; crypto_major avg `-0.0378` n `7`; equity avg `0.503` n `42`; fx avg `0.0154` n `4`; index avg `0.057` n `9`; metal avg `-0.0476` n `7`; unknown avg `0.1156` n `313`
- 24h: commodity avg `-0.0055` n `7`; crypto_alt avg `1.617` n `223`; crypto_major avg `0.2966` n `7`; equity avg `1.1382` n `42`; fx avg `-0.009` n `4`; index avg `0.0723` n `9`; metal avg `-0.1002` n `7`; unknown avg `0.3013` n `311`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.5318`, n `99`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5245`, n `99`, strong_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5071`, n `103`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4895`, n `103`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4571`, n `99`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4289`, n `99`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.4253`, n `99`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4188`, n `99`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4175`, n `99`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4168`, n `103`, moderate_sample_signal
