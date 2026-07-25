# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T17:07:30.230336+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0067` n `12`; crypto_alt avg `0.0398` n `230`; crypto_major avg `0.0927` n `8`; equity avg `0.014` n `100`; fx avg `0.01` n `6`; index avg `0.0185` n `25`; metal avg `0.0052` n `20`; unknown avg `0.0055` n `774`
- 1h: commodity avg `-0.0038` n `12`; crypto_alt avg `0.0773` n `230`; crypto_major avg `0.28` n `8`; equity avg `0.0487` n `100`; fx avg `0.0048` n `6`; index avg `0.0016` n `25`; metal avg `-0.004` n `20`; unknown avg `-0.0237` n `774`
- 4h: commodity avg `-0.3563` n `12`; crypto_alt avg `0.4254` n `230`; crypto_major avg `0.7634` n `8`; equity avg `0.0476` n `100`; fx avg `0.0021` n `6`; index avg `0.0114` n `25`; metal avg `0.0077` n `20`; unknown avg `-0.0322` n `774`
- 24h: commodity avg `-0.2356` n `12`; crypto_alt avg `0.355` n `230`; crypto_major avg `1.0346` n `8`; equity avg `-0.6395` n `100`; fx avg `-0.0103` n `6`; index avg `-0.0507` n `25`; metal avg `-0.1075` n `20`; unknown avg `-0.3549` n `757`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1643`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1642`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.128`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1167`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1118`, n `666`, weak_sample_signal
