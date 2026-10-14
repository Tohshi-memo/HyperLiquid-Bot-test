# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T12:37:30.472766+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0555` n `13`; crypto_alt avg `-0.6983` n `235`; crypto_major avg `-0.8483` n `8`; equity avg `-0.9553` n `151`; fx avg `-0.0691` n `6`; index avg `-0.2195` n `26`; metal avg `-0.2832` n `20`; unknown avg `2.569` n `1136`
- 1h: commodity avg `-0.1386` n `13`; crypto_alt avg `-0.6684` n `235`; crypto_major avg `-0.6671` n `8`; equity avg `-0.7837` n `151`; fx avg `-0.0492` n `6`; index avg `-0.1701` n `26`; metal avg `-0.1885` n `20`; unknown avg `1.5278` n `1128`
- 4h: commodity avg `-0.0589` n `13`; crypto_alt avg `-1.2699` n `235`; crypto_major avg `-0.8738` n `8`; equity avg `-1.2485` n `151`; fx avg `-0.045` n `6`; index avg `-0.2135` n `26`; metal avg `-0.2424` n `20`; unknown avg `2.6322` n `1047`
- 24h: commodity avg `0.8806` n `13`; crypto_alt avg `-0.7228` n `235`; crypto_major avg `-0.4262` n `8`; equity avg `-0.744` n `151`; fx avg `-0.0536` n `6`; index avg `-0.1483` n `26`; metal avg `-0.5709` n `20`; unknown avg `1269.0135` n `975`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.15`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1272`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1057`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0711`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0709`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
