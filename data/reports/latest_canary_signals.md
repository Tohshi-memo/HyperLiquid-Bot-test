# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T20:22:49.496837+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0296` n `12`; crypto_alt avg `-0.1784` n `234`; crypto_major avg `-0.1743` n `8`; equity avg `0.042` n `141`; fx avg `-0.0056` n `6`; index avg `0.006` n `26`; metal avg `-0.0148` n `20`; unknown avg `0.6389` n `903`
- 1h: commodity avg `0.0598` n `12`; crypto_alt avg `-0.2935` n `234`; crypto_major avg `-0.202` n `8`; equity avg `-0.1719` n `141`; fx avg `0.0006` n `6`; index avg `0.0007` n `26`; metal avg `0.0031` n `20`; unknown avg `304.9562` n `871`
- 4h: commodity avg `0.1485` n `12`; crypto_alt avg `-0.7941` n `234`; crypto_major avg `-0.2566` n `8`; equity avg `-0.2933` n `141`; fx avg `-0.0194` n `6`; index avg `-0.0272` n `26`; metal avg `0.0046` n `20`; unknown avg `4.2042` n `863`
- 24h: commodity avg `0.6226` n `12`; crypto_alt avg `-3.4539` n `234`; crypto_major avg `-3.4471` n `8`; equity avg `-1.5696` n `140`; fx avg `0.0182` n `6`; index avg `-0.3586` n `26`; metal avg `-0.8443` n `20`; unknown avg `1.5485` n `828`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1628`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
