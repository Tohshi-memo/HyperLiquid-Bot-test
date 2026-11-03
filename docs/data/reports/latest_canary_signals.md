# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T16:22:36.821369+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0319` n `13`; crypto_alt avg `-0.4401` n `239`; crypto_major avg `-0.3796` n `8`; equity avg `-0.4505` n `158`; fx avg `0.0122` n `6`; index avg `-0.0619` n `27`; metal avg `-0.0184` n `20`; unknown avg `0.1959` n `1263`
- 1h: commodity avg `-0.0554` n `13`; crypto_alt avg `0.0285` n `239`; crypto_major avg `-0.0263` n `8`; equity avg `-0.0823` n `158`; fx avg `0.0173` n `6`; index avg `-0.0049` n `27`; metal avg `0.0148` n `20`; unknown avg `0.2901` n `1251`
- 4h: commodity avg `-0.4193` n `13`; crypto_alt avg `-0.1054` n `239`; crypto_major avg `0.0131` n `8`; equity avg `1.0358` n `158`; fx avg `0.0313` n `6`; index avg `0.1091` n `27`; metal avg `0.1349` n `20`; unknown avg `9.8932` n `1249`
- 24h: commodity avg `-0.127` n `13`; crypto_alt avg `-0.2616` n `239`; crypto_major avg `0.4095` n `8`; equity avg `-0.8396` n `158`; fx avg `0.061` n `6`; index avg `-0.1033` n `27`; metal avg `-0.6117` n `20`; unknown avg `-0.427` n `1021`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1448`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1374`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
