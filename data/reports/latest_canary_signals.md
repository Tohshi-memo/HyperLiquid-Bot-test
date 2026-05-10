# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T11:07:23.694072+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0071` n `12`; crypto_alt avg `0.0788` n `228`; crypto_major avg `0.0582` n `8`; equity avg `0.011` n `65`; fx avg `0.0` n `5`; index avg `-0.0064` n `23`; metal avg `0.0021` n `18`; unknown avg `-0.1812` n `376`
- 1h: commodity avg `0.087` n `12`; crypto_alt avg `0.4397` n `228`; crypto_major avg `0.1507` n `8`; equity avg `0.0241` n `65`; fx avg `0.0008` n `5`; index avg `0.0057` n `23`; metal avg `0.019` n `18`; unknown avg `-0.0827` n `376`
- 4h: commodity avg `-0.0099` n `12`; crypto_alt avg `0.5017` n `228`; crypto_major avg `0.1599` n `8`; equity avg `-0.0574` n `65`; fx avg `0.0104` n `5`; index avg `0.0155` n `23`; metal avg `0.0306` n `18`; unknown avg `0.1501` n `376`
- 24h: commodity avg `0.1443` n `12`; crypto_alt avg `-0.1887` n `228`; crypto_major avg `-0.0423` n `8`; equity avg `0.8622` n `65`; fx avg `-0.0214` n `5`; index avg `0.3113` n `23`; metal avg `0.4438` n `18`; unknown avg `0.2122` n `366`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
