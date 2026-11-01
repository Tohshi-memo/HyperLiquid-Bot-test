# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T20:52:26.845816+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.008` n `13`; crypto_alt avg `0.0714` n `238`; crypto_major avg `0.0131` n `8`; equity avg `0.0464` n `156`; fx avg `0.0076` n `6`; index avg `0.0031` n `27`; metal avg `0.0029` n `20`; unknown avg `3.2324` n `1263`
- 1h: commodity avg `-0.0261` n `13`; crypto_alt avg `0.2174` n `238`; crypto_major avg `0.1893` n `8`; equity avg `0.0742` n `156`; fx avg `0.0001` n `6`; index avg `0.0076` n `27`; metal avg `0.0125` n `20`; unknown avg `295.7538` n `1235`
- 4h: commodity avg `0.0323` n `13`; crypto_alt avg `-0.6681` n `238`; crypto_major avg `-0.4132` n `8`; equity avg `-0.1815` n `156`; fx avg `-0.0145` n `6`; index avg `-0.0437` n `27`; metal avg `-0.0136` n `20`; unknown avg `329.8221` n `1215`
- 24h: commodity avg `0.0361` n `13`; crypto_alt avg `-0.5595` n `238`; crypto_major avg `-0.1485` n `8`; equity avg `0.2715` n `156`; fx avg `-0.0052` n `6`; index avg `0.0533` n `27`; metal avg `0.0454` n `20`; unknown avg `4.4862` n `990`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1416`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
