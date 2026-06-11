# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T19:52:40.634620+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.8356` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0018` n `12`; crypto_alt avg `-0.173` n `228`; crypto_major avg `-0.31` n `8`; equity avg `-0.0539` n `74`; fx avg `0.0035` n `6`; index avg `-0.0812` n `23`; metal avg `-0.0846` n `18`; unknown avg `-0.2188` n `556`
- 1h: commodity avg `-0.8424` n `12`; crypto_alt avg `0.1171` n `228`; crypto_major avg `0.1818` n `8`; equity avg `0.8744` n `74`; fx avg `0.0151` n `6`; index avg `0.3796` n `23`; metal avg `0.8343` n `18`; unknown avg `-0.2331` n `556`
- 4h: commodity avg `-1.7221` n `12`; crypto_alt avg `1.4353` n `228`; crypto_major avg `2.1135` n `8`; equity avg `2.3876` n `74`; fx avg `0.0451` n `6`; index avg `1.3011` n `23`; metal avg `2.6895` n `18`; unknown avg `0.3353` n `556`
- 24h: commodity avg `-1.9583` n `12`; crypto_alt avg `3.6854` n `228`; crypto_major avg `3.9108` n `8`; equity avg `3.3773` n `74`; fx avg `0.0144` n `6`; index avg `2.1485` n `23`; metal avg `3.2578` n `18`; unknown avg `2.2728` n `530`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
