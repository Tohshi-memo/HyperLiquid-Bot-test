# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T16:52:28.952969+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0514` n `12`; crypto_alt avg `-0.2614` n `234`; crypto_major avg `-0.3517` n `8`; equity avg `-0.2794` n `141`; fx avg `0.0074` n `6`; index avg `-0.0486` n `26`; metal avg `-0.083` n `20`; unknown avg `0.3033` n `962`
- 1h: commodity avg `-0.3663` n `12`; crypto_alt avg `0.9087` n `234`; crypto_major avg `0.5657` n `8`; equity avg `0.5257` n `141`; fx avg `-0.0084` n `6`; index avg `0.1036` n `26`; metal avg `0.0866` n `20`; unknown avg `12.324` n `954`
- 4h: commodity avg `-0.1741` n `12`; crypto_alt avg `-1.1005` n `234`; crypto_major avg `-0.5319` n `8`; equity avg `-0.8039` n `141`; fx avg `0.0174` n `6`; index avg `-0.1237` n `26`; metal avg `-0.0979` n `20`; unknown avg `65.8955` n `904`
- 24h: commodity avg `-0.341` n `12`; crypto_alt avg `-2.7594` n `234`; crypto_major avg `-1.36` n `8`; equity avg `-3.0627` n `141`; fx avg `0.0281` n `6`; index avg `-0.2761` n `26`; metal avg `-1.0278` n `20`; unknown avg `21.613` n `786`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1835`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1707`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1654`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
