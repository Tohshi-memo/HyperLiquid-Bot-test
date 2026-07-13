# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T17:52:37.194850+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0907` n `12`; crypto_alt avg `-0.0959` n `230`; crypto_major avg `-0.0829` n `8`; equity avg `-0.1596` n `92`; fx avg `0.0041` n `6`; index avg `-0.0423` n `25`; metal avg `-0.0415` n `20`; unknown avg `-0.0148` n `766`
- 1h: commodity avg `0.2732` n `12`; crypto_alt avg `-0.6106` n `230`; crypto_major avg `-0.426` n `8`; equity avg `-0.3979` n `92`; fx avg `-0.0074` n `6`; index avg `-0.0383` n `25`; metal avg `-0.0333` n `20`; unknown avg `-0.14` n `766`
- 4h: commodity avg `0.7781` n `12`; crypto_alt avg `-0.7088` n `230`; crypto_major avg `-0.3643` n `8`; equity avg `-0.5817` n `92`; fx avg `-0.0295` n `6`; index avg `-0.1041` n `25`; metal avg `-0.3797` n `20`; unknown avg `-0.1588` n `766`
- 24h: commodity avg `0.5162` n `12`; crypto_alt avg `-2.334` n `230`; crypto_major avg `-3.1793` n `8`; equity avg `-3.3088` n `92`; fx avg `-0.1846` n `6`; index avg `-0.636` n `25`; metal avg `-0.599` n `20`; unknown avg `-0.2127` n `749`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1954`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.182`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
