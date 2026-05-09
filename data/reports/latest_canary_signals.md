# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T19:07:18.446840+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `6.76` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0041` n `12`; crypto_alt avg `0.0542` n `228`; crypto_major avg `0.0034` n `8`; equity avg `0.018` n `65`; fx avg `-0.006` n `5`; index avg `0.0079` n `23`; metal avg `-0.0027` n `18`; unknown avg `0.1447` n `376`
- 1h: commodity avg `0.0156` n `12`; crypto_alt avg `0.0819` n `228`; crypto_major avg `0.0434` n `8`; equity avg `0.0848` n `65`; fx avg `-0.011` n `5`; index avg `0.0351` n `23`; metal avg `0.0262` n `18`; unknown avg `0.1032` n `376`
- 4h: commodity avg `-0.0766` n `12`; crypto_alt avg `0.8669` n `228`; crypto_major avg `0.5901` n `8`; equity avg `0.2149` n `65`; fx avg `-0.0426` n `5`; index avg `0.0627` n `23`; metal avg `0.087` n `18`; unknown avg `0.2492` n `376`
- 24h: commodity avg `0.1062` n `12`; crypto_alt avg `0.5945` n `228`; crypto_major avg `0.3908` n `8`; equity avg `1.1994` n `65`; fx avg `-0.0298` n `5`; index avg `0.4144` n `23`; metal avg `-0.1505` n `18`; unknown avg `-0.0926` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
