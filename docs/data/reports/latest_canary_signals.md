# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T12:00:24.966033+00:00`
- Correlation status: `ready`
- Asset price records: `71`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0406` n `7`; crypto_alt avg `0.1172` n `223`; crypto_major avg `0.0757` n `7`; equity avg `0.0018` n `42`; fx avg `0.0155` n `4`; index avg `0.0165` n `9`; metal avg `0.0073` n `7`; unknown avg `-0.009` n `313`
- 1h: commodity avg `-0.0641` n `7`; crypto_alt avg `0.0425` n `223`; crypto_major avg `-0.0597` n `7`; equity avg `0.0395` n `42`; fx avg `0.0016` n `4`; index avg `0.0234` n `9`; metal avg `0.0005` n `7`; unknown avg `-0.075` n `313`
- 4h: commodity avg `-0.0203` n `7`; crypto_alt avg `0.1916` n `223`; crypto_major avg `-0.037` n `7`; equity avg `-0.006` n `42`; fx avg `0.0381` n `4`; index avg `0.0325` n `9`; metal avg `0.0371` n `7`; unknown avg `-0.0229` n `313`
- 24h: crypto_alt avg `0.747` n `223`; crypto_major avg `0.5313` n `7`; metal avg `0.7818` n `1`; unknown avg `1.3138` n `310`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5738`, n `67`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.554`, n `67`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.549`, n `63`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5387`, n `63`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4872`, n `67`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4752`, n `63`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4708`, n `63`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.462`, n `63`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4529`, n `67`, moderate_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.4463`, n `67`, moderate_sample_signal
