# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T04:07:30.037705+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0135` n `12`; crypto_alt avg `0.1214` n `233`; crypto_major avg `0.1108` n `8`; equity avg `0.0575` n `134`; fx avg `-0.0041` n `6`; index avg `0.0083` n `26`; metal avg `0.0526` n `20`; unknown avg `-0.065` n `795`
- 1h: commodity avg `0.0195` n `12`; crypto_alt avg `0.0042` n `233`; crypto_major avg `-0.0483` n `8`; equity avg `0.018` n `134`; fx avg `-0.0232` n `6`; index avg `0.0121` n `26`; metal avg `-0.0039` n `20`; unknown avg `-0.377` n `795`
- 4h: commodity avg `-0.1633` n `12`; crypto_alt avg `-0.2394` n `233`; crypto_major avg `0.1889` n `8`; equity avg `-0.3106` n `134`; fx avg `-0.0319` n `6`; index avg `-0.0276` n `26`; metal avg `0.0623` n `20`; unknown avg `8.1363` n `789`
- 24h: commodity avg `-0.0059` n `12`; crypto_alt avg `-2.9694` n `233`; crypto_major avg `-1.953` n `8`; equity avg `-1.0421` n `134`; fx avg `0.0069` n `6`; index avg `-0.1623` n `26`; metal avg `0.4677` n `20`; unknown avg `1.3255` n `668`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
