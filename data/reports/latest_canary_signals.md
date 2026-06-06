# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T17:07:22.500030+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0219` n `12`; crypto_alt avg `-0.2774` n `228`; crypto_major avg `-0.2418` n `8`; equity avg `-0.0721` n `74`; fx avg `-0.0187` n `6`; index avg `0.0632` n `23`; metal avg `-0.0009` n `18`; unknown avg `-0.0418` n `515`
- 1h: commodity avg `0.1247` n `12`; crypto_alt avg `-0.3802` n `228`; crypto_major avg `-0.3649` n `8`; equity avg `0.1025` n `74`; fx avg `0.0412` n `6`; index avg `0.0446` n `23`; metal avg `0.0319` n `18`; unknown avg `-0.5811` n `515`
- 4h: commodity avg `0.1612` n `12`; crypto_alt avg `-0.6594` n `228`; crypto_major avg `-0.8333` n `8`; equity avg `-0.0283` n `74`; fx avg `0.0643` n `6`; index avg `0.102` n `23`; metal avg `-0.1729` n `18`; unknown avg `-0.6634` n `415`
- 24h: commodity avg `0.4737` n `12`; crypto_alt avg `-2.6346` n `228`; crypto_major avg `-2.3225` n `8`; equity avg `-1.9612` n `74`; fx avg `-0.0062` n `6`; index avg `-1.1937` n `23`; metal avg `-1.3604` n `18`; unknown avg `0.3866` n `400`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
