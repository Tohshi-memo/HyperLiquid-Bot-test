# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T19:37:13.809768+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.01` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0035` n `12`; crypto_alt avg `0.0169` n `228`; crypto_major avg `-0.011` n `8`; equity avg `-0.0166` n `65`; fx avg `0.0` n `5`; index avg `0.0042` n `23`; metal avg `0.012` n `18`; unknown avg `-0.2921` n `376`
- 1h: commodity avg `0.0236` n `12`; crypto_alt avg `-0.065` n `228`; crypto_major avg `-0.1167` n `8`; equity avg `0.0051` n `65`; fx avg `-0.006` n `5`; index avg `0.0425` n `23`; metal avg `0.0089` n `18`; unknown avg `-0.1009` n `376`
- 4h: commodity avg `0.0624` n `12`; crypto_alt avg `0.7575` n `228`; crypto_major avg `0.3396` n `8`; equity avg `0.1097` n `65`; fx avg `-0.0178` n `5`; index avg `0.0518` n `23`; metal avg `0.1007` n `18`; unknown avg `-0.1753` n `376`
- 24h: commodity avg `0.189` n `12`; crypto_alt avg `0.5412` n `228`; crypto_major avg `0.3734` n `8`; equity avg `1.0845` n `65`; fx avg `-0.0619` n `5`; index avg `0.3934` n `23`; metal avg `-0.2239` n `18`; unknown avg `0.0354` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
