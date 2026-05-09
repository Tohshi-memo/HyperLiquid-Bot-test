# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T18:37:23.850597+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.75` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0082` n `12`; crypto_alt avg `0.1127` n `228`; crypto_major avg `0.1105` n `8`; equity avg `0.0394` n `65`; fx avg `-0.0017` n `5`; index avg `-0.0172` n `23`; metal avg `0.0144` n `18`; unknown avg `-0.0453` n `376`
- 1h: commodity avg `-0.0311` n `12`; crypto_alt avg `-0.0531` n `228`; crypto_major avg `0.0498` n `8`; equity avg `-0.0026` n `65`; fx avg `-0.0051` n `5`; index avg `-0.034` n `23`; metal avg `0.0471` n `18`; unknown avg `-0.0328` n `376`
- 4h: commodity avg `0.1264` n `12`; crypto_alt avg `0.7797` n `228`; crypto_major avg `0.5328` n `8`; equity avg `0.1927` n `65`; fx avg `-0.0236` n `5`; index avg `0.0591` n `23`; metal avg `0.0583` n `18`; unknown avg `0.2699` n `376`
- 24h: commodity avg `0.2134` n `12`; crypto_alt avg `0.4669` n `228`; crypto_major avg `0.4327` n `8`; equity avg `1.1782` n `65`; fx avg `-0.0147` n `5`; index avg `0.3495` n `23`; metal avg `-0.2136` n `18`; unknown avg `-0.1063` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
