# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T11:22:13.758694+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0289` n `12`; crypto_alt avg `-0.3057` n `228`; crypto_major avg `-0.2988` n `8`; equity avg `0.0287` n `65`; fx avg `-0.0034` n `5`; index avg `0.008` n `23`; metal avg `0.0073` n `18`; unknown avg `0.2367` n `376`
- 1h: commodity avg `0.13` n `12`; crypto_alt avg `-0.0251` n `228`; crypto_major avg `-0.1539` n `8`; equity avg `0.0107` n `65`; fx avg `-0.0026` n `5`; index avg `0.0123` n `23`; metal avg `0.0223` n `18`; unknown avg `0.2632` n `376`
- 4h: commodity avg `-0.0086` n `12`; crypto_alt avg `0.0146` n `228`; crypto_major avg `-0.1705` n `8`; equity avg `-0.0027` n `65`; fx avg `0.0064` n `5`; index avg `0.0216` n `23`; metal avg `0.0468` n `18`; unknown avg `0.1171` n `376`
- 24h: commodity avg `0.1691` n `12`; crypto_alt avg `-0.5101` n `228`; crypto_major avg `-0.4493` n `8`; equity avg `0.8951` n `65`; fx avg `-0.0273` n `5`; index avg `0.3166` n `23`; metal avg `0.44` n `18`; unknown avg `0.4039` n `366`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
