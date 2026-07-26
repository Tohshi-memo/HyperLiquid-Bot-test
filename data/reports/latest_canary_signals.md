# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T14:22:29.108542+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.004` n `12`; crypto_alt avg `-0.0602` n `230`; crypto_major avg `-0.0967` n `8`; equity avg `-0.029` n `100`; fx avg `0.0` n `6`; index avg `-0.0057` n `25`; metal avg `-0.0119` n `20`; unknown avg `0.0374` n `775`
- 1h: commodity avg `0.0088` n `12`; crypto_alt avg `0.0025` n `230`; crypto_major avg `0.1353` n `8`; equity avg `0.0533` n `100`; fx avg `-0.0029` n `6`; index avg `0.0123` n `25`; metal avg `0.0144` n `20`; unknown avg `0.2066` n `775`
- 4h: commodity avg `0.0534` n `12`; crypto_alt avg `-0.1286` n `230`; crypto_major avg `0.0374` n `8`; equity avg `0.1681` n `100`; fx avg `0.0035` n `6`; index avg `0.0154` n `25`; metal avg `0.0673` n `20`; unknown avg `-0.0099` n `775`
- 24h: commodity avg `-0.4218` n `12`; crypto_alt avg `1.2548` n `230`; crypto_major avg `1.5896` n `8`; equity avg `0.8524` n `100`; fx avg `0.0275` n `6`; index avg `0.1794` n `25`; metal avg `0.1897` n `20`; unknown avg `0.1199` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1908`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1807`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.162`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
