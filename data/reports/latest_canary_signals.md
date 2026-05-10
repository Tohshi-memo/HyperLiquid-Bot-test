# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T06:37:14.097342+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0047` n `12`; crypto_alt avg `-0.01` n `228`; crypto_major avg `-0.0195` n `8`; equity avg `-0.0036` n `65`; fx avg `0.0` n `5`; index avg `-0.0354` n `23`; metal avg `-0.0195` n `18`; unknown avg `-0.263` n `376`
- 1h: commodity avg `-0.0099` n `12`; crypto_alt avg `-0.2332` n `228`; crypto_major avg `-0.0812` n `8`; equity avg `-0.0066` n `65`; fx avg `0.0013` n `5`; index avg `-0.0261` n `23`; metal avg `-0.087` n `18`; unknown avg `0.1562` n `366`
- 4h: commodity avg `-0.1133` n `12`; crypto_alt avg `0.0405` n `228`; crypto_major avg `0.01` n `8`; equity avg `0.2581` n `65`; fx avg `0.0036` n `5`; index avg `-0.0027` n `23`; metal avg `0.2359` n `18`; unknown avg `0.1738` n `366`
- 24h: commodity avg `0.1689` n `12`; crypto_alt avg `-1.3684` n `228`; crypto_major avg `-0.5639` n `8`; equity avg `0.9481` n `65`; fx avg `-0.0244` n `5`; index avg `0.295` n `23`; metal avg `0.4128` n `18`; unknown avg `-0.2469` n `366`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
