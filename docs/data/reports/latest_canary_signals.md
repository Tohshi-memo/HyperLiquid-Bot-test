# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T01:07:27.270296+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0` n `5`; crypto_alt avg `0.023` n `225`; crypto_major avg `-0.0557` n `7`; equity avg `0.0207` n `8`; fx avg `0.0796` n `1`; index avg `-0.0492` n `4`; metal avg `0.0394` n `20`; unknown avg `0.2744` n `947`
- 1h: commodity avg `0.0` n `5`; crypto_alt avg `-0.2934` n `225`; crypto_major avg `-0.2931` n `7`; equity avg `-0.4389` n `8`; fx avg `-0.0362` n `1`; index avg `-0.2849` n `4`; metal avg `-0.1123` n `20`; unknown avg `0.2072` n `947`
- 4h: commodity avg `0.0` n `5`; crypto_alt avg `-1.2605` n `225`; crypto_major avg `-0.5211` n `7`; equity avg `-0.5216` n `8`; fx avg `-0.2742` n `1`; index avg `-0.91` n `4`; metal avg `0.0033` n `20`; unknown avg `0.2007` n `947`
- 24h: commodity avg `0.0` n `5`; crypto_alt avg `2.0549` n `225`; crypto_major avg `0.1295` n `7`; equity avg `-0.0877` n `8`; fx avg `-0.2742` n `1`; index avg `-0.2974` n `4`; metal avg `0.1081` n `20`; unknown avg `4.8944` n `930`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
