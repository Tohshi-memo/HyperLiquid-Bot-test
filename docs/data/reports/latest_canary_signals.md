# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T16:37:29.511732+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.437` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.1957` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.1934` n `12`; crypto_alt avg `0.0654` n `234`; crypto_major avg `0.0425` n `8`; equity avg `0.1158` n `141`; fx avg `-0.013` n `6`; index avg `0.016` n `26`; metal avg `0.0275` n `20`; unknown avg `6.3045` n `943`
- 1h: commodity avg `-0.5194` n `12`; crypto_alt avg `0.6425` n `234`; crypto_major avg `0.4913` n `8`; equity avg `0.8743` n `141`; fx avg `-0.0312` n `6`; index avg `0.173` n `26`; metal avg `0.2364` n `20`; unknown avg `6.7598` n `929`
- 4h: commodity avg `0.363` n `12`; crypto_alt avg `3.9478` n `234`; crypto_major avg `2.5587` n `8`; equity avg `1.2546` n `141`; fx avg `-0.01` n `6`; index avg `0.1655` n `26`; metal avg `0.1217` n `20`; unknown avg `9.7418` n `883`
- 24h: commodity avg `0.6444` n `12`; crypto_alt avg `3.326` n `234`; crypto_major avg `1.5627` n `8`; equity avg `-0.52` n `141`; fx avg `0.0174` n `6`; index avg `-0.077` n `26`; metal avg `-0.0495` n `20`; unknown avg `272.6199` n `825`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1723`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1678`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
