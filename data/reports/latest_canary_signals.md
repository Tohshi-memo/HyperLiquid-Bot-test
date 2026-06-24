# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T12:37:39.630085+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0335` n `12`; crypto_alt avg `-0.0222` n `228`; crypto_major avg `-0.0235` n `8`; equity avg `-0.2338` n `86`; fx avg `-0.0057` n `6`; index avg `-0.0494` n `23`; metal avg `-0.2068` n `20`; unknown avg `-0.006` n `764`
- 1h: commodity avg `-0.1141` n `12`; crypto_alt avg `0.5535` n `228`; crypto_major avg `0.3619` n `8`; equity avg `-0.1097` n `86`; fx avg `-0.0235` n `6`; index avg `0.0134` n `23`; metal avg `-0.4534` n `20`; unknown avg `0.0634` n `764`
- 4h: commodity avg `-0.1432` n `12`; crypto_alt avg `0.0515` n `228`; crypto_major avg `0.0087` n `8`; equity avg `-0.2052` n `86`; fx avg `-0.0421` n `6`; index avg `0.0149` n `23`; metal avg `-1.0152` n `20`; unknown avg `-0.1479` n `764`
- 24h: commodity avg `-0.5297` n `12`; crypto_alt avg `0.0126` n `228`; crypto_major avg `0.0827` n `8`; equity avg `4.6753` n `86`; fx avg `-0.0157` n `6`; index avg `0.1931` n `23`; metal avg `-1.2771` n `20`; unknown avg `-0.118` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
