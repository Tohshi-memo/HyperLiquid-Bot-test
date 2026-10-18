# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T22:37:28.889992+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0704` n `13`; crypto_alt avg `0.07` n `237`; crypto_major avg `0.0322` n `8`; equity avg `0.193` n `151`; fx avg `0.006` n `6`; index avg `0.0137` n `26`; metal avg `0.0219` n `20`; unknown avg `2.0471` n `1194`
- 1h: commodity avg `-0.3797` n `13`; crypto_alt avg `1.7838` n `237`; crypto_major avg `1.3242` n `8`; equity avg `1.2267` n `151`; fx avg `0.0523` n `6`; index avg `0.2826` n `26`; metal avg `0.2474` n `20`; unknown avg `3.6636` n `1142`
- 4h: commodity avg `-0.324` n `13`; crypto_alt avg `0.5982` n `237`; crypto_major avg `1.0877` n `8`; equity avg `1.1303` n `151`; fx avg `-0.009` n `6`; index avg `0.27` n `26`; metal avg `0.2139` n `20`; unknown avg `9.0102` n `1088`
- 24h: commodity avg `-0.3197` n `13`; crypto_alt avg `-2.0691` n `236`; crypto_major avg `0.1731` n `8`; equity avg `0.9679` n `151`; fx avg `0.0044` n `6`; index avg `0.2564` n `26`; metal avg `0.2249` n `20`; unknown avg `2.2142` n `961`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2019`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1359`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1357`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1165`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0816`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0759`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.071`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
