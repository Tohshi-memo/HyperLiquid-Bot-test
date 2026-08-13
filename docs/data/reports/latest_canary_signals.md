# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T22:07:28.471940+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0264` n `12`; crypto_alt avg `0.061` n `230`; crypto_major avg `0.1276` n `8`; equity avg `0.0435` n `113`; fx avg `-0.0061` n `6`; index avg `0.0171` n `25`; metal avg `-0.0161` n `20`; unknown avg `0.0284` n `787`
- 1h: commodity avg `-0.005` n `12`; crypto_alt avg `0.2562` n `230`; crypto_major avg `0.0011` n `8`; equity avg `0.1716` n `113`; fx avg `0.0014` n `6`; index avg `0.0144` n `25`; metal avg `-0.0118` n `20`; unknown avg `0.1085` n `787`
- 4h: commodity avg `-0.0361` n `12`; crypto_alt avg `0.3282` n `230`; crypto_major avg `0.3208` n `8`; equity avg `0.1905` n `113`; fx avg `0.0052` n `6`; index avg `0.028` n `25`; metal avg `-0.0844` n `20`; unknown avg `0.2269` n `787`
- 24h: commodity avg `-0.4532` n `12`; crypto_alt avg `0.8337` n `230`; crypto_major avg `0.7569` n `8`; equity avg `1.7617` n `113`; fx avg `0.0224` n `6`; index avg `0.3251` n `25`; metal avg `-0.4461` n `20`; unknown avg `0.217` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2407`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2041`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1959`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1852`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1691`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.163`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1529`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1501`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1492`, n `668`, weak_sample_signal
