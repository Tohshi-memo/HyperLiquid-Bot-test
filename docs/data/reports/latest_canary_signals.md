# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T02:52:28.406329+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0098` n `13`; crypto_alt avg `0.3391` n `235`; crypto_major avg `0.279` n `8`; equity avg `0.1191` n `151`; fx avg `-0.006` n `6`; index avg `0.0211` n `26`; metal avg `0.0365` n `20`; unknown avg `0.6453` n `1135`
- 1h: commodity avg `-0.0436` n `13`; crypto_alt avg `0.2278` n `235`; crypto_major avg `0.1776` n `8`; equity avg `0.2177` n `151`; fx avg `-0.018` n `6`; index avg `0.0377` n `26`; metal avg `0.1294` n `20`; unknown avg `-0.1242` n `1133`
- 4h: commodity avg `0.081` n `13`; crypto_alt avg `0.4122` n `235`; crypto_major avg `0.2689` n `8`; equity avg `0.1258` n `151`; fx avg `-0.0025` n `6`; index avg `0.0279` n `26`; metal avg `0.0528` n `20`; unknown avg `-0.0983` n `1127`
- 24h: commodity avg `1.0739` n `13`; crypto_alt avg `1.6256` n `235`; crypto_major avg `0.8297` n `8`; equity avg `1.3078` n `151`; fx avg `0.0626` n `6`; index avg `0.2476` n `26`; metal avg `-0.1614` n `20`; unknown avg `0.8196` n `947`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1513`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1361`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1106`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0899`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0733`, n `666`, weak_sample_signal
