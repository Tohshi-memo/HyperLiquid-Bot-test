# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T21:52:23.626949+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0073` n `12`; crypto_alt avg `-0.0253` n `230`; crypto_major avg `0.0345` n `8`; equity avg `0.0245` n `100`; fx avg `0.0051` n `6`; index avg `0.012` n `25`; metal avg `0.0084` n `20`; unknown avg `0.1192` n `772`
- 1h: commodity avg `0.0209` n `12`; crypto_alt avg `-0.19` n `230`; crypto_major avg `-0.1424` n `8`; equity avg `-0.2308` n `100`; fx avg `-0.0137` n `6`; index avg `-0.0001` n `25`; metal avg `0.0374` n `20`; unknown avg `0.2349` n `772`
- 4h: commodity avg `-0.1585` n `12`; crypto_alt avg `-0.2435` n `230`; crypto_major avg `-0.0231` n `8`; equity avg `-0.1108` n `100`; fx avg `-0.0009` n `6`; index avg `0.0794` n `25`; metal avg `0.0583` n `20`; unknown avg `0.1035` n `772`
- 24h: commodity avg `0.8077` n `12`; crypto_alt avg `-1.7196` n `230`; crypto_major avg `-2.1679` n `8`; equity avg `-1.2411` n `99`; fx avg `-0.0694` n `6`; index avg `-0.222` n `25`; metal avg `-0.7318` n `20`; unknown avg `-0.2385` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1534`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
