# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T21:26:54.713422+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0115` n `12`; crypto_alt avg `-0.0303` n `228`; crypto_major avg `-0.0679` n `8`; equity avg `0.011` n `65`; fx avg `-0.0289` n `5`; index avg `-0.0003` n `23`; metal avg `0.002` n `18`; unknown avg `0.0608` n `376`
- 1h: commodity avg `-0.0013` n `12`; crypto_alt avg `0.002` n `228`; crypto_major avg `-0.0224` n `8`; equity avg `0.1014` n `65`; fx avg `-0.0127` n `5`; index avg `0.0139` n `23`; metal avg `0.0179` n `18`; unknown avg `0.0214` n `376`
- 4h: commodity avg `-0.0073` n `12`; crypto_alt avg `0.0936` n `228`; crypto_major avg `0.0495` n `8`; equity avg `0.315` n `65`; fx avg `-0.0117` n `5`; index avg `0.0358` n `23`; metal avg `0.1368` n `18`; unknown avg `-0.0995` n `376`
- 24h: commodity avg `0.2793` n `12`; crypto_alt avg `0.4748` n `228`; crypto_major avg `0.4127` n `8`; equity avg `0.8587` n `65`; fx avg `-0.0352` n `5`; index avg `0.4253` n `23`; metal avg `0.0429` n `18`; unknown avg `0.2161` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
