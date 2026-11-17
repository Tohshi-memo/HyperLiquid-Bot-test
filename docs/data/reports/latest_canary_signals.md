# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T07:52:34.642169+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0161` n `13`; crypto_alt avg `-0.0169` n `239`; crypto_major avg `0.0081` n `8`; equity avg `0.0184` n `162`; fx avg `0.0021` n `6`; index avg `0.0123` n `27`; metal avg `-0.0161` n `20`; unknown avg `0.009` n `1266`
- 1h: commodity avg `0.1172` n `13`; crypto_alt avg `0.2382` n `239`; crypto_major avg `0.1242` n `8`; equity avg `0.1619` n `162`; fx avg `-0.0088` n `6`; index avg `0.0036` n `27`; metal avg `0.0041` n `20`; unknown avg `204.0306` n `1224`
- 4h: commodity avg `0.169` n `13`; crypto_alt avg `-0.0923` n `239`; crypto_major avg `-0.3329` n `8`; equity avg `-0.797` n `162`; fx avg `-0.0173` n `6`; index avg `-0.0526` n `27`; metal avg `-0.0076` n `20`; unknown avg `-0.3545` n `1188`
- 24h: commodity avg `-1.0004` n `13`; crypto_alt avg `0.7795` n `239`; crypto_major avg `0.8751` n `8`; equity avg `-2.6023` n `162`; fx avg `-0.0269` n `6`; index avg `-0.2554` n `27`; metal avg `0.0081` n `20`; unknown avg `233.3242` n `1101`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
