# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T16:33:33.072437+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0006` n `12`; crypto_alt avg `0.1894` n `230`; crypto_major avg `0.2848` n `8`; equity avg `0.078` n `100`; fx avg `0.0029` n `6`; index avg `0.0065` n `25`; metal avg `0.0239` n `20`; unknown avg `-0.1019` n `775`
- 1h: commodity avg `0.0031` n `12`; crypto_alt avg `0.3291` n `230`; crypto_major avg `0.3094` n `8`; equity avg `0.0467` n `100`; fx avg `-0.0085` n `6`; index avg `0.0252` n `25`; metal avg `0.0314` n `20`; unknown avg `-0.0619` n `775`
- 4h: commodity avg `0.0043` n `12`; crypto_alt avg `0.4127` n `230`; crypto_major avg `0.7287` n `8`; equity avg `0.2145` n `100`; fx avg `-0.0187` n `6`; index avg `0.0304` n `25`; metal avg `0.0518` n `20`; unknown avg `0.2075` n `775`
- 24h: commodity avg `-0.4793` n `12`; crypto_alt avg `1.45` n `230`; crypto_major avg `1.6208` n `8`; equity avg `0.9306` n `100`; fx avg `0.0269` n `6`; index avg `0.2149` n `25`; metal avg `0.2194` n `20`; unknown avg `0.1378` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1921`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1822`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1632`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
