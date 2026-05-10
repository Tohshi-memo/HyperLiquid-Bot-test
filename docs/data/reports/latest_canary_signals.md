# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T07:22:17.189815+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0277` n `12`; crypto_alt avg `0.1785` n `228`; crypto_major avg `0.0308` n `8`; equity avg `-0.0305` n `65`; fx avg `0.0006` n `5`; index avg `0.0019` n `23`; metal avg `-0.009` n `18`; unknown avg `0.0967` n `376`
- 1h: commodity avg `-0.0061` n `12`; crypto_alt avg `0.3094` n `228`; crypto_major avg `0.1369` n `8`; equity avg `0.0263` n `65`; fx avg `0.0013` n `5`; index avg `-0.0224` n `23`; metal avg `-0.0787` n `18`; unknown avg `-0.1089` n `376`
- 4h: commodity avg `-0.0925` n `12`; crypto_alt avg `0.447` n `228`; crypto_major avg `0.2626` n `8`; equity avg `0.1653` n `65`; fx avg `0.0036` n `5`; index avg `0.015` n `23`; metal avg `0.1301` n `18`; unknown avg `-0.0282` n `366`
- 24h: commodity avg `0.1938` n `12`; crypto_alt avg `-0.9279` n `228`; crypto_major avg `-0.4415` n `8`; equity avg `0.9852` n `65`; fx avg `-0.0242` n `5`; index avg `0.2763` n `23`; metal avg `0.3509` n `18`; unknown avg `0.0801` n `366`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
