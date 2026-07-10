# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T16:52:30.440016+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0013` n `12`; crypto_alt avg `0.2562` n `229`; crypto_major avg `0.3206` n `8`; equity avg `0.1937` n `92`; fx avg `0.0032` n `6`; index avg `0.0296` n `25`; metal avg `-0.0476` n `20`; unknown avg `0.073` n `765`
- 1h: commodity avg `0.1904` n `12`; crypto_alt avg `0.354` n `229`; crypto_major avg `0.3159` n `8`; equity avg `0.5299` n `92`; fx avg `-0.0017` n `6`; index avg `0.0954` n `25`; metal avg `-0.0079` n `20`; unknown avg `0.0621` n `765`
- 4h: commodity avg `-0.2912` n `12`; crypto_alt avg `-0.1566` n `229`; crypto_major avg `-0.2604` n `8`; equity avg `-0.1997` n `92`; fx avg `-0.0639` n `6`; index avg `0.1148` n `25`; metal avg `0.087` n `20`; unknown avg `-0.2604` n `765`
- 24h: commodity avg `-0.3979` n `12`; crypto_alt avg `1.3473` n `229`; crypto_major avg `1.5568` n `8`; equity avg `-0.5433` n `92`; fx avg `-0.1596` n `6`; index avg `0.0722` n `25`; metal avg `-0.1977` n `20`; unknown avg `-0.1887` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
