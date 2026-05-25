# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T12:22:18.480692+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0893` n `12`; crypto_alt avg `0.1246` n `228`; crypto_major avg `0.1014` n `8`; equity avg `-0.0337` n `67`; fx avg `0.0056` n `6`; index avg `-0.0255` n `23`; metal avg `-0.1303` n `18`; unknown avg `-0.0623` n `405`
- 1h: commodity avg `0.1394` n `12`; crypto_alt avg `-0.2573` n `228`; crypto_major avg `0.1529` n `8`; equity avg `-0.0292` n `67`; fx avg `0.0097` n `6`; index avg `0.0189` n `23`; metal avg `-0.3811` n `18`; unknown avg `-0.2887` n `397`
- 4h: commodity avg `-0.1862` n `12`; crypto_alt avg `0.1646` n `228`; crypto_major avg `0.1003` n `8`; equity avg `0.2496` n `67`; fx avg `0.0205` n `6`; index avg `0.1082` n `23`; metal avg `0.0031` n `18`; unknown avg `-0.1577` n `397`
- 24h: commodity avg `-0.0524` n `12`; crypto_alt avg `0.8434` n `228`; crypto_major avg `0.157` n `8`; equity avg `0.5543` n `67`; fx avg `0.0416` n `6`; index avg `0.0524` n `23`; metal avg `0.4687` n `18`; unknown avg `0.4758` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1614`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
