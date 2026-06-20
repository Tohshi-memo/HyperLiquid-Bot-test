# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T01:34:22.739310+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0119` n `12`; crypto_alt avg `-0.0693` n `228`; crypto_major avg `0.1019` n `8`; equity avg `0.0283` n `78`; fx avg `0.0004` n `6`; index avg `0.0005` n `23`; metal avg `-0.0033` n `18`; unknown avg `-0.1169` n `679`
- 1h: commodity avg `-0.0232` n `12`; crypto_alt avg `-0.5817` n `228`; crypto_major avg `-0.2154` n `8`; equity avg `-0.0787` n `78`; fx avg `-0.0055` n `6`; index avg `-0.0154` n `23`; metal avg `-0.043` n `18`; unknown avg `-0.3735` n `679`
- 4h: commodity avg `-0.0896` n `12`; crypto_alt avg `0.3093` n `228`; crypto_major avg `0.3623` n `8`; equity avg `0.2189` n `78`; fx avg `0.0688` n `6`; index avg `0.0575` n `23`; metal avg `-0.0175` n `18`; unknown avg `-0.5049` n `671`
- 24h: commodity avg `0.2571` n `12`; crypto_alt avg `-3.4854` n `228`; crypto_major avg `-4.3231` n `8`; equity avg `0.9243` n `78`; fx avg `-0.0845` n `6`; index avg `0.2683` n `23`; metal avg `-4.1323` n `18`; unknown avg `-0.6197` n `556`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0559`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
