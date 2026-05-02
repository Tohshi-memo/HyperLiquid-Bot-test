# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T12:03:27.377952+00:00`
- Correlation status: `ready`
- Asset price records: `71`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0452` n `7`; crypto_alt avg `0.1231` n `223`; crypto_major avg `0.0852` n `7`; equity avg `-0.0013` n `42`; fx avg `0.0155` n `4`; index avg `0.0071` n `9`; metal avg `0.0033` n `7`; unknown avg `-0.0277` n `313`
- 1h: commodity avg `-0.0687` n `7`; crypto_alt avg `0.0484` n `223`; crypto_major avg `-0.0502` n `7`; equity avg `0.0364` n `42`; fx avg `0.0016` n `4`; index avg `0.0141` n `9`; metal avg `-0.0036` n `7`; unknown avg `-0.0938` n `313`
- 4h: commodity avg `-0.025` n `7`; crypto_alt avg `0.1985` n `223`; crypto_major avg `-0.0276` n `7`; equity avg `-0.0091` n `42`; fx avg `0.0381` n `4`; index avg `0.0232` n `9`; metal avg `0.033` n `7`; unknown avg `-0.0429` n `313`
- 24h: crypto_alt avg `0.7572` n `223`; crypto_major avg `0.541` n `7`; metal avg `0.7829` n `1`; unknown avg `1.2939` n `310`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5738`, n `67`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.554`, n `67`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5494`, n `63`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5391`, n `63`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4882`, n `67`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4754`, n `63`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4711`, n `63`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4622`, n `63`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4537`, n `67`, moderate_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.4476`, n `67`, moderate_sample_signal
