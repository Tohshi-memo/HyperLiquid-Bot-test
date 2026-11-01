# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T13:52:24.876519+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0266` n `13`; crypto_alt avg `0.0019` n `238`; crypto_major avg `-0.0039` n `8`; equity avg `0.0048` n `156`; fx avg `-0.0069` n `6`; index avg `0.0181` n `27`; metal avg `-0.0015` n `20`; unknown avg `0.1066` n `1263`
- 1h: commodity avg `0.0078` n `13`; crypto_alt avg `0.2429` n `238`; crypto_major avg `0.0369` n `8`; equity avg `0.0343` n `156`; fx avg `-0.0048` n `6`; index avg `0.0257` n `27`; metal avg `0.0049` n `20`; unknown avg `-0.1741` n `1257`
- 4h: commodity avg `-0.0076` n `13`; crypto_alt avg `0.1737` n `238`; crypto_major avg `-0.1066` n `8`; equity avg `0.0212` n `156`; fx avg `-0.012` n `6`; index avg `0.0197` n `27`; metal avg `0.0252` n `20`; unknown avg `0.0038` n `1237`
- 24h: commodity avg `0.0137` n `13`; crypto_alt avg `0.5944` n `238`; crypto_major avg `0.2949` n `8`; equity avg `0.598` n `156`; fx avg `-0.0324` n `6`; index avg `0.0753` n `27`; metal avg `0.0723` n `20`; unknown avg `3.0797` n `1018`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
