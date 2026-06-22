# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T18:52:32.702566+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0618` n `12`; crypto_alt avg `-0.4419` n `228`; crypto_major avg `-0.4471` n `8`; equity avg `-0.4035` n `85`; fx avg `-0.0071` n `6`; index avg `-0.0308` n `23`; metal avg `0.0228` n `20`; unknown avg `-0.1288` n `717`
- 1h: commodity avg `0.0235` n `12`; crypto_alt avg `-0.31` n `228`; crypto_major avg `-0.0052` n `8`; equity avg `-0.1632` n `85`; fx avg `-0.0068` n `6`; index avg `-0.0763` n `23`; metal avg `0.1049` n `20`; unknown avg `-0.3471` n `717`
- 4h: commodity avg `-0.1261` n `12`; crypto_alt avg `-1.1202` n `228`; crypto_major avg `-0.7285` n `8`; equity avg `-0.2484` n `85`; fx avg `0.0117` n `6`; index avg `-0.0799` n `23`; metal avg `-0.1478` n `20`; unknown avg `-0.3424` n `716`
- 24h: commodity avg `-1.0223` n `12`; crypto_alt avg `-0.7332` n `228`; crypto_major avg `-0.1991` n `8`; equity avg `-0.6362` n `85`; fx avg `0.0303` n `6`; index avg `0.0754` n `23`; metal avg `0.3138` n `18`; unknown avg `0.6803` n `631`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
