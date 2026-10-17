# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T16:37:30.776760+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0034` n `13`; crypto_alt avg `-0.2633` n `236`; crypto_major avg `-0.1069` n `8`; equity avg `-0.0012` n `151`; fx avg `0.0068` n `6`; index avg `0.0071` n `26`; metal avg `-0.0112` n `20`; unknown avg `0.4749` n `1185`
- 1h: commodity avg `-0.0545` n `13`; crypto_alt avg `-0.3788` n `236`; crypto_major avg `-0.2803` n `8`; equity avg `-0.0335` n `151`; fx avg `-0.0021` n `6`; index avg `-0.0185` n `26`; metal avg `-0.0286` n `20`; unknown avg `-0.5143` n `1177`
- 4h: commodity avg `0.0765` n `13`; crypto_alt avg `-1.2191` n `236`; crypto_major avg `-0.6137` n `8`; equity avg `-0.2549` n `151`; fx avg `-0.0315` n `6`; index avg `-0.0461` n `26`; metal avg `-0.0507` n `20`; unknown avg `1.1306` n `1159`
- 24h: commodity avg `0.1253` n `13`; crypto_alt avg `-2.629` n `236`; crypto_major avg `-1.1069` n `8`; equity avg `-1.496` n `151`; fx avg `-0.0049` n `6`; index avg `-0.2721` n `26`; metal avg `-0.0742` n `20`; unknown avg `3.1563` n `1048`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1712`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1459`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1145`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1124`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0721`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
