# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T13:07:22.828130+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0904` n `12`; crypto_alt avg `-0.2373` n `228`; crypto_major avg `-0.0292` n `8`; equity avg `0.0776` n `66`; fx avg `-0.0089` n `5`; index avg `0.0495` n `23`; metal avg `0.0366` n `18`; unknown avg `0.1097` n `383`
- 1h: commodity avg `-0.4296` n `12`; crypto_alt avg `-0.0063` n `228`; crypto_major avg `0.1507` n `8`; equity avg `0.5893` n `66`; fx avg `-0.0256` n `5`; index avg `0.5068` n `23`; metal avg `0.3248` n `18`; unknown avg `0.1282` n `383`
- 4h: commodity avg `-0.8333` n `12`; crypto_alt avg `0.6639` n `228`; crypto_major avg `0.8368` n `8`; equity avg `0.478` n `66`; fx avg `0.004` n `5`; index avg `0.4391` n `23`; metal avg `0.6305` n `18`; unknown avg `0.0672` n `383`
- 24h: commodity avg `-0.175` n `12`; crypto_alt avg `-2.02` n `228`; crypto_major avg `-0.9265` n `8`; equity avg `0.8457` n `65`; fx avg `0.0607` n `5`; index avg `0.6365` n `23`; metal avg `0.7731` n `18`; unknown avg `-0.4364` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
