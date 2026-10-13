# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T02:37:30.333980+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0384` n `13`; crypto_alt avg `-0.212` n `235`; crypto_major avg `0.1582` n `8`; equity avg `-0.1004` n `151`; fx avg `-0.0134` n `6`; index avg `-0.0294` n `26`; metal avg `0.0258` n `20`; unknown avg `0.3384` n `1135`
- 1h: commodity avg `-0.1252` n `13`; crypto_alt avg `0.4767` n `235`; crypto_major avg `0.9133` n `8`; equity avg `-0.0467` n `151`; fx avg `-0.0083` n `6`; index avg `-0.049` n `26`; metal avg `0.1147` n `20`; unknown avg `1.2572` n `1133`
- 4h: commodity avg `-0.1989` n `13`; crypto_alt avg `-1.1948` n `235`; crypto_major avg `-0.199` n `8`; equity avg `-1.3874` n `151`; fx avg `0.0483` n `6`; index avg `-0.3301` n `26`; metal avg `-0.0698` n `20`; unknown avg `3.5782` n `1127`
- 24h: commodity avg `0.6623` n `13`; crypto_alt avg `-5.4315` n `235`; crypto_major avg `-3.0361` n `8`; equity avg `-4.2978` n `151`; fx avg `-0.0442` n `6`; index avg `-0.6448` n `26`; metal avg `-0.3236` n `20`; unknown avg `0.48` n `853`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2123`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1964`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1266`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1091`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1084`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1033`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0956`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0944`, n `666`, weak_sample_signal
