# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T11:52:19.033998+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0011` n `12`; crypto_alt avg `-0.0656` n `228`; crypto_major avg `0.0467` n `8`; equity avg `0.0337` n `65`; fx avg `0.0` n `5`; index avg `0.0409` n `23`; metal avg `0.0245` n `18`; unknown avg `-0.143` n `376`
- 1h: commodity avg `0.0488` n `12`; crypto_alt avg `-0.1884` n `228`; crypto_major avg `-0.1882` n `8`; equity avg `0.0786` n `65`; fx avg `-0.01` n `5`; index avg `0.0118` n `23`; metal avg `0.036` n `18`; unknown avg `-0.3629` n `376`
- 4h: commodity avg `0.0958` n `12`; crypto_alt avg `0.019` n `228`; crypto_major avg `-0.1169` n `8`; equity avg `-0.0019` n `65`; fx avg `-0.0004` n `5`; index avg `0.0187` n `23`; metal avg `0.0918` n `18`; unknown avg `0.0216` n `376`
- 24h: commodity avg `0.2669` n `12`; crypto_alt avg `-0.4685` n `228`; crypto_major avg `-0.36` n `8`; equity avg `0.9322` n `65`; fx avg `-0.0206` n `5`; index avg `0.3384` n `23`; metal avg `0.4557` n `18`; unknown avg `-0.0322` n `366`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
