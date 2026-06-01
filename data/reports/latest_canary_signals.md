# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T15:37:25.190290+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.8768` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.1658` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.3332` n `12`; crypto_alt avg `0.5402` n `228`; crypto_major avg `0.3479` n `8`; equity avg `0.3883` n `69`; fx avg `0.0093` n `6`; index avg `0.1116` n `23`; metal avg `0.3035` n `18`; unknown avg `0.2426` n `422`
- 1h: commodity avg `-0.5975` n `12`; crypto_alt avg `0.5818` n `228`; crypto_major avg `0.2577` n `8`; equity avg `1.0508` n `69`; fx avg `0.0184` n `6`; index avg `0.2062` n `23`; metal avg `0.6495` n `18`; unknown avg `0.1322` n `422`
- 4h: commodity avg `0.1842` n `12`; crypto_alt avg `-0.4918` n `228`; crypto_major avg `-1.3533` n `8`; equity avg `0.5235` n `69`; fx avg `-0.0473` n `6`; index avg `-0.1875` n `23`; metal avg `-0.3437` n `18`; unknown avg `1.0974` n `422`
- 24h: commodity avg `0.7717` n `12`; crypto_alt avg `-0.3077` n `228`; crypto_major avg `-1.6954` n `8`; equity avg `0.1777` n `69`; fx avg `-0.0465` n `6`; index avg `0.2357` n `23`; metal avg `0.039` n `18`; unknown avg `3.6803` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2848`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2141`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2111`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1545`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
