# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T06:07:14.778868+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0034` n `12`; crypto_alt avg `-0.0728` n `228`; crypto_major avg `0.0252` n `8`; equity avg `0.0058` n `65`; fx avg `0.0` n `5`; index avg `-0.0007` n `23`; metal avg `-0.2364` n `18`; unknown avg `-0.0268` n `366`
- 1h: commodity avg `-0.0181` n `12`; crypto_alt avg `0.2343` n `228`; crypto_major avg `0.0841` n `8`; equity avg `-0.0094` n `65`; fx avg `0.0004` n `5`; index avg `0.0076` n `23`; metal avg `0.1075` n `18`; unknown avg `-0.1173` n `366`
- 4h: commodity avg `-0.1221` n `12`; crypto_alt avg `0.5739` n `228`; crypto_major avg `0.2956` n `8`; equity avg `0.3526` n `65`; fx avg `0.0036` n `5`; index avg `0.0368` n `23`; metal avg `0.2894` n `18`; unknown avg `0.0692` n `366`
- 24h: commodity avg `0.188` n `12`; crypto_alt avg `-1.5464` n `228`; crypto_major avg `-0.754` n `8`; equity avg `0.9749` n `65`; fx avg `-0.0229` n `5`; index avg `0.3382` n `23`; metal avg `0.4626` n `18`; unknown avg `-0.4931` n `366`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
