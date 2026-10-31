# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T04:22:23.426727+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0014` n `13`; crypto_alt avg `-0.1153` n `238`; crypto_major avg `-0.0506` n `8`; equity avg `-0.0109` n `156`; fx avg `0.0005` n `6`; index avg `-0.0077` n `27`; metal avg `-0.0005` n `20`; unknown avg `-0.2262` n `1262`
- 1h: commodity avg `0.0058` n `13`; crypto_alt avg `-0.3765` n `238`; crypto_major avg `-0.3193` n `8`; equity avg `0.0064` n `156`; fx avg `0.0081` n `6`; index avg `-0.0194` n `27`; metal avg `-0.0011` n `20`; unknown avg `0.3641` n `1242`
- 4h: commodity avg `0.1092` n `13`; crypto_alt avg `-0.8303` n `238`; crypto_major avg `-0.468` n `8`; equity avg `-0.0112` n `156`; fx avg `0.0088` n `6`; index avg `-0.055` n `27`; metal avg `-0.0165` n `20`; unknown avg `-0.3883` n `1232`
- 24h: commodity avg `0.0187` n `13`; crypto_alt avg `1.9875` n `238`; crypto_major avg `-1.0684` n `8`; equity avg `-2.7102` n `156`; fx avg `-0.0823` n `6`; index avg `-0.2311` n `27`; metal avg `-0.6241` n `20`; unknown avg `2.9723` n `1006`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
