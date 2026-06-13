# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T04:37:29.478544+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0872` n `12`; crypto_alt avg `0.2057` n `228`; crypto_major avg `0.1027` n `8`; equity avg `-0.0442` n `74`; fx avg `0.002` n `6`; index avg `-0.0562` n `23`; metal avg `-0.0031` n `18`; unknown avg `-0.1735` n `643`
- 1h: commodity avg `0.1453` n `12`; crypto_alt avg `0.182` n `228`; crypto_major avg `0.1097` n `8`; equity avg `-0.1305` n `74`; fx avg `0.0115` n `6`; index avg `-0.0618` n `23`; metal avg `-0.0516` n `18`; unknown avg `0.8855` n `643`
- 4h: commodity avg `0.0377` n `12`; crypto_alt avg `0.444` n `228`; crypto_major avg `-0.1018` n `8`; equity avg `-0.3135` n `74`; fx avg `-0.0026` n `6`; index avg `0.041` n `23`; metal avg `-0.0516` n `18`; unknown avg `-0.4197` n `643`
- 24h: commodity avg `-0.4696` n `12`; crypto_alt avg `-0.0153` n `228`; crypto_major avg `-0.478` n `8`; equity avg `-0.9441` n `74`; fx avg `-0.0081` n `6`; index avg `0.5186` n `23`; metal avg `0.3384` n `18`; unknown avg `40.1614` n `515`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0545`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0541`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0506`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0504`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.049`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0482`, n `668`, weak_sample_signal
