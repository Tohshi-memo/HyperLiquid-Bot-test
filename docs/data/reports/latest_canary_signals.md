# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T23:37:29.482771+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0233` n `12`; crypto_alt avg `0.0708` n `230`; crypto_major avg `0.0946` n `8`; equity avg `-0.0064` n `114`; fx avg `-0.0685` n `6`; index avg `0.0007` n `25`; metal avg `0.0036` n `20`; unknown avg `0.082` n `791`
- 1h: commodity avg `0.024` n `12`; crypto_alt avg `0.1694` n `230`; crypto_major avg `0.1961` n `8`; equity avg `0.0171` n `114`; fx avg `-0.0597` n `6`; index avg `-0.0016` n `25`; metal avg `0.0134` n `20`; unknown avg `0.0043` n `791`
- 4h: commodity avg `0.0591` n `12`; crypto_alt avg `0.3987` n `230`; crypto_major avg `0.3122` n `8`; equity avg `0.222` n `114`; fx avg `-0.0567` n `6`; index avg `0.022` n `25`; metal avg `0.0144` n `20`; unknown avg `0.5306` n `791`
- 24h: commodity avg `0.2315` n `12`; crypto_alt avg `0.2718` n `230`; crypto_major avg `-0.7609` n `8`; equity avg `-0.5087` n `114`; fx avg `0.0165` n `6`; index avg `-0.1068` n `25`; metal avg `0.2001` n `20`; unknown avg `-0.1562` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2168`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1932`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1636`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.158`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1518`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1509`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
