# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T09:07:27.932057+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0136` n `12`; crypto_alt avg `-0.0829` n `230`; crypto_major avg `-0.0873` n `8`; equity avg `-0.0377` n `114`; fx avg `-0.0008` n `6`; index avg `-0.0008` n `25`; metal avg `0.0069` n `20`; unknown avg `0.0617` n `791`
- 1h: commodity avg `0.011` n `12`; crypto_alt avg `-0.0317` n `230`; crypto_major avg `-0.1919` n `8`; equity avg `-0.0282` n `114`; fx avg `-0.0075` n `6`; index avg `0.007` n `25`; metal avg `-0.0` n `20`; unknown avg `-0.0633` n `791`
- 4h: commodity avg `-0.1858` n `12`; crypto_alt avg `-0.0599` n `230`; crypto_major avg `-0.3849` n `8`; equity avg `-0.0634` n `114`; fx avg `0.0021` n `6`; index avg `-0.0043` n `25`; metal avg `0.0072` n `20`; unknown avg `-0.0858` n `759`
- 24h: commodity avg `-0.1723` n `12`; crypto_alt avg `0.8092` n `230`; crypto_major avg `-0.2451` n `8`; equity avg `-0.3638` n `114`; fx avg `0.1495` n `6`; index avg `-0.0989` n `25`; metal avg `0.2167` n `20`; unknown avg `-0.0814` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2164`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1773`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1765`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1543`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1524`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1471`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
