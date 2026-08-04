# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T21:52:25.847112+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0031` n `12`; crypto_alt avg `-0.0217` n `230`; crypto_major avg `-0.017` n `8`; equity avg `-0.0427` n `108`; fx avg `-0.0021` n `6`; index avg `0.0011` n `25`; metal avg `-0.0025` n `20`; unknown avg `-0.0001` n `781`
- 1h: commodity avg `0.0012` n `12`; crypto_alt avg `-0.1401` n `230`; crypto_major avg `-0.1993` n `8`; equity avg `0.0616` n `108`; fx avg `0.007` n `6`; index avg `0.0127` n `25`; metal avg `0.0002` n `20`; unknown avg `0.1288` n `781`
- 4h: commodity avg `-0.0788` n `12`; crypto_alt avg `0.2853` n `230`; crypto_major avg `0.1041` n `8`; equity avg `-0.545` n `108`; fx avg `0.059` n `6`; index avg `0.0044` n `25`; metal avg `-0.1286` n `20`; unknown avg `0.0033` n `781`
- 24h: commodity avg `-1.2524` n `12`; crypto_alt avg `-0.1849` n `230`; crypto_major avg `0.4907` n `8`; equity avg `2.9589` n `107`; fx avg `0.1294` n `6`; index avg `0.7286` n `25`; metal avg `0.8563` n `20`; unknown avg `0.4248` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1541`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1524`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
