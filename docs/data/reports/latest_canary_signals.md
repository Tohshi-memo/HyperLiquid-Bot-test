# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T20:07:24.885729+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0087` n `13`; crypto_alt avg `0.0357` n `238`; crypto_major avg `0.0465` n `8`; equity avg `0.0004` n `156`; fx avg `0.0067` n `6`; index avg `-0.0031` n `27`; metal avg `-0.0035` n `20`; unknown avg `319.7466` n `1235`
- 1h: commodity avg `0.0245` n `13`; crypto_alt avg `-0.1432` n `238`; crypto_major avg `-0.1711` n `8`; equity avg `-0.0687` n `156`; fx avg `-0.0067` n `6`; index avg `-0.0252` n `27`; metal avg `-0.0275` n `20`; unknown avg `0.479` n `1223`
- 4h: commodity avg `0.0576` n `13`; crypto_alt avg `-0.8544` n `238`; crypto_major avg `-0.5314` n `8`; equity avg `-0.2128` n `156`; fx avg `0.013` n `6`; index avg `-0.0326` n `27`; metal avg `-0.0205` n `20`; unknown avg `329.6355` n `1215`
- 24h: commodity avg `0.0721` n `13`; crypto_alt avg `-0.8329` n `238`; crypto_major avg `-0.4426` n `8`; equity avg `0.2088` n `156`; fx avg `0.0112` n `6`; index avg `0.0353` n `27`; metal avg `0.0293` n `20`; unknown avg `4.3733` n `990`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1483`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
