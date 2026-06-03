# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T13:37:24.991612+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0296` n `12`; crypto_alt avg `-0.1161` n `228`; crypto_major avg `-0.2754` n `8`; equity avg `-1.0485` n `72`; fx avg `0.022` n `6`; index avg `-0.3001` n `23`; metal avg `-0.1552` n `18`; unknown avg `0.1392` n `420`
- 1h: commodity avg `-0.594` n `12`; crypto_alt avg `0.1767` n `228`; crypto_major avg `-0.2861` n `8`; equity avg `-0.9279` n `72`; fx avg `-0.0204` n `6`; index avg `-0.2564` n `23`; metal avg `-0.0315` n `18`; unknown avg `0.1617` n `420`
- 4h: commodity avg `-0.7785` n `12`; crypto_alt avg `0.8973` n `228`; crypto_major avg `-0.1035` n `8`; equity avg `-1.0129` n `72`; fx avg `-0.0165` n `6`; index avg `-0.3379` n `23`; metal avg `-0.274` n `18`; unknown avg `-0.2085` n `420`
- 24h: commodity avg `0.945` n `12`; crypto_alt avg `-1.0255` n `228`; crypto_major avg `-3.5278` n `8`; equity avg `-0.1945` n `72`; fx avg `0.0175` n `6`; index avg `0.524` n `23`; metal avg `-1.5418` n `18`; unknown avg `-0.5081` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0537`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0522`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0446`, n `668`, weak_sample_signal
