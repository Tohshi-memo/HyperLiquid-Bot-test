# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T06:02:06.530649+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0247` n `12`; crypto_alt avg `0.1987` n `228`; crypto_major avg `0.1832` n `8`; equity avg `0.0168` n `78`; fx avg `-0.0041` n `6`; index avg `-0.0125` n `23`; metal avg `-0.0089` n `18`; unknown avg `0.0494` n `655`
- 1h: commodity avg `0.0815` n `12`; crypto_alt avg `0.1129` n `228`; crypto_major avg `0.3218` n `8`; equity avg `0.1236` n `78`; fx avg `-0.0053` n `6`; index avg `0.0335` n `23`; metal avg `-0.0108` n `18`; unknown avg `7.309` n `655`
- 4h: commodity avg `0.0769` n `12`; crypto_alt avg `0.5287` n `228`; crypto_major avg `0.9992` n `8`; equity avg `0.4845` n `78`; fx avg `-0.0279` n `6`; index avg `0.0514` n `23`; metal avg `0.0011` n `18`; unknown avg `0.1709` n `655`
- 24h: commodity avg `0.5064` n `12`; crypto_alt avg `-3.0924` n `228`; crypto_major avg `-3.4513` n `8`; equity avg `1.3416` n `78`; fx avg `-0.1121` n `6`; index avg `0.3317` n `23`; metal avg `-4.1247` n `18`; unknown avg `-0.4174` n `546`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0546`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0529`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0507`, n `668`, weak_sample_signal
