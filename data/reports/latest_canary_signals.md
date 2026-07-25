# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T07:07:30.982533+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0304` n `12`; crypto_alt avg `0.1527` n `230`; crypto_major avg `0.0607` n `8`; equity avg `-0.0222` n `100`; fx avg `0.008` n `6`; index avg `-0.0063` n `25`; metal avg `0.0005` n `20`; unknown avg `0.0137` n `774`
- 1h: commodity avg `0.048` n `12`; crypto_alt avg `-0.0868` n `230`; crypto_major avg `0.0075` n `8`; equity avg `-0.0143` n `100`; fx avg `0.0185` n `6`; index avg `-0.0005` n `25`; metal avg `0.004` n `20`; unknown avg `-0.0015` n `774`
- 4h: commodity avg `0.0491` n `12`; crypto_alt avg `-0.2514` n `230`; crypto_major avg `-0.1912` n `8`; equity avg `-0.0167` n `100`; fx avg `0.0104` n `6`; index avg `0.0136` n `25`; metal avg `-0.0044` n `20`; unknown avg `-0.098` n `758`
- 24h: commodity avg `-0.1519` n `12`; crypto_alt avg `-1.7758` n `230`; crypto_major avg `-1.6089` n `8`; equity avg `-2.5011` n `100`; fx avg `-0.0798` n `6`; index avg `-0.1741` n `25`; metal avg `0.0438` n `20`; unknown avg `13.5941` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1534`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1144`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1053`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1025`, n `666`, weak_sample_signal
