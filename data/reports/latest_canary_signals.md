# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T19:37:29.041092+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.5315` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0073` n `12`; crypto_alt avg `0.3108` n `234`; crypto_major avg `0.3266` n `8`; equity avg `0.0205` n `140`; fx avg `0.0201` n `6`; index avg `-0.0015` n `26`; metal avg `0.0001` n `20`; unknown avg `0.9979` n `943`
- 1h: commodity avg `0.0248` n `12`; crypto_alt avg `0.1665` n `234`; crypto_major avg `0.2948` n `8`; equity avg `0.0457` n `140`; fx avg `-0.0114` n `6`; index avg `-0.0032` n `26`; metal avg `0.0106` n `20`; unknown avg `1.1265` n `941`
- 4h: commodity avg `0.016` n `12`; crypto_alt avg `2.1656` n `234`; crypto_major avg `1.5297` n `8`; equity avg `0.2475` n `140`; fx avg `0.0035` n `6`; index avg `0.0301` n `26`; metal avg `-0.0018` n `20`; unknown avg `2.6776` n `871`
- 24h: commodity avg `0.3879` n `12`; crypto_alt avg `0.2085` n `234`; crypto_major avg `-0.3001` n `8`; equity avg `-0.0762` n `140`; fx avg `-0.0342` n `6`; index avg `-0.0421` n `26`; metal avg `-0.0316` n `20`; unknown avg `3.1152` n `819`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
