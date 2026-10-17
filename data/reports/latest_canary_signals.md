# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T00:22:31.834398+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1402` n `13`; crypto_alt avg `-0.2109` n `236`; crypto_major avg `-0.0977` n `8`; equity avg `-0.0599` n `151`; fx avg `-0.0024` n `6`; index avg `-0.0087` n `26`; metal avg `-0.0038` n `20`; unknown avg `-0.1695` n `1193`
- 1h: commodity avg `0.1905` n `13`; crypto_alt avg `0.0267` n `236`; crypto_major avg `-0.1586` n `8`; equity avg `0.2454` n `151`; fx avg `0.0079` n `6`; index avg `0.0237` n `26`; metal avg `0.0057` n `20`; unknown avg `0.7804` n `1185`
- 4h: commodity avg `0.2485` n `13`; crypto_alt avg `0.6434` n `236`; crypto_major avg `0.3899` n `8`; equity avg `-0.1575` n `151`; fx avg `0.0111` n `6`; index avg `-0.0174` n `26`; metal avg `0.0162` n `20`; unknown avg `0.8831` n `1177`
- 24h: commodity avg `0.6273` n `13`; crypto_alt avg `-1.1827` n `236`; crypto_major avg `-1.0856` n `8`; equity avg `-3.1446` n `151`; fx avg `0.0366` n `6`; index avg `-0.4998` n `26`; metal avg `0.0222` n `20`; unknown avg `39.9936` n `910`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1694`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.118`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1132`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0904`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.077`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
