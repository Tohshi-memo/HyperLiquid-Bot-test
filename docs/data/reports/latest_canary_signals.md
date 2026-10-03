# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T20:37:28.825139+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0055` n `13`; crypto_alt avg `0.237` n `235`; crypto_major avg `0.0107` n `8`; equity avg `0.0082` n `143`; fx avg `-0.005` n `6`; index avg `-0.0038` n `26`; metal avg `0.0025` n `20`; unknown avg `9.3248` n `1079`
- 1h: commodity avg `-0.0074` n `13`; crypto_alt avg `0.4751` n `235`; crypto_major avg `0.153` n `8`; equity avg `0.039` n `143`; fx avg `0.0095` n `6`; index avg `-0.0041` n `26`; metal avg `-0.0032` n `20`; unknown avg `3.3691` n `1070`
- 4h: commodity avg `0.1131` n `13`; crypto_alt avg `0.4964` n `235`; crypto_major avg `0.3125` n `8`; equity avg `0.1022` n `143`; fx avg `-0.0112` n `6`; index avg `0.0128` n `26`; metal avg `-0.0011` n `20`; unknown avg `1.7301` n `1062`
- 24h: commodity avg `-0.0028` n `13`; crypto_alt avg `2.8753` n `235`; crypto_major avg `1.4558` n `8`; equity avg `0.1827` n `143`; fx avg `-0.0274` n `6`; index avg `0.0279` n `26`; metal avg `-0.0127` n `20`; unknown avg `1.6478` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1992`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1875`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1548`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
