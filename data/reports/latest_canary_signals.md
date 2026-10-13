# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T02:52:27.774955+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0219` n `13`; crypto_alt avg `-0.1124` n `235`; crypto_major avg `0.0302` n `8`; equity avg `-0.1454` n `151`; fx avg `0.0396` n `6`; index avg `-0.0159` n `26`; metal avg `-0.0039` n `20`; unknown avg `0.2276` n `1135`
- 1h: commodity avg `-0.087` n `13`; crypto_alt avg `0.1789` n `235`; crypto_major avg `0.6839` n `8`; equity avg `-0.1998` n `151`; fx avg `0.0406` n `6`; index avg `-0.0524` n `26`; metal avg `0.1242` n `20`; unknown avg `0.8074` n `1133`
- 4h: commodity avg `-0.2213` n `13`; crypto_alt avg `-1.2001` n `235`; crypto_major avg `-0.0656` n `8`; equity avg `-1.4589` n `151`; fx avg `0.0901` n `6`; index avg `-0.3277` n `26`; metal avg `-0.064` n `20`; unknown avg `1.653` n `1127`
- 24h: commodity avg `0.6527` n `13`; crypto_alt avg `-5.5333` n `235`; crypto_major avg `-2.9286` n `8`; equity avg `-4.426` n `151`; fx avg `-0.0136` n `6`; index avg `-0.6579` n `26`; metal avg `-0.3038` n `20`; unknown avg `0.4716` n `853`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.213`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1974`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1285`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1095`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1087`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1046`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0978`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0963`, n `666`, weak_sample_signal
