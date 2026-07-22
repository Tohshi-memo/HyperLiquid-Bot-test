# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T01:52:30.492421+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0002` n `12`; crypto_alt avg `0.1441` n `230`; crypto_major avg `0.0944` n `8`; equity avg `0.1681` n `98`; fx avg `0.0054` n `6`; index avg `0.0276` n `25`; metal avg `0.0503` n `20`; unknown avg `-0.0258` n `771`
- 1h: commodity avg `0.1995` n `12`; crypto_alt avg `-0.0781` n `230`; crypto_major avg `-0.1102` n `8`; equity avg `-0.033` n `98`; fx avg `-0.0011` n `6`; index avg `0.0615` n `25`; metal avg `0.3546` n `20`; unknown avg `-0.1854` n `771`
- 4h: commodity avg `0.202` n `12`; crypto_alt avg `0.0424` n `230`; crypto_major avg `0.2404` n `8`; equity avg `0.0026` n `98`; fx avg `0.005` n `6`; index avg `0.0501` n `25`; metal avg `0.4485` n `20`; unknown avg `-0.2821` n `771`
- 24h: commodity avg `0.7021` n `12`; crypto_alt avg `0.9037` n `230`; crypto_major avg `0.8557` n `8`; equity avg `4.208` n `98`; fx avg `0.0102` n `6`; index avg `0.5982` n `25`; metal avg `1.0849` n `20`; unknown avg `0.3979` n `755`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.095`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.057`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0496`, n `668`, weak_sample_signal
