# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T04:37:28.216967+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0042` n `13`; crypto_alt avg `0.4034` n `235`; crypto_major avg `0.2571` n `8`; equity avg `-0.0375` n `151`; fx avg `0.0033` n `6`; index avg `-0.0071` n `26`; metal avg `0.0324` n `20`; unknown avg `0.7273` n `1135`
- 1h: commodity avg `-0.0345` n `13`; crypto_alt avg `0.0301` n `235`; crypto_major avg `-0.055` n `8`; equity avg `-0.0894` n `151`; fx avg `0.0066` n `6`; index avg `0.0031` n `26`; metal avg `0.0036` n `20`; unknown avg `-0.2175` n `1127`
- 4h: commodity avg `-0.1022` n `13`; crypto_alt avg `0.1072` n `235`; crypto_major avg `0.1447` n `8`; equity avg `-0.2231` n `151`; fx avg `-0.024` n `6`; index avg `0.0025` n `26`; metal avg `0.1191` n `20`; unknown avg `0.1659` n `1127`
- 24h: commodity avg `1.075` n `13`; crypto_alt avg `0.2275` n `235`; crypto_major avg `0.1937` n `8`; equity avg `0.6888` n `151`; fx avg `0.0674` n `6`; index avg `0.197` n `26`; metal avg `-0.2943` n `20`; unknown avg `1.4826` n `979`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1531`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1364`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.114`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0874`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0739`, n `666`, weak_sample_signal
