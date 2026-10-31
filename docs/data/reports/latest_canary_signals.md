# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T14:52:28.925439+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0263` n `13`; crypto_alt avg `0.1486` n `238`; crypto_major avg `0.0961` n `8`; equity avg `0.0508` n `156`; fx avg `0.0085` n `6`; index avg `0.0039` n `27`; metal avg `0.0028` n `20`; unknown avg `-0.099` n `1262`
- 1h: commodity avg `-0.063` n `13`; crypto_alt avg `0.0986` n `238`; crypto_major avg `-0.0844` n `8`; equity avg `0.1079` n `156`; fx avg `0.0038` n `6`; index avg `0.0112` n `27`; metal avg `0.0063` n `20`; unknown avg `129.8357` n `1256`
- 4h: commodity avg `-0.126` n `13`; crypto_alt avg `0.4827` n `238`; crypto_major avg `0.0915` n `8`; equity avg `0.0535` n `156`; fx avg `-0.0034` n `6`; index avg `-0.003` n `27`; metal avg `0.004` n `20`; unknown avg `-0.1436` n `1224`
- 24h: commodity avg `-0.3348` n `13`; crypto_alt avg `0.7733` n `238`; crypto_major avg `-0.263` n `8`; equity avg `-0.6051` n `156`; fx avg `0.0253` n `6`; index avg `-0.1456` n `27`; metal avg `-0.1613` n `20`; unknown avg `271.6313` n `1099`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1562`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1483`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1431`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
