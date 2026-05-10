# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T12:22:18.589711+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0094` n `12`; crypto_alt avg `0.1327` n `228`; crypto_major avg `0.0243` n `8`; equity avg `0.0185` n `65`; fx avg `0.0` n `5`; index avg `-0.0171` n `23`; metal avg `0.0321` n `18`; unknown avg `0.094` n `376`
- 1h: commodity avg `-0.0067` n `12`; crypto_alt avg `-0.0229` n `228`; crypto_major avg `-0.0103` n `8`; equity avg `0.0581` n `65`; fx avg `-0.0074` n `5`; index avg `-0.0122` n `23`; metal avg `0.0608` n `18`; unknown avg `-0.0659` n `376`
- 4h: commodity avg `0.0737` n `12`; crypto_alt avg `-0.2231` n `228`; crypto_major avg `-0.2581` n `8`; equity avg `0.0439` n `65`; fx avg `-0.004` n `5`; index avg `0.0144` n `23`; metal avg `0.1271` n `18`; unknown avg `0.2991` n `376`
- 24h: commodity avg `0.2311` n `12`; crypto_alt avg `-0.4344` n `228`; crypto_major avg `-0.4402` n `8`; equity avg `0.9799` n `65`; fx avg `-0.0214` n `5`; index avg `0.3269` n `23`; metal avg `0.4732` n `18`; unknown avg `0.5364` n `366`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
