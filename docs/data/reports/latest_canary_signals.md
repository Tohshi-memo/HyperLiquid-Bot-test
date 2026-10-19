# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T17:07:40.965745+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0708` n `13`; crypto_alt avg `-0.2101` n `237`; crypto_major avg `-0.0122` n `8`; equity avg `-0.0463` n `151`; fx avg `-0.005` n `6`; index avg `-0.0153` n `26`; metal avg `-0.0012` n `20`; unknown avg `0.0184` n `1194`
- 1h: commodity avg `0.0697` n `13`; crypto_alt avg `0.1977` n `237`; crypto_major avg `0.1596` n `8`; equity avg `-0.4637` n `151`; fx avg `0.0032` n `6`; index avg `-0.0717` n `26`; metal avg `0.0061` n `20`; unknown avg `0.0915` n `1194`
- 4h: commodity avg `0.2542` n `13`; crypto_alt avg `-0.3519` n `237`; crypto_major avg `-0.7595` n `8`; equity avg `-0.6777` n `151`; fx avg `-0.0113` n `6`; index avg `-0.0468` n `26`; metal avg `-0.1233` n `20`; unknown avg `-0.01` n `1133`
- 24h: commodity avg `-0.0592` n `13`; crypto_alt avg `1.2679` n `237`; crypto_major avg `1.5117` n `8`; equity avg `2.8577` n `151`; fx avg `-0.033` n `6`; index avg `0.5394` n `26`; metal avg `0.074` n `20`; unknown avg `2.8423` n `916`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1991`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1463`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
