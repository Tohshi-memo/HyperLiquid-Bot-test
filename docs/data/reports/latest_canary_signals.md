# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T05:08:45.602343+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0012` n `12`; crypto_alt avg `-0.0593` n `228`; crypto_major avg `-0.0703` n `8`; equity avg `-0.0334` n `65`; fx avg `0.0` n `5`; index avg `-0.0142` n `23`; metal avg `-0.0194` n `18`; unknown avg `-0.1501` n `376`
- 1h: commodity avg `0.0143` n `12`; crypto_alt avg `0.0315` n `228`; crypto_major avg `-0.0245` n `8`; equity avg `0.0427` n `65`; fx avg `0.0006` n `5`; index avg `0.0028` n `23`; metal avg `0.0406` n `18`; unknown avg `-0.0197` n `376`
- 4h: commodity avg `-0.1305` n `12`; crypto_alt avg `0.3372` n `228`; crypto_major avg `0.2609` n `8`; equity avg `0.3916` n `65`; fx avg `0.0032` n `5`; index avg `0.0664` n `23`; metal avg `0.2083` n `18`; unknown avg `-0.1812` n `376`
- 24h: commodity avg `0.2294` n `12`; crypto_alt avg `-1.4851` n `228`; crypto_major avg `-0.5494` n `8`; equity avg `1.0186` n `65`; fx avg `-0.0055` n `5`; index avg `0.3154` n `23`; metal avg `0.3747` n `18`; unknown avg `-0.1539` n `356`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
