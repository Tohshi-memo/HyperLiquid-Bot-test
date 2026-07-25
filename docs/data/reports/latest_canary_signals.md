# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T11:07:30.355170+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0238` n `12`; crypto_alt avg `0.0894` n `230`; crypto_major avg `0.0615` n `8`; equity avg `0.0055` n `100`; fx avg `-0.0005` n `6`; index avg `0.0012` n `25`; metal avg `0.008` n `20`; unknown avg `-0.0177` n `774`
- 1h: commodity avg `-0.0264` n `12`; crypto_alt avg `0.1343` n `230`; crypto_major avg `0.048` n `8`; equity avg `0.0185` n `100`; fx avg `-0.0001` n `6`; index avg `0.0061` n `25`; metal avg `0.0062` n `20`; unknown avg `-0.016` n `774`
- 4h: commodity avg `-0.0469` n `12`; crypto_alt avg `0.0106` n `230`; crypto_major avg `0.1596` n `8`; equity avg `-0.0491` n `100`; fx avg `0.0007` n `6`; index avg `0.0114` n `25`; metal avg `0.0103` n `20`; unknown avg `-0.1845` n `774`
- 24h: commodity avg `-0.0696` n `12`; crypto_alt avg `-1.2672` n `230`; crypto_major avg `-1.0282` n `8`; equity avg `-2.9115` n `100`; fx avg `-0.0058` n `6`; index avg `-0.2606` n `25`; metal avg `-0.1492` n `20`; unknown avg `13.1902` n `757`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.157`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1162`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1107`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1005`, n `666`, weak_sample_signal
