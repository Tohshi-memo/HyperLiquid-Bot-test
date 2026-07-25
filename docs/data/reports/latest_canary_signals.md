# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T03:07:29.642525+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0337` n `12`; crypto_alt avg `0.0887` n `230`; crypto_major avg `0.1197` n `8`; equity avg `0.0885` n `100`; fx avg `0.0029` n `6`; index avg `0.0079` n `25`; metal avg `-0.0019` n `20`; unknown avg `0.8552` n `774`
- 1h: commodity avg `-0.1556` n `12`; crypto_alt avg `0.0513` n `230`; crypto_major avg `0.0084` n `8`; equity avg `0.202` n `100`; fx avg `-0.0213` n `6`; index avg `0.0378` n `25`; metal avg `-0.0075` n `20`; unknown avg `0.3185` n `774`
- 4h: commodity avg `-0.1883` n `12`; crypto_alt avg `0.0005` n `230`; crypto_major avg `0.0907` n `8`; equity avg `0.1884` n `100`; fx avg `-0.0442` n `6`; index avg `0.0569` n `25`; metal avg `-0.025` n `20`; unknown avg `-0.0098` n `774`
- 24h: commodity avg `-0.4881` n `12`; crypto_alt avg `-0.9498` n `230`; crypto_major avg `-0.8272` n `8`; equity avg `-2.2712` n `100`; fx avg `-0.0433` n `6`; index avg `-0.1179` n `25`; metal avg `0.2051` n `20`; unknown avg `14.0106` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1191`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1116`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1044`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1038`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1026`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
