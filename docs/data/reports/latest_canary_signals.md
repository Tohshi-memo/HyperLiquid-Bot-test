# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T07:37:27.749931+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.023` n `12`; crypto_alt avg `0.0334` n `230`; crypto_major avg `-0.0486` n `8`; equity avg `0.004` n `100`; fx avg `-0.0029` n `6`; index avg `0.0016` n `25`; metal avg `0.0048` n `20`; unknown avg `-0.002` n `775`
- 1h: commodity avg `-0.048` n `12`; crypto_alt avg `0.2996` n `230`; crypto_major avg `0.1156` n `8`; equity avg `0.0426` n `100`; fx avg `-0.0072` n `6`; index avg `0.0066` n `25`; metal avg `0.0194` n `20`; unknown avg `-0.011` n `775`
- 4h: commodity avg `-0.0751` n `12`; crypto_alt avg `0.4551` n `230`; crypto_major avg `0.1066` n `8`; equity avg `-0.0089` n `100`; fx avg `0.0532` n `6`; index avg `0.0051` n `25`; metal avg `0.022` n `20`; unknown avg `-0.0031` n `759`
- 24h: commodity avg `-0.5933` n `12`; crypto_alt avg `1.699` n `230`; crypto_major avg `1.7621` n `8`; equity avg `0.5259` n `100`; fx avg `0.039` n `6`; index avg `0.1242` n `25`; metal avg `0.051` n `20`; unknown avg `0.0029` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1852`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.173`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.141`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1254`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1231`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1221`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1186`, n `666`, weak_sample_signal
