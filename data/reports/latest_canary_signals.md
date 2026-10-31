# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T16:07:34.887264+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0011` n `13`; crypto_alt avg `0.1375` n `238`; crypto_major avg `0.0865` n `8`; equity avg `0.006` n `156`; fx avg `-0.0064` n `6`; index avg `-0.0083` n `27`; metal avg `-0.0004` n `20`; unknown avg `0.6949` n `1242`
- 1h: commodity avg `0.0153` n `13`; crypto_alt avg `0.7171` n `238`; crypto_major avg `0.3642` n `8`; equity avg `0.023` n `156`; fx avg `-0.0141` n `6`; index avg `-0.0133` n `27`; metal avg `0.0063` n `20`; unknown avg `0.3087` n `1236`
- 4h: commodity avg `-0.0894` n `13`; crypto_alt avg `1.1464` n `238`; crypto_major avg `0.1922` n `8`; equity avg `0.0358` n `156`; fx avg `-0.0228` n `6`; index avg `-0.0167` n `27`; metal avg `0.016` n `20`; unknown avg `0.1293` n `1236`
- 24h: commodity avg `-0.3962` n `13`; crypto_alt avg `1.3964` n `238`; crypto_major avg `-0.108` n `8`; equity avg `0.2714` n `156`; fx avg `-0.0282` n `6`; index avg `-0.0584` n `27`; metal avg `-0.0054` n `20`; unknown avg `1.1378` n `1081`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1549`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.142`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
