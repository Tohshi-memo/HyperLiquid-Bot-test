# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T19:22:31.084351+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0475` n `12`; crypto_alt avg `-0.0159` n `230`; crypto_major avg `-0.013` n `8`; equity avg `-0.0184` n `100`; fx avg `0.0191` n `6`; index avg `-0.0036` n `25`; metal avg `0.002` n `20`; unknown avg `-0.0815` n `775`
- 1h: commodity avg `0.1841` n `12`; crypto_alt avg `-0.0446` n `230`; crypto_major avg `-0.0938` n `8`; equity avg `-0.0044` n `100`; fx avg `0.017` n `6`; index avg `-0.0344` n `25`; metal avg `0.0282` n `20`; unknown avg `-0.1708` n `775`
- 4h: commodity avg `0.2359` n `12`; crypto_alt avg `-0.0058` n `230`; crypto_major avg `-0.0743` n `8`; equity avg `-0.0049` n `100`; fx avg `0.0183` n `6`; index avg `-0.0236` n `25`; metal avg `0.0523` n `20`; unknown avg `-0.2626` n `775`
- 24h: commodity avg `-0.1784` n `12`; crypto_alt avg `0.7701` n `230`; crypto_major avg `0.6587` n `8`; equity avg `0.6774` n `100`; fx avg `0.0443` n `6`; index avg `0.1197` n `25`; metal avg `0.2092` n `20`; unknown avg `-0.1173` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1919`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.182`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
