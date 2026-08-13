# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T11:22:28.327651+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0138` n `12`; crypto_alt avg `-0.0675` n `230`; crypto_major avg `-0.1058` n `8`; equity avg `-0.0559` n `113`; fx avg `-0.0033` n `6`; index avg `-0.0052` n `25`; metal avg `-0.0235` n `20`; unknown avg `-0.0346` n `787`
- 1h: commodity avg `-0.0509` n `12`; crypto_alt avg `-0.1269` n `230`; crypto_major avg `-0.2304` n `8`; equity avg `-0.0201` n `113`; fx avg `-0.0077` n `6`; index avg `0.0022` n `25`; metal avg `0.0175` n `20`; unknown avg `-0.0244` n `787`
- 4h: commodity avg `-0.3015` n `12`; crypto_alt avg `-0.1638` n `230`; crypto_major avg `-0.6135` n `8`; equity avg `0.0073` n `113`; fx avg `-0.0002` n `6`; index avg `0.007` n `25`; metal avg `0.1042` n `20`; unknown avg `-0.065` n `787`
- 24h: commodity avg `-0.3378` n `12`; crypto_alt avg `-0.7964` n `230`; crypto_major avg `-0.7099` n `8`; equity avg `1.3897` n `113`; fx avg `0.0414` n `6`; index avg `0.1649` n `25`; metal avg `-0.5266` n `20`; unknown avg `0.1132` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2241`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1927`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1923`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1822`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1814`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1671`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
