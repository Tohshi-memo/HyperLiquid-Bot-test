# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T09:08:02.649901+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.068` n `12`; crypto_alt avg `0.1407` n `234`; crypto_major avg `0.3539` n `8`; equity avg `-0.0814` n `140`; fx avg `0.0052` n `6`; index avg `-0.0182` n `26`; metal avg `0.0343` n `20`; unknown avg `-0.0832` n `925`
- 1h: commodity avg `-0.043` n `12`; crypto_alt avg `0.3673` n `234`; crypto_major avg `0.5352` n `8`; equity avg `-0.0149` n `140`; fx avg `0.0182` n `6`; index avg `-0.0322` n `26`; metal avg `-0.0003` n `20`; unknown avg `0.3791` n `919`
- 4h: commodity avg `-0.2219` n `12`; crypto_alt avg `0.8922` n `234`; crypto_major avg `0.919` n `8`; equity avg `0.3681` n `140`; fx avg `0.0478` n `6`; index avg `0.0438` n `26`; metal avg `0.2948` n `20`; unknown avg `-0.0496` n `863`
- 24h: commodity avg `-0.3387` n `12`; crypto_alt avg `5.2316` n `234`; crypto_major avg `3.9693` n `8`; equity avg `1.7675` n `140`; fx avg `0.187` n `6`; index avg `0.259` n `26`; metal avg `0.7963` n `20`; unknown avg `2.3426` n `731`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
