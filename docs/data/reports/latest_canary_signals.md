# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T21:52:28.763374+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0098` n `12`; crypto_alt avg `0.0544` n `230`; crypto_major avg `-0.0165` n `8`; equity avg `-0.0254` n `100`; fx avg `0.0` n `6`; index avg `-0.0056` n `25`; metal avg `-0.0046` n `20`; unknown avg `-0.0006` n `774`
- 1h: commodity avg `0.0555` n `12`; crypto_alt avg `0.1682` n `230`; crypto_major avg `0.0128` n `8`; equity avg `-0.0228` n `100`; fx avg `-0.0022` n `6`; index avg `-0.0127` n `25`; metal avg `-0.0055` n `20`; unknown avg `-0.0474` n `774`
- 4h: commodity avg `0.1217` n `12`; crypto_alt avg `0.0333` n `230`; crypto_major avg `-0.2068` n `8`; equity avg `0.0628` n `100`; fx avg `0.0188` n `6`; index avg `0.0126` n `25`; metal avg `0.0038` n `20`; unknown avg `-0.1105` n `774`
- 24h: commodity avg `-0.6453` n `12`; crypto_alt avg `0.7229` n `230`; crypto_major avg `1.3308` n `8`; equity avg `0.3212` n `100`; fx avg `0.0018` n `6`; index avg `0.1293` n `25`; metal avg `0.011` n `20`; unknown avg `-0.3191` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1784`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1727`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.135`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1217`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1216`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1166`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1144`, n `666`, weak_sample_signal
