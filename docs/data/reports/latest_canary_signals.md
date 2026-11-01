# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T09:52:31.299972+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0122` n `13`; crypto_alt avg `0.2181` n `238`; crypto_major avg `0.1288` n `8`; equity avg `0.0097` n `156`; fx avg `-0.0005` n `6`; index avg `0.0083` n `27`; metal avg `0.0` n `20`; unknown avg `-0.0177` n `1263`
- 1h: commodity avg `-0.0133` n `13`; crypto_alt avg `-0.1197` n `238`; crypto_major avg `-0.1882` n `8`; equity avg `0.0478` n `156`; fx avg `-0.0124` n `6`; index avg `0.0161` n `27`; metal avg `-0.0016` n `20`; unknown avg `-0.0455` n `1257`
- 4h: commodity avg `-0.0119` n `13`; crypto_alt avg `0.0137` n `238`; crypto_major avg `0.1294` n `8`; equity avg `0.1764` n `156`; fx avg `-0.0092` n `6`; index avg `0.0298` n `27`; metal avg `0.0186` n `20`; unknown avg `117.2461` n `1224`
- 24h: commodity avg `0.0` n `13`; crypto_alt avg `0.8111` n `238`; crypto_major avg `0.7485` n `8`; equity avg `0.4787` n `156`; fx avg `-0.011` n `6`; index avg `0.0302` n `27`; metal avg `0.0498` n `20`; unknown avg `2.625` n `996`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
