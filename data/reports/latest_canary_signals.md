# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T20:37:25.717339+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.025` n `12`; crypto_alt avg `-0.028` n `230`; crypto_major avg `-0.036` n `8`; equity avg `0.0196` n `100`; fx avg `0.0012` n `6`; index avg `0.0121` n `25`; metal avg `-0.0024` n `20`; unknown avg `-0.0532` n `774`
- 1h: commodity avg `0.0243` n `12`; crypto_alt avg `-0.0409` n `230`; crypto_major avg `-0.1467` n `8`; equity avg `0.0266` n `100`; fx avg `-0.0027` n `6`; index avg `0.0298` n `25`; metal avg `-0.0024` n `20`; unknown avg `0.0515` n `774`
- 4h: commodity avg `-0.0907` n `12`; crypto_alt avg `0.1667` n `230`; crypto_major avg `0.2514` n `8`; equity avg `0.2251` n `100`; fx avg `0.0185` n `6`; index avg `0.085` n `25`; metal avg `0.0255` n `20`; unknown avg `-0.1787` n `774`
- 24h: commodity avg `-0.6202` n `12`; crypto_alt avg `0.2816` n `230`; crypto_major avg `0.9194` n `8`; equity avg `0.308` n `100`; fx avg `0.0089` n `6`; index avg `0.1563` n `25`; metal avg `0.0187` n `20`; unknown avg `-0.3584` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1772`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1723`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1339`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.121`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1198`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1157`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1129`, n `666`, weak_sample_signal
