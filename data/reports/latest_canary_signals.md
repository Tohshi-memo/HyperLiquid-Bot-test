# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T21:52:20.896936+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0231` n `12`; crypto_alt avg `-0.1915` n `228`; crypto_major avg `-0.1413` n `8`; equity avg `0.0053` n `74`; fx avg `-0.2535` n `6`; index avg `0.2725` n `23`; metal avg `-0.031` n `18`; unknown avg `-0.0089` n `517`
- 1h: commodity avg `0.0186` n `12`; crypto_alt avg `0.4339` n `228`; crypto_major avg `0.6754` n `8`; equity avg `0.079` n `74`; fx avg `-0.3375` n `6`; index avg `0.1729` n `23`; metal avg `0.1263` n `18`; unknown avg `0.2454` n `517`
- 4h: commodity avg `0.1509` n `12`; crypto_alt avg `0.1616` n `228`; crypto_major avg `0.6715` n `8`; equity avg `-0.2448` n `74`; fx avg `-0.3677` n `6`; index avg `0.0595` n `23`; metal avg `0.1479` n `18`; unknown avg `0.0017` n `517`
- 24h: commodity avg `-0.9859` n `12`; crypto_alt avg `4.0702` n `228`; crypto_major avg `4.4626` n `8`; equity avg `2.4773` n `74`; fx avg `-0.629` n `6`; index avg `1.117` n `23`; metal avg `0.2905` n `18`; unknown avg `-1.9488` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
