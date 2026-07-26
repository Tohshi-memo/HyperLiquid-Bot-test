# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T18:47:00.875294+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0129` n `12`; crypto_alt avg `0.0105` n `230`; crypto_major avg `0.0224` n `8`; equity avg `0.0146` n `100`; fx avg `0.0071` n `6`; index avg `-0.0014` n `25`; metal avg `0.0073` n `20`; unknown avg `-0.1183` n `775`
- 1h: commodity avg `0.1014` n `12`; crypto_alt avg `-0.117` n `230`; crypto_major avg `-0.0385` n `8`; equity avg `0.0417` n `100`; fx avg `0.0186` n `6`; index avg `-0.0229` n `25`; metal avg `0.0286` n `20`; unknown avg `-0.1778` n `775`
- 4h: commodity avg `0.1777` n `12`; crypto_alt avg `0.1607` n `230`; crypto_major avg `0.2663` n `8`; equity avg `0.1049` n `100`; fx avg `0.0007` n `6`; index avg `0.0043` n `25`; metal avg `0.0286` n `20`; unknown avg `-0.2262` n `775`
- 24h: commodity avg `-0.3489` n `12`; crypto_alt avg `0.742` n `230`; crypto_major avg `0.6126` n `8`; equity avg `0.7253` n `100`; fx avg `0.0509` n `6`; index avg `0.133` n `25`; metal avg `0.1972` n `20`; unknown avg `-0.0742` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1926`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1829`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1641`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
