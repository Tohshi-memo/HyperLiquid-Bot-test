# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T20:37:29.558053+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0187` n `13`; crypto_alt avg `0.5129` n `237`; crypto_major avg `0.3338` n `8`; equity avg `0.3777` n `151`; fx avg `-0.0026` n `6`; index avg `0.0366` n `26`; metal avg `0.0084` n `20`; unknown avg `1.9972` n `1183`
- 1h: commodity avg `-0.0761` n `13`; crypto_alt avg `0.5238` n `237`; crypto_major avg `0.5187` n `8`; equity avg `0.3887` n `151`; fx avg `-0.006` n `6`; index avg `0.0784` n `26`; metal avg `0.038` n `20`; unknown avg `50.3683` n `1147`
- 4h: commodity avg `0.1829` n `13`; crypto_alt avg `0.4598` n `237`; crypto_major avg `0.5541` n `8`; equity avg `0.0203` n `151`; fx avg `-0.0102` n `6`; index avg `-0.002` n `26`; metal avg `-0.019` n `20`; unknown avg `68.4913` n `1133`
- 24h: commodity avg `-0.1193` n `13`; crypto_alt avg `2.9219` n `237`; crypto_major avg `1.8635` n `8`; equity avg `0.4555` n `151`; fx avg `0.0236` n `6`; index avg `0.0468` n `26`; metal avg `0.0442` n `20`; unknown avg `5.4287` n `1034`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1816`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
