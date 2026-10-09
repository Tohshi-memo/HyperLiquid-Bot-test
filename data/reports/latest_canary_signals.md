# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T01:37:31.858814+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0176` n `13`; crypto_alt avg `0.2428` n `235`; crypto_major avg `0.1499` n `8`; equity avg `0.1936` n `150`; fx avg `-0.0047` n `6`; index avg `0.0175` n `26`; metal avg `0.045` n `20`; unknown avg `0.1489` n `1078`
- 1h: commodity avg `-0.0442` n `13`; crypto_alt avg `0.4134` n `235`; crypto_major avg `0.0411` n `8`; equity avg `0.0785` n `150`; fx avg `-0.0177` n `6`; index avg `-0.0145` n `26`; metal avg `0.2087` n `20`; unknown avg `0.1232` n `1076`
- 4h: commodity avg `-0.0982` n `13`; crypto_alt avg `0.3994` n `235`; crypto_major avg `-0.0107` n `8`; equity avg `0.2361` n `150`; fx avg `0.0272` n `6`; index avg `0.0447` n `26`; metal avg `0.3712` n `20`; unknown avg `0.369` n `1069`
- 24h: commodity avg `0.451` n `13`; crypto_alt avg `-3.2592` n `235`; crypto_major avg `-3.7335` n `8`; equity avg `-2.6495` n `150`; fx avg `0.1452` n `6`; index avg `-0.3101` n `26`; metal avg `0.0224` n `20`; unknown avg `5.8511` n `991`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1784`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1616`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
