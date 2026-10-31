# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T00:52:33.161373+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0382` n `13`; crypto_alt avg `0.0124` n `238`; crypto_major avg `0.0563` n `8`; equity avg `0.006` n `156`; fx avg `-0.0015` n `6`; index avg `-0.0077` n `27`; metal avg `-0.007` n `20`; unknown avg `-0.0086` n `1262`
- 1h: commodity avg `-0.0924` n `13`; crypto_alt avg `0.1686` n `238`; crypto_major avg `0.1819` n `8`; equity avg `0.0836` n `156`; fx avg `-0.0004` n `6`; index avg `0.0069` n `27`; metal avg `0.0105` n `20`; unknown avg `-0.2369` n `1248`
- 4h: commodity avg `-0.0621` n `13`; crypto_alt avg `1.5504` n `238`; crypto_major avg `0.711` n `8`; equity avg `0.2528` n `156`; fx avg `-0.0314` n `6`; index avg `0.0417` n `27`; metal avg `0.0807` n `20`; unknown avg `0.1427` n `1233`
- 24h: commodity avg `0.0262` n `13`; crypto_alt avg `4.4069` n `238`; crypto_major avg `1.1451` n `8`; equity avg `-2.0462` n `156`; fx avg `-0.1529` n `6`; index avg `-0.157` n `27`; metal avg `-0.9087` n `20`; unknown avg `4.1085` n `1018`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1483`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
