# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T06:07:28.202266+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0039` n `12`; crypto_alt avg `-0.0501` n `230`; crypto_major avg `0.0023` n `8`; equity avg `0.0133` n `100`; fx avg `0.0034` n `6`; index avg `0.0087` n `25`; metal avg `0.0001` n `20`; unknown avg `-0.0047` n `758`
- 1h: commodity avg `-0.0057` n `12`; crypto_alt avg `-0.2591` n `230`; crypto_major avg `-0.2617` n `8`; equity avg `-0.0156` n `100`; fx avg `-0.0021` n `6`; index avg `-0.0061` n `25`; metal avg `-0.0052` n `20`; unknown avg `-0.0363` n `758`
- 4h: commodity avg `-0.1546` n `12`; crypto_alt avg `-0.1124` n `230`; crypto_major avg `-0.1903` n `8`; equity avg `0.1995` n `100`; fx avg `-0.0294` n `6`; index avg `0.0519` n `25`; metal avg `-0.0159` n `20`; unknown avg `-0.1063` n `758`
- 24h: commodity avg `-0.3174` n `12`; crypto_alt avg `-1.4085` n `230`; crypto_major avg `-1.2412` n `8`; equity avg `-2.28` n `100`; fx avg `-0.0622` n `6`; index avg `-0.114` n `25`; metal avg `0.2163` n `20`; unknown avg `13.699` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1517`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1148`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1032`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1031`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
