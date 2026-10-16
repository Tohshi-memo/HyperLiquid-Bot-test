# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T07:52:28.357155+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0036` n `13`; crypto_alt avg `-0.0111` n `236`; crypto_major avg `0.0511` n `8`; equity avg `-0.0846` n `151`; fx avg `0.0269` n `6`; index avg `-0.0329` n `26`; metal avg `-0.0065` n `20`; unknown avg `7.4483` n `1136`
- 1h: commodity avg `-0.0281` n `13`; crypto_alt avg `-0.3373` n `236`; crypto_major avg `-0.1381` n `8`; equity avg `-0.047` n `151`; fx avg `0.0329` n `6`; index avg `-0.0192` n `26`; metal avg `0.0662` n `20`; unknown avg `6.1873` n `1134`
- 4h: commodity avg `0.1664` n `13`; crypto_alt avg `0.7951` n `236`; crypto_major avg `0.432` n `8`; equity avg `-0.3322` n `151`; fx avg `-0.0762` n `6`; index avg `-0.084` n `26`; metal avg `0.0116` n `20`; unknown avg `4.5182` n `1102`
- 24h: commodity avg `0.1218` n `13`; crypto_alt avg `4.4174` n `236`; crypto_major avg `1.9693` n `8`; equity avg `2.3417` n `151`; fx avg `0.0327` n `6`; index avg `0.285` n `26`; metal avg `0.4507` n `20`; unknown avg `28.9371` n `904`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.0976`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0945`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.092`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0904`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0754`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
