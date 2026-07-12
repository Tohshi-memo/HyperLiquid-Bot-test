# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T07:07:35.071773+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0127` n `12`; crypto_alt avg `0.1359` n `230`; crypto_major avg `0.189` n `8`; equity avg `0.0014` n `92`; fx avg `0.0128` n `6`; index avg `-0.0086` n `25`; metal avg `0.0073` n `20`; unknown avg `2.9336` n `763`
- 1h: commodity avg `0.0685` n `12`; crypto_alt avg `0.1549` n `230`; crypto_major avg `0.137` n `8`; equity avg `-0.0364` n `92`; fx avg `0.0047` n `6`; index avg `-0.026` n `25`; metal avg `-0.0001` n `20`; unknown avg `0.0171` n `763`
- 4h: commodity avg `-0.0243` n `12`; crypto_alt avg `-0.2368` n `230`; crypto_major avg `-0.3001` n `8`; equity avg `-0.1575` n `92`; fx avg `0.0005` n `6`; index avg `-0.0283` n `25`; metal avg `-0.0104` n `20`; unknown avg `-0.2315` n `747`
- 24h: commodity avg `0.4404` n `12`; crypto_alt avg `-0.7171` n `230`; crypto_major avg `-0.6821` n `8`; equity avg `-0.1694` n `92`; fx avg `0.0026` n `6`; index avg `-0.1406` n `25`; metal avg `-0.0936` n `20`; unknown avg `-0.0076` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1761`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
