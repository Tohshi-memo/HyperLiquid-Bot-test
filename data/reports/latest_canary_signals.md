# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T08:18:49.806765+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0022` n `12`; crypto_alt avg `-0.0128` n `230`; crypto_major avg `0.006` n `8`; equity avg `0.0154` n `114`; fx avg `-0.0058` n `6`; index avg `0.004` n `25`; metal avg `-0.0004` n `20`; unknown avg `-0.0759` n `791`
- 1h: commodity avg `0.0376` n `12`; crypto_alt avg `0.1423` n `230`; crypto_major avg `0.0694` n `8`; equity avg `0.0119` n `114`; fx avg `-0.0016` n `6`; index avg `0.0018` n `25`; metal avg `-0.0016` n `20`; unknown avg `-0.0713` n `791`
- 4h: commodity avg `-0.0342` n `12`; crypto_alt avg `0.3548` n `230`; crypto_major avg `0.023` n `8`; equity avg `0.1027` n `114`; fx avg `0.0006` n `6`; index avg `0.0252` n `25`; metal avg `0.0101` n `20`; unknown avg `-0.0256` n `759`
- 24h: commodity avg `0.1165` n `12`; crypto_alt avg `0.0657` n `230`; crypto_major avg `0.1058` n `8`; equity avg `0.3923` n `114`; fx avg `-0.019` n `6`; index avg `0.0582` n `25`; metal avg `0.016` n `20`; unknown avg `-0.0374` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2095`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1798`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1753`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1747`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1513`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.144`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1423`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1422`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
