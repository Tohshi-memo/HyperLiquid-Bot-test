# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T02:22:28.407636+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0002` n `12`; crypto_alt avg `0.0959` n `230`; crypto_major avg `0.1082` n `8`; equity avg `0.014` n `114`; fx avg `0.0026` n `6`; index avg `-0.0026` n `25`; metal avg `0.0006` n `20`; unknown avg `0.2161` n `791`
- 1h: commodity avg `0.038` n `12`; crypto_alt avg `0.1548` n `230`; crypto_major avg `0.1907` n `8`; equity avg `0.0347` n `114`; fx avg `0.0017` n `6`; index avg `0.0024` n `25`; metal avg `-0.0124` n `20`; unknown avg `0.385` n `791`
- 4h: commodity avg `-0.0231` n `12`; crypto_alt avg `0.3688` n `230`; crypto_major avg `0.5` n `8`; equity avg `-0.0094` n `114`; fx avg `-0.026` n `6`; index avg `-0.0086` n `25`; metal avg `0.0347` n `20`; unknown avg `0.4659` n `791`
- 24h: commodity avg `0.2432` n `12`; crypto_alt avg `0.0612` n `230`; crypto_major avg `-0.465` n `8`; equity avg `-0.1644` n `114`; fx avg `0.0957` n `6`; index avg `-0.0503` n `25`; metal avg `0.4966` n `20`; unknown avg `-0.1287` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2172`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1916`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1855`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1658`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1654`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1535`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1529`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1481`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1444`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
