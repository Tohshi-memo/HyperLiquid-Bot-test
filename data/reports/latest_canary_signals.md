# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T21:07:31.396171+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0182` n `13`; crypto_alt avg `0.1356` n `237`; crypto_major avg `0.1548` n `8`; equity avg `0.0426` n `151`; fx avg `0.0022` n `6`; index avg `-0.0031` n `26`; metal avg `0.0117` n `20`; unknown avg `-0.0104` n `1182`
- 1h: commodity avg `-0.0282` n `13`; crypto_alt avg `-0.0166` n `237`; crypto_major avg `0.1977` n `8`; equity avg `0.0984` n `151`; fx avg `0.0048` n `6`; index avg `0.0123` n `26`; metal avg `-0.0023` n `20`; unknown avg `-0.0016` n `1148`
- 4h: commodity avg `-0.2277` n `13`; crypto_alt avg `-0.2116` n `237`; crypto_major avg `0.0299` n `8`; equity avg `-0.2278` n `151`; fx avg `0.0191` n `6`; index avg `-0.0183` n `26`; metal avg `-0.0058` n `20`; unknown avg `-0.1559` n `1122`
- 24h: commodity avg `-0.3185` n `13`; crypto_alt avg `3.0091` n `237`; crypto_major avg `2.3076` n `8`; equity avg `2.9608` n `151`; fx avg `0.0245` n `6`; index avg `0.5732` n `26`; metal avg `0.1122` n `20`; unknown avg `3.1174` n `908`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1937`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.141`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
