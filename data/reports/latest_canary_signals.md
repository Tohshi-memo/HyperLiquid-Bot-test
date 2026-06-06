# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T16:54:28.672981+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0546` n `12`; crypto_alt avg `0.4833` n `228`; crypto_major avg `0.486` n `8`; equity avg `0.1759` n `74`; fx avg `0.0401` n `6`; index avg `-0.035` n `23`; metal avg `0.0278` n `18`; unknown avg `-0.0137` n `515`
- 1h: commodity avg `0.0958` n `12`; crypto_alt avg `0.1323` n `228`; crypto_major avg `-0.11` n `8`; equity avg `0.1625` n `74`; fx avg `0.06` n `6`; index avg `0.0107` n `23`; metal avg `0.077` n `18`; unknown avg `-2.3138` n `515`
- 4h: commodity avg `0.2035` n `12`; crypto_alt avg `-0.2941` n `228`; crypto_major avg `-0.7465` n `8`; equity avg `0.0411` n `74`; fx avg `0.0827` n `6`; index avg `0.1407` n `23`; metal avg `-0.176` n `18`; unknown avg `-0.4785` n `415`
- 24h: commodity avg `0.5781` n `12`; crypto_alt avg `-2.0926` n `228`; crypto_major avg `-1.8344` n `8`; equity avg `-1.9858` n `74`; fx avg `0.0085` n `6`; index avg `-1.2306` n `23`; metal avg `-1.1719` n `18`; unknown avg `-0.3166` n `400`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
