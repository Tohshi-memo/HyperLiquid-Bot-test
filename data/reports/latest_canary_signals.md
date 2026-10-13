# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T08:37:38.103522+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0578` n `13`; crypto_alt avg `-0.0532` n `235`; crypto_major avg `-0.1077` n `8`; equity avg `0.0418` n `151`; fx avg `-0.0228` n `6`; index avg `0.0168` n `26`; metal avg `-0.0119` n `20`; unknown avg `0.0356` n `1135`
- 1h: commodity avg `-0.0961` n `13`; crypto_alt avg `-0.2785` n `235`; crypto_major avg `-0.1252` n `8`; equity avg `0.564` n `151`; fx avg `-0.0248` n `6`; index avg `0.0729` n `26`; metal avg `0.0078` n `20`; unknown avg `1.2972` n `1117`
- 4h: commodity avg `-0.0832` n `13`; crypto_alt avg `0.3528` n `235`; crypto_major avg `0.3281` n `8`; equity avg `0.6086` n `151`; fx avg `0.0126` n `6`; index avg `0.1425` n `26`; metal avg `0.0574` n `20`; unknown avg `1.336` n `1097`
- 24h: commodity avg `0.1602` n `13`; crypto_alt avg `-3.6015` n `235`; crypto_major avg `-1.974` n `8`; equity avg `-2.7632` n `151`; fx avg `0.0654` n `6`; index avg `-0.3713` n `26`; metal avg `0.0604` n `20`; unknown avg `0.2671` n `883`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1872`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1684`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1547`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1347`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0852`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.076`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0751`, n `666`, weak_sample_signal
