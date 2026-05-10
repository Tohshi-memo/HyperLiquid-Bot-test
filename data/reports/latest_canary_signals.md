# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T03:52:14.437283+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0206` n `12`; crypto_alt avg `-0.0252` n `228`; crypto_major avg `0.0797` n `8`; equity avg `0.0214` n `65`; fx avg `0.0` n `5`; index avg `0.0052` n `23`; metal avg `0.0027` n `18`; unknown avg `-0.198` n `376`
- 1h: commodity avg `-0.0514` n `12`; crypto_alt avg `0.0228` n `228`; crypto_major avg `0.1364` n `8`; equity avg `0.177` n `65`; fx avg `0.0026` n `5`; index avg `-0.0033` n `23`; metal avg `0.0765` n `18`; unknown avg `-0.2858` n `376`
- 4h: commodity avg `-0.0737` n `12`; crypto_alt avg `-0.2934` n `228`; crypto_major avg `-0.0475` n `8`; equity avg `0.2186` n `65`; fx avg `-0.0066` n `5`; index avg `0.0691` n `23`; metal avg `0.1372` n `18`; unknown avg `-0.6243` n `376`
- 24h: commodity avg `0.3672` n `12`; crypto_alt avg `-1.3634` n `228`; crypto_major avg `-0.6169` n `8`; equity avg `0.8931` n `65`; fx avg `-0.0074` n `5`; index avg `0.3167` n `23`; metal avg `0.2338` n `18`; unknown avg `-0.3511` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
