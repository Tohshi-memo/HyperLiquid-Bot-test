# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T12:22:27.751038+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0789` n `13`; crypto_alt avg `-0.0542` n `238`; crypto_major avg `0.0699` n `8`; equity avg `-0.1714` n `156`; fx avg `-0.0003` n `6`; index avg `-0.0241` n `27`; metal avg `-0.071` n `20`; unknown avg `1.4686` n `1261`
- 1h: commodity avg `-0.0798` n `13`; crypto_alt avg `-0.1949` n `238`; crypto_major avg `-0.328` n `8`; equity avg `-0.3015` n `156`; fx avg `-0.0083` n `6`; index avg `-0.032` n `27`; metal avg `-0.1262` n `20`; unknown avg `0.0616` n `1249`
- 4h: commodity avg `0.0423` n `13`; crypto_alt avg `0.2328` n `238`; crypto_major avg `-0.4304` n `8`; equity avg `-0.9122` n `156`; fx avg `-0.0086` n `6`; index avg `-0.1109` n `27`; metal avg `-0.2381` n `20`; unknown avg `5.1562` n `1249`
- 24h: commodity avg `0.2489` n `13`; crypto_alt avg `-3.7379` n `238`; crypto_major avg `-2.5061` n `8`; equity avg `-4.0167` n `156`; fx avg `0.052` n `6`; index avg `-0.4444` n `27`; metal avg `-0.7799` n `20`; unknown avg `22.9905` n `1032`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
