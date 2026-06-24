# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T13:07:30.762337+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.191` n `12`; crypto_alt avg `-0.4022` n `228`; crypto_major avg `-0.4565` n `8`; equity avg `-0.1705` n `86`; fx avg `-0.003` n `6`; index avg `-0.0146` n `23`; metal avg `-0.1813` n `20`; unknown avg `-0.0345` n `764`
- 1h: commodity avg `-0.1998` n `12`; crypto_alt avg `-0.8195` n `228`; crypto_major avg `-0.8578` n `8`; equity avg `-0.5061` n `86`; fx avg `-0.0278` n `6`; index avg `-0.0693` n `23`; metal avg `-0.4676` n `20`; unknown avg `-0.0705` n `764`
- 4h: commodity avg `-0.3299` n `12`; crypto_alt avg `-0.702` n `228`; crypto_major avg `-0.7334` n `8`; equity avg `-0.4542` n `86`; fx avg `-0.079` n `6`; index avg `-0.0109` n `23`; metal avg `-1.1325` n `20`; unknown avg `-0.1452` n `764`
- 24h: commodity avg `-0.7674` n `12`; crypto_alt avg `-0.3264` n `228`; crypto_major avg `-0.4207` n `8`; equity avg `4.6223` n `86`; fx avg `-0.037` n `6`; index avg `0.2051` n `23`; metal avg `-1.5582` n `20`; unknown avg `-0.1984` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
