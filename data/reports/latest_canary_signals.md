# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T04:20:55.123825+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0018` n `12`; crypto_alt avg `-0.029` n `228`; crypto_major avg `-0.0879` n `8`; equity avg `-0.0074` n `86`; fx avg `-0.0107` n `6`; index avg `-0.0061` n `23`; metal avg `-0.0418` n `20`; unknown avg `2.0373` n `765`
- 1h: commodity avg `0.0362` n `12`; crypto_alt avg `0.0025` n `228`; crypto_major avg `-0.1312` n `8`; equity avg `0.024` n `86`; fx avg `0.0354` n `6`; index avg `0.0084` n `23`; metal avg `0.1924` n `20`; unknown avg `0.9362` n `765`
- 4h: commodity avg `-0.145` n `12`; crypto_alt avg `-0.3324` n `228`; crypto_major avg `-0.3915` n `8`; equity avg `-0.4387` n `86`; fx avg `0.0288` n `6`; index avg `0.0637` n `23`; metal avg `-0.1115` n `20`; unknown avg `0.2865` n `748`
- 24h: commodity avg `-0.5144` n `12`; crypto_alt avg `-1.583` n `228`; crypto_major avg `-1.5784` n `8`; equity avg `0.4478` n `86`; fx avg `0.0757` n `6`; index avg `0.7262` n `23`; metal avg `-1.3198` n `20`; unknown avg `-0.5228` n `708`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
