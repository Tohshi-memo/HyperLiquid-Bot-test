# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T07:07:14.773635+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.014` n `12`; crypto_alt avg `0.1009` n `228`; crypto_major avg `0.0425` n `8`; equity avg `0.0144` n `65`; fx avg `0.0` n `5`; index avg `0.0019` n `23`; metal avg `-0.003` n `18`; unknown avg `0.1526` n `376`
- 1h: commodity avg `-0.0182` n `12`; crypto_alt avg `-0.0161` n `228`; crypto_major avg `0.0629` n `8`; equity avg `0.0436` n `65`; fx avg `0.0006` n `5`; index avg `-0.0175` n `23`; metal avg `-0.1002` n `18`; unknown avg `0.0335` n `376`
- 4h: commodity avg `-0.1285` n `12`; crypto_alt avg `0.1834` n `228`; crypto_major avg `0.1958` n `8`; equity avg `0.2274` n `65`; fx avg `0.0043` n `5`; index avg `0.0176` n `23`; metal avg `0.1635` n `18`; unknown avg `0.0165` n `366`
- 24h: commodity avg `0.14` n `12`; crypto_alt avg `-1.0585` n `228`; crypto_major avg `-0.4033` n `8`; equity avg `1.0001` n `65`; fx avg `-0.0238` n `5`; index avg `0.2894` n `23`; metal avg `0.3654` n `18`; unknown avg `-0.0991` n `366`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
