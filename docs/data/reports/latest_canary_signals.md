# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T15:22:32.309937+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.07` n `12`; crypto_alt avg `0.12` n `230`; crypto_major avg `0.1119` n `8`; equity avg `0.1568` n `98`; fx avg `-0.001` n `6`; index avg `0.0431` n `25`; metal avg `0.0927` n `20`; unknown avg `0.0387` n `771`
- 1h: commodity avg `-0.0495` n `12`; crypto_alt avg `0.0513` n `230`; crypto_major avg `0.0544` n `8`; equity avg `0.7515` n `98`; fx avg `-0.0177` n `6`; index avg `0.1435` n `25`; metal avg `0.1225` n `20`; unknown avg `0.0953` n `771`
- 4h: commodity avg `0.0401` n `12`; crypto_alt avg `0.1122` n `230`; crypto_major avg `0.1164` n `8`; equity avg `1.4418` n `98`; fx avg `-0.0074` n `6`; index avg `0.2101` n `25`; metal avg `0.0961` n `20`; unknown avg `0.1262` n `771`
- 24h: commodity avg `0.5157` n `12`; crypto_alt avg `1.5386` n `230`; crypto_major avg `1.7247` n `8`; equity avg `2.9699` n `98`; fx avg `0.016` n `6`; index avg `0.443` n `25`; metal avg `0.666` n `20`; unknown avg `0.3597` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0849`, n `666`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0557`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0544`, n `666`, weak_sample_signal
