# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T22:52:31.726234+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0193` n `12`; crypto_alt avg `-0.0383` n `230`; crypto_major avg `-0.0672` n `8`; equity avg `0.0545` n `100`; fx avg `0.0072` n `6`; index avg `0.0493` n `25`; metal avg `0.0039` n `20`; unknown avg `-0.0812` n `772`
- 1h: commodity avg `-0.0384` n `12`; crypto_alt avg `-0.1276` n `230`; crypto_major avg `-0.0401` n `8`; equity avg `-0.0743` n `100`; fx avg `0.0064` n `6`; index avg `-0.0273` n `25`; metal avg `-0.0201` n `20`; unknown avg `-0.1532` n `772`
- 4h: commodity avg `-0.0285` n `12`; crypto_alt avg `-0.1439` n `230`; crypto_major avg `-0.0006` n `8`; equity avg `0.1023` n `100`; fx avg `0.0052` n `6`; index avg `0.0857` n `25`; metal avg `0.0389` n `20`; unknown avg `0.2011` n `772`
- 24h: commodity avg `0.6756` n `12`; crypto_alt avg `-1.6546` n `230`; crypto_major avg `-2.1462` n `8`; equity avg `-1.1257` n `99`; fx avg `-0.0521` n `6`; index avg `-0.2014` n `25`; metal avg `-0.6337` n `20`; unknown avg `-0.296` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
