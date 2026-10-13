# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T08:52:28.837663+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0404` n `13`; crypto_alt avg `-0.1605` n `235`; crypto_major avg `-0.2643` n `8`; equity avg `-0.0623` n `151`; fx avg `-0.0244` n `6`; index avg `-0.0198` n `26`; metal avg `-0.0375` n `20`; unknown avg `0.2155` n `1135`
- 1h: commodity avg `-0.0257` n `13`; crypto_alt avg `-0.4146` n `235`; crypto_major avg `-0.42` n `8`; equity avg `0.3252` n `151`; fx avg `-0.0614` n `6`; index avg `0.0087` n `26`; metal avg `-0.017` n `20`; unknown avg `0.6231` n `1117`
- 4h: commodity avg `-0.0692` n `13`; crypto_alt avg `0.0278` n `235`; crypto_major avg `0.0815` n `8`; equity avg `0.5947` n `151`; fx avg `-0.0098` n `6`; index avg `0.1447` n `26`; metal avg `0.0051` n `20`; unknown avg `1.2575` n `1099`
- 24h: commodity avg `0.1347` n `13`; crypto_alt avg `-3.56` n `235`; crypto_major avg `-2.0389` n `8`; equity avg `-2.5997` n `151`; fx avg `0.0423` n `6`; index avg `-0.354` n `26`; metal avg `0.0839` n `20`; unknown avg `0.1173` n `897`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1855`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1671`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1569`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1366`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0831`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.075`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0741`, n `666`, weak_sample_signal
