# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T21:07:31.549633+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0277` n `12`; crypto_alt avg `0.1925` n `228`; crypto_major avg `0.2` n `8`; equity avg `0.0227` n `88`; fx avg `0.0012` n `6`; index avg `0.0057` n `25`; metal avg `-0.0173` n `20`; unknown avg `-0.0267` n `763`
- 1h: commodity avg `0.0434` n `12`; crypto_alt avg `0.3911` n `228`; crypto_major avg `0.1274` n `8`; equity avg `0.151` n `88`; fx avg `0.0012` n `6`; index avg `0.0217` n `25`; metal avg `-0.0066` n `20`; unknown avg `0.7893` n `763`
- 4h: commodity avg `-0.0507` n `12`; crypto_alt avg `-0.1524` n `228`; crypto_major avg `0.0503` n `8`; equity avg `-0.6805` n `88`; fx avg `0.0112` n `6`; index avg `-0.1075` n `25`; metal avg `-0.3557` n `20`; unknown avg `0.5555` n `761`
- 24h: commodity avg `-0.588` n `12`; crypto_alt avg `2.053` n `228`; crypto_major avg `1.5869` n `8`; equity avg `-1.6297` n `88`; fx avg `0.0094` n `6`; index avg `-0.5263` n `25`; metal avg `0.1878` n `20`; unknown avg `0.7896` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
