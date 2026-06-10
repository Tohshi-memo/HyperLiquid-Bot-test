# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T22:52:26.205462+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1405` n `12`; crypto_alt avg `0.1486` n `228`; crypto_major avg `0.0816` n `8`; equity avg `-0.117` n `74`; fx avg `0.0066` n `6`; index avg `-0.0159` n `23`; metal avg `-0.0123` n `18`; unknown avg `0.0439` n `550`
- 1h: commodity avg `0.1252` n `12`; crypto_alt avg `0.5416` n `228`; crypto_major avg `0.3955` n `8`; equity avg `-0.3786` n `74`; fx avg `-0.0369` n `6`; index avg `-0.0907` n `23`; metal avg `-0.1773` n `18`; unknown avg `0.3733` n `550`
- 4h: commodity avg `0.7417` n `12`; crypto_alt avg `-1.3839` n `228`; crypto_major avg `-0.8371` n `8`; equity avg `-1.4467` n `74`; fx avg `-0.0842` n `6`; index avg `-0.4841` n `23`; metal avg `-1.0932` n `18`; unknown avg `-0.0021` n `550`
- 24h: commodity avg `1.5023` n `12`; crypto_alt avg `-2.4271` n `228`; crypto_major avg `-2.5443` n `8`; equity avg `-2.1343` n `74`; fx avg `-0.0829` n `6`; index avg `-1.621` n `23`; metal avg `-2.3618` n `18`; unknown avg `-0.4579` n `537`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
