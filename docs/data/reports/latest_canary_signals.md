# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T15:52:33.330709+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.088` n `13`; crypto_alt avg `-0.1374` n `238`; crypto_major avg `-0.0953` n `8`; equity avg `-0.0004` n `156`; fx avg `0.0113` n `6`; index avg `0.0019` n `27`; metal avg `0.0068` n `20`; unknown avg `0.3163` n `1263`
- 1h: commodity avg `-0.0925` n `13`; crypto_alt avg `-0.3849` n `238`; crypto_major avg `-0.1872` n `8`; equity avg `0.0116` n `156`; fx avg `0.0037` n `6`; index avg `0.0096` n `27`; metal avg `0.0074` n `20`; unknown avg `-0.4391` n `1257`
- 4h: commodity avg `-0.0565` n `13`; crypto_alt avg `-0.0835` n `238`; crypto_major avg `-0.1159` n `8`; equity avg `-0.0428` n `156`; fx avg `0.0275` n `6`; index avg `0.0466` n `27`; metal avg `-0.0077` n `20`; unknown avg `-0.0224` n `1253`
- 24h: commodity avg `-0.0314` n `13`; crypto_alt avg `-0.5569` n `238`; crypto_major avg `0.1943` n `8`; equity avg `0.4491` n `156`; fx avg `0.0047` n `6`; index avg `0.0847` n `27`; metal avg `0.0555` n `20`; unknown avg `3.4408` n `1018`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
