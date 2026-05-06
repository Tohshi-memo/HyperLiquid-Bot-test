# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T22:07:14.217078+00:00`
- Correlation status: `ready`
- Asset price records: `492`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.87` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1647` n `12`; crypto_alt avg `-0.3617` n `228`; crypto_major avg `-0.2119` n `8`; equity avg `0.0914` n `65`; fx avg `-0.0073` n `4`; index avg `0.0097` n `23`; metal avg `-0.063` n `18`; unknown avg `-0.0001` n `356`
- 1h: commodity avg `-0.1779` n `12`; crypto_alt avg `0.1287` n `228`; crypto_major avg `-0.0241` n `8`; equity avg `-0.2573` n `65`; fx avg `0.0007` n `4`; index avg `-0.04` n `23`; metal avg `-0.0432` n `18`; unknown avg `0.0145` n `356`
- 4h: commodity avg `0.1927` n `12`; crypto_alt avg `0.3695` n `228`; crypto_major avg `0.0812` n `8`; equity avg `0.0338` n `65`; fx avg `-0.0262` n `4`; index avg `0.1609` n `23`; metal avg `0.1912` n `18`; unknown avg `0.167` n `356`
- 24h: commodity avg `-2.3405` n `7`; crypto_alt avg `2.0202` n `223`; crypto_major avg `-0.0802` n `7`; equity avg `1.9478` n `47`; fx avg `-0.6107` n `4`; index avg `1.4425` n `6`; metal avg `3.4836` n `7`; unknown avg `3.9837` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1314`, n `488`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1178`, n `488`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0968`, n `484`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0884`, n `484`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0869`, n `484`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0764`, n `484`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0761`, n `484`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0738`, n `488`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0647`, n `488`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.063`, n `484`, weak_sample_signal
