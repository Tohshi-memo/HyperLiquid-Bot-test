# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T06:52:26.729578+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0287` n `12`; crypto_alt avg `-0.027` n `234`; crypto_major avg `-0.1665` n `8`; equity avg `-0.0704` n `141`; fx avg `-0.0048` n `6`; index avg `-0.0077` n `26`; metal avg `-0.0344` n `20`; unknown avg `0.0716` n `945`
- 1h: commodity avg `0.0563` n `12`; crypto_alt avg `0.0548` n `234`; crypto_major avg `-0.1245` n `8`; equity avg `-0.3595` n `141`; fx avg `0.0196` n `6`; index avg `-0.0523` n `26`; metal avg `-0.0664` n `20`; unknown avg `0.5991` n `927`
- 4h: commodity avg `0.2456` n `12`; crypto_alt avg `0.4659` n `234`; crypto_major avg `-0.1032` n `8`; equity avg `-0.6182` n `141`; fx avg `0.0219` n `6`; index avg `-0.104` n `26`; metal avg `-0.0473` n `20`; unknown avg `2.8299` n `921`
- 24h: commodity avg `0.731` n `12`; crypto_alt avg `-4.2382` n `234`; crypto_major avg `-4.0338` n `8`; equity avg `-2.275` n `140`; fx avg `0.0268` n `6`; index avg `-0.4653` n `26`; metal avg `-0.6105` n `20`; unknown avg `586.0378` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1836`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1612`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1483`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
