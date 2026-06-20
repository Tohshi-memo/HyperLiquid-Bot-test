# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T06:22:30.223985+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0367` n `12`; crypto_alt avg `0.168` n `228`; crypto_major avg `0.1451` n `8`; equity avg `0.0211` n `78`; fx avg `0.0066` n `6`; index avg `0.0065` n `23`; metal avg `-0.0007` n `18`; unknown avg `1.0314` n `679`
- 1h: commodity avg `0.0584` n `12`; crypto_alt avg `0.1653` n `228`; crypto_major avg `0.3625` n `8`; equity avg `0.0889` n `78`; fx avg `-0.0033` n `6`; index avg `-0.0074` n `23`; metal avg `-0.0229` n `18`; unknown avg `-0.0816` n `647`
- 4h: commodity avg `0.0735` n `12`; crypto_alt avg `0.9402` n `228`; crypto_major avg `1.4584` n `8`; equity avg `0.5012` n `78`; fx avg `-0.0228` n `6`; index avg `0.0412` n `23`; metal avg `0.0037` n `18`; unknown avg `0.3616` n `647`
- 24h: commodity avg `0.5194` n `12`; crypto_alt avg `-2.919` n `228`; crypto_major avg `-3.2185` n `8`; equity avg `1.3731` n `78`; fx avg `-0.1054` n `6`; index avg `0.3204` n `23`; metal avg `-4.1271` n `18`; unknown avg `0.0106` n `538`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0548`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0509`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0508`, n `668`, weak_sample_signal
