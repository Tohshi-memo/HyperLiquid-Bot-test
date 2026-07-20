# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T00:22:29.851574+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0083` n `12`; crypto_alt avg `0.2081` n `230`; crypto_major avg `0.023` n `8`; equity avg `0.1998` n `98`; fx avg `-0.0278` n `6`; index avg `0.0718` n `25`; metal avg `0.1224` n `20`; unknown avg `-0.0264` n `769`
- 1h: commodity avg `-0.0472` n `12`; crypto_alt avg `0.491` n `230`; crypto_major avg `0.3246` n `8`; equity avg `0.7187` n `98`; fx avg `0.0018` n `6`; index avg `0.1748` n `25`; metal avg `0.1726` n `20`; unknown avg `0.0336` n `767`
- 4h: commodity avg `-0.0686` n `12`; crypto_alt avg `0.5211` n `230`; crypto_major avg `0.4583` n `8`; equity avg `0.836` n `98`; fx avg `-0.033` n `6`; index avg `0.2113` n `25`; metal avg `0.0222` n `20`; unknown avg `0.131` n `767`
- 24h: commodity avg `-0.0743` n `12`; crypto_alt avg `0.2846` n `230`; crypto_major avg `0.5746` n `8`; equity avg `1.2427` n `97`; fx avg `0.0817` n `6`; index avg `0.1944` n `25`; metal avg `0.0334` n `20`; unknown avg `0.1225` n `749`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1352`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1213`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1139`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0932`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0897`, n `666`, weak_sample_signal
