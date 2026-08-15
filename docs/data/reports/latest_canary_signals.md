# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T00:37:23.547453+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0223` n `12`; crypto_alt avg `-0.0331` n `230`; crypto_major avg `0.0029` n `8`; equity avg `0.0091` n `114`; fx avg `0.0026` n `6`; index avg `-0.0025` n `25`; metal avg `0.0271` n `20`; unknown avg `-0.0368` n `791`
- 1h: commodity avg `0.0235` n `12`; crypto_alt avg `0.045` n `230`; crypto_major avg `-0.0208` n `8`; equity avg `-0.0542` n `114`; fx avg `0.0516` n `6`; index avg `-0.0096` n `25`; metal avg `0.051` n `20`; unknown avg `-0.1097` n `791`
- 4h: commodity avg `0.1009` n `12`; crypto_alt avg `0.3906` n `230`; crypto_major avg `0.2967` n `8`; equity avg `0.0096` n `114`; fx avg `-0.0336` n `6`; index avg `-0.0022` n `25`; metal avg `0.1016` n `20`; unknown avg `0.9831` n `791`
- 24h: commodity avg `0.2568` n `12`; crypto_alt avg `0.1133` n `230`; crypto_major avg `-0.6677` n `8`; equity avg `-0.5819` n `114`; fx avg `0.0723` n `6`; index avg `-0.1205` n `25`; metal avg `0.3818` n `20`; unknown avg `-0.3641` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2168`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1953`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1683`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1641`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1567`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1545`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1486`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1425`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
