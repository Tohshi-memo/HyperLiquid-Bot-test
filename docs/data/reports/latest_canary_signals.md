# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T19:07:34.307375+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1331` n `12`; crypto_alt avg `-0.0311` n `234`; crypto_major avg `-0.1295` n `8`; equity avg `-0.1228` n `141`; fx avg `0.0075` n `6`; index avg `-0.0191` n `26`; metal avg `-0.0441` n `20`; unknown avg `1.3813` n `939`
- 1h: commodity avg `0.08` n `12`; crypto_alt avg `0.6018` n `234`; crypto_major avg `0.5887` n `8`; equity avg `0.3545` n `141`; fx avg `0.0051` n `6`; index avg `0.0401` n `26`; metal avg `0.0714` n `20`; unknown avg `11.246` n `939`
- 4h: commodity avg `0.0748` n `12`; crypto_alt avg `1.3662` n `234`; crypto_major avg `1.2747` n `8`; equity avg `0.8761` n `141`; fx avg `-0.0016` n `6`; index avg `0.124` n `26`; metal avg `0.2274` n `20`; unknown avg `12.0046` n `927`
- 24h: commodity avg `1.032` n `12`; crypto_alt avg `3.7106` n `234`; crypto_major avg `1.5213` n `8`; equity avg `-0.3994` n `141`; fx avg `0.0473` n `6`; index avg `-0.1099` n `26`; metal avg `-0.1571` n `20`; unknown avg `266.9207` n `831`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1602`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
