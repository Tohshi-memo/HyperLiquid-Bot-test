# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T09:22:30.524551+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0675` n `12`; crypto_alt avg `-0.0604` n `230`; crypto_major avg `0.0488` n `8`; equity avg `0.0488` n `100`; fx avg `0.0005` n `6`; index avg `0.0061` n `25`; metal avg `0.0196` n `20`; unknown avg `-0.0046` n `775`
- 1h: commodity avg `-0.0793` n `12`; crypto_alt avg `-0.1387` n `230`; crypto_major avg `0.1268` n `8`; equity avg `0.0307` n `100`; fx avg `-0.0033` n `6`; index avg `0.0034` n `25`; metal avg `0.0316` n `20`; unknown avg `-0.0459` n `775`
- 4h: commodity avg `-0.1044` n `12`; crypto_alt avg `0.1497` n `230`; crypto_major avg `-0.0303` n `8`; equity avg `0.0089` n `100`; fx avg `-0.0424` n `6`; index avg `0.0053` n `25`; metal avg `0.0618` n `20`; unknown avg `-0.0488` n `759`
- 24h: commodity avg `-0.697` n `12`; crypto_alt avg `1.7194` n `230`; crypto_major avg `1.8518` n `8`; equity avg `0.5765` n `100`; fx avg `-0.0079` n `6`; index avg `0.1286` n `25`; metal avg `0.1133` n `20`; unknown avg `0.0441` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1856`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1737`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1578`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1446`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1295`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1294`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1232`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1208`, n `666`, weak_sample_signal
