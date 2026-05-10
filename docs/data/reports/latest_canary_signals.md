# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T13:07:19.898615+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0626` n `12`; crypto_alt avg `0.043` n `228`; crypto_major avg `-0.0323` n `8`; equity avg `0.0123` n `65`; fx avg `-0.0004` n `5`; index avg `0.0099` n `23`; metal avg `0.0396` n `18`; unknown avg `-0.0598` n `376`
- 1h: commodity avg `-0.1467` n `12`; crypto_alt avg `0.2964` n `228`; crypto_major avg `0.038` n `8`; equity avg `0.005` n `65`; fx avg `-0.0002` n `5`; index avg `-0.0436` n `23`; metal avg `0.1038` n `18`; unknown avg `-0.0142` n `376`
- 4h: commodity avg `-0.025` n `12`; crypto_alt avg `-0.2648` n `228`; crypto_major avg `-0.4766` n `8`; equity avg `0.0` n `65`; fx avg `-0.0059` n `5`; index avg `-0.0165` n `23`; metal avg `0.1745` n `18`; unknown avg `-0.1602` n `376`
- 24h: commodity avg `0.0018` n `12`; crypto_alt avg `-0.0718` n `228`; crypto_major avg `-0.2762` n `8`; equity avg `0.8892` n `65`; fx avg `-0.0216` n `5`; index avg `0.2474` n `23`; metal avg `0.5643` n `18`; unknown avg `0.3311` n `366`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
