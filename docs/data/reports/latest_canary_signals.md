# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T17:07:22.118629+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1715` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0465` n `12`; crypto_alt avg `0.2147` n `228`; crypto_major avg `0.2928` n `8`; equity avg `0.1347` n `66`; fx avg `-0.0204` n `5`; index avg `0.0708` n `23`; metal avg `0.1565` n `18`; unknown avg `0.0193` n `384`
- 1h: commodity avg `-0.0406` n `12`; crypto_alt avg `0.3779` n `228`; crypto_major avg `0.5098` n `8`; equity avg `0.1242` n `66`; fx avg `-0.0143` n `5`; index avg `0.068` n `23`; metal avg `0.3086` n `18`; unknown avg `0.2204` n `384`
- 4h: commodity avg `1.1705` n `12`; crypto_alt avg `-0.5834` n `228`; crypto_major avg `-1.001` n `8`; equity avg `-2.1397` n `66`; fx avg `-0.0028` n `5`; index avg `-0.9316` n `23`; metal avg `-0.0276` n `18`; unknown avg `0.1588` n `383`
- 24h: commodity avg `1.0165` n `12`; crypto_alt avg `-2.0851` n `228`; crypto_major avg `-1.5392` n `8`; equity avg `-0.6244` n `66`; fx avg `0.0257` n `5`; index avg `-0.3163` n `23`; metal avg `0.7582` n `18`; unknown avg `-0.191` n `363`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1624`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1583`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
