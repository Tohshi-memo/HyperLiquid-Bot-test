# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T13:00:25.267035+00:00`
- Correlation status: `ready`
- Asset price records: `75`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0002` n `7`; crypto_alt avg `-0.148` n `223`; crypto_major avg `-0.0144` n `7`; equity avg `0.0285` n `42`; fx avg `0.0003` n `4`; index avg `-0.0004` n `9`; metal avg `0.0081` n `7`; unknown avg `-0.0402` n `313`
- 1h: commodity avg `-0.001` n `7`; crypto_alt avg `0.1509` n `223`; crypto_major avg `0.0708` n `7`; equity avg `-0.0108` n `42`; fx avg `-0.0067` n `4`; index avg `0.0297` n `9`; metal avg `0.0204` n `7`; unknown avg `0.047` n `313`
- 4h: commodity avg `-0.0546` n `7`; crypto_alt avg `0.214` n `223`; crypto_major avg `-0.1232` n `7`; equity avg `0.051` n `42`; fx avg `-0.0075` n `4`; index avg `0.0302` n `9`; metal avg `0.0407` n `7`; unknown avg `-0.0288` n `313`
- 24h: crypto_alt avg `0.2765` n `223`; crypto_major avg `-0.302` n `7`; metal avg `0.327` n `1`; unknown avg `1.0352` n `310`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5663`, n `71`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5575`, n `67`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5476`, n `67`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5468`, n `71`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4908`, n `71`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4839`, n `67`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4807`, n `67`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4715`, n `67`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4576`, n `71`, moderate_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.4511`, n `71`, moderate_sample_signal
