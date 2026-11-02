# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T02:52:28.887179+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0297` n `13`; crypto_alt avg `-0.0527` n `238`; crypto_major avg `0.0485` n `8`; equity avg `-0.005` n `156`; fx avg `-0.0009` n `6`; index avg `-0.0108` n `27`; metal avg `-0.1056` n `20`; unknown avg `-0.1144` n `1263`
- 1h: commodity avg `-0.2004` n `13`; crypto_alt avg `-0.125` n `238`; crypto_major avg `-0.146` n `8`; equity avg `0.0937` n `156`; fx avg `0.0644` n `6`; index avg `-0.0` n `27`; metal avg `-0.1362` n `20`; unknown avg `1.1119` n `1255`
- 4h: commodity avg `-0.329` n `13`; crypto_alt avg `0.2778` n `238`; crypto_major avg `0.7446` n `8`; equity avg `0.6717` n `156`; fx avg `0.1775` n `6`; index avg `0.1903` n `27`; metal avg `-0.0599` n `20`; unknown avg `163.0983` n `1241`
- 24h: commodity avg `-0.315` n `13`; crypto_alt avg `-0.2297` n `238`; crypto_major avg `0.475` n `8`; equity avg `0.9287` n `156`; fx avg `0.1646` n `6`; index avg `0.2654` n `27`; metal avg `-0.0427` n `20`; unknown avg `3.0541` n `1120`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1852`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1769`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
