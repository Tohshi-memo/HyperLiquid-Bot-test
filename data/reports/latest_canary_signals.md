# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T22:37:21.334693+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0047` n `12`; crypto_alt avg `-0.0761` n `228`; crypto_major avg `-0.0531` n `8`; equity avg `0.007` n `65`; fx avg `-0.0008` n `5`; index avg `-0.0087` n `23`; metal avg `0.0128` n `18`; unknown avg `0.2083` n `376`
- 1h: commodity avg `-0.0471` n `12`; crypto_alt avg `-0.0079` n `228`; crypto_major avg `-0.0421` n `8`; equity avg `0.127` n `65`; fx avg `-0.0008` n `5`; index avg `0.0322` n `23`; metal avg `0.0482` n `18`; unknown avg `-0.12` n `376`
- 4h: commodity avg `-0.0074` n `12`; crypto_alt avg `-0.0531` n `228`; crypto_major avg `-0.177` n `8`; equity avg `0.379` n `65`; fx avg `-0.0074` n `5`; index avg `0.1158` n `23`; metal avg `0.1626` n `18`; unknown avg `0.0874` n `376`
- 24h: commodity avg `0.4824` n `12`; crypto_alt avg `-0.005` n `228`; crypto_major avg `0.1804` n `8`; equity avg `0.7657` n `65`; fx avg `-0.0236` n `5`; index avg `0.3529` n `23`; metal avg `0.1896` n `18`; unknown avg `0.3033` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
