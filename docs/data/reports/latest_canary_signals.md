# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T12:18:04.980073+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2679` n `12`; crypto_alt avg `0.0489` n `228`; crypto_major avg `0.0259` n `8`; equity avg `-0.083` n `66`; fx avg `0.0176` n `5`; index avg `-0.0239` n `23`; metal avg `-0.1435` n `18`; unknown avg `0.1268` n `383`
- 1h: commodity avg `-0.2586` n `12`; crypto_alt avg `1.1031` n `228`; crypto_major avg `1.0124` n `8`; equity avg `0.498` n `66`; fx avg `-0.0061` n `5`; index avg `0.2345` n `23`; metal avg `0.4378` n `18`; unknown avg `0.4978` n `383`
- 4h: commodity avg `-0.1561` n `12`; crypto_alt avg `0.7748` n `228`; crypto_major avg `0.6838` n `8`; equity avg `0.0214` n `66`; fx avg `0.0574` n `5`; index avg `-0.0069` n `23`; metal avg `0.2118` n `18`; unknown avg `0.0121` n `383`
- 24h: commodity avg `0.5614` n `12`; crypto_alt avg `-2.0846` n `228`; crypto_major avg `-1.0486` n `8`; equity avg `0.3011` n `65`; fx avg `0.102` n `5`; index avg `0.1717` n `23`; metal avg `0.3197` n `18`; unknown avg `-0.4217` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
