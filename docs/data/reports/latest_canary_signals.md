# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T18:22:13.913265+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.86` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0127` n `12`; crypto_alt avg `-0.0471` n `228`; crypto_major avg `0.0108` n `8`; equity avg `0.0038` n `65`; fx avg `-0.0034` n `5`; index avg `0.0078` n `23`; metal avg `0.0106` n `18`; unknown avg `0.1699` n `376`
- 1h: commodity avg `-0.0321` n `12`; crypto_alt avg `0.0532` n `228`; crypto_major avg `0.1054` n `8`; equity avg `-0.012` n `65`; fx avg `-0.0034` n `5`; index avg `-0.0036` n `23`; metal avg `0.0272` n `18`; unknown avg `0.2474` n `376`
- 4h: commodity avg `0.1528` n `12`; crypto_alt avg `0.3294` n `228`; crypto_major avg `0.1536` n `8`; equity avg `0.1928` n `65`; fx avg `-0.0219` n `5`; index avg `0.0165` n `23`; metal avg `0.0184` n `18`; unknown avg `0.1962` n `376`
- 24h: commodity avg `0.1486` n `12`; crypto_alt avg `0.5244` n `228`; crypto_major avg `0.4377` n `8`; equity avg `1.2306` n `65`; fx avg `-0.0091` n `5`; index avg `0.2668` n `23`; metal avg `-0.3118` n `18`; unknown avg `0.1177` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
