# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T07:22:27.656013+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0605` n `12`; crypto_alt avg `0.0459` n `228`; crypto_major avg `0.0664` n `8`; equity avg `0.0395` n `86`; fx avg `-0.0009` n `6`; index avg `0.0117` n `23`; metal avg `0.0534` n `20`; unknown avg `30.7843` n `765`
- 1h: commodity avg `0.0947` n `12`; crypto_alt avg `-0.0255` n `228`; crypto_major avg `0.0738` n `8`; equity avg `0.0949` n `86`; fx avg `-0.0265` n `6`; index avg `-0.0188` n `23`; metal avg `0.0057` n `20`; unknown avg `31.2285` n `757`
- 4h: commodity avg `0.1895` n `12`; crypto_alt avg `1.137` n `228`; crypto_major avg `1.4691` n `8`; equity avg `0.508` n `86`; fx avg `-0.0299` n `6`; index avg `0.0699` n `23`; metal avg `0.0197` n `20`; unknown avg `0.0003` n `741`
- 24h: commodity avg `-0.3018` n `12`; crypto_alt avg `-1.0201` n `228`; crypto_major avg `-0.5984` n `8`; equity avg `0.1557` n `86`; fx avg `-0.0477` n `6`; index avg `0.5376` n `23`; metal avg `-1.7978` n `20`; unknown avg `-0.8757` n `708`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
