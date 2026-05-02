# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T08:45:46.009183+00:00`
- Correlation status: `ready`
- Asset price records: `58`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0053` n `7`; crypto_alt avg `0.0391` n `223`; crypto_major avg `0.0247` n `7`; equity avg `0.0538` n `42`; fx avg `0.0144` n `4`; index avg `0.0036` n `9`; metal avg `-0.0001` n `7`; unknown avg `-0.0413` n `313`
- 1h: commodity avg `0.0163` n `7`; crypto_alt avg `0.0091` n `223`; crypto_major avg `0.1532` n `7`; equity avg `0.1086` n `42`; fx avg `0.0464` n `4`; index avg `-0.0021` n `9`; metal avg `0.0128` n `7`; unknown avg `0.1154` n `313`
- 4h: commodity avg `0.0272` n `7`; crypto_alt avg `0.1986` n `223`; crypto_major avg `0.2121` n `7`; equity avg `0.3267` n `42`; fx avg `-0.0504` n `4`; index avg `-0.0047` n `9`; metal avg `0.0746` n `7`; unknown avg `0.1843` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5933`, n `54`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5851`, n `50`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5726`, n `54`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5365`, n `50`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4816`, n `54`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4575`, n `50`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4456`, n `54`, moderate_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.4419`, n `54`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4394`, n `50`, moderate_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.4326`, n `54`, moderate_sample_signal
