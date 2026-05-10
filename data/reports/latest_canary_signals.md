# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T12:07:17.506867+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0101` n `12`; crypto_alt avg `-0.1946` n `228`; crypto_major avg `-0.0874` n `8`; equity avg `0.0006` n `65`; fx avg `-0.0008` n `5`; index avg `-0.0053` n `23`; metal avg `0.0021` n `18`; unknown avg `0.2492` n `376`
- 1h: commodity avg `0.0316` n `12`; crypto_alt avg `-0.4604` n `228`; crypto_major avg `-0.3333` n `8`; equity avg `0.069` n `65`; fx avg `-0.0108` n `5`; index avg `0.0129` n `23`; metal avg `0.036` n `18`; unknown avg `0.0712` n `376`
- 4h: commodity avg `0.0819` n `12`; crypto_alt avg `-0.1384` n `228`; crypto_major avg `-0.19` n `8`; equity avg `0.0166` n `65`; fx avg `-0.0027` n `5`; index avg `0.0252` n `23`; metal avg `0.1068` n `18`; unknown avg `0.3563` n `376`
- 24h: commodity avg `0.2697` n `12`; crypto_alt avg `-0.709` n `228`; crypto_major avg `-0.5234` n `8`; equity avg `0.9289` n `65`; fx avg `-0.0214` n `5`; index avg `0.3293` n `23`; metal avg `0.4312` n `18`; unknown avg `-0.0959` n `366`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
