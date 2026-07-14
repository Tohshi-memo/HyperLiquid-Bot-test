# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T10:54:41.055695+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.138` n `12`; crypto_alt avg `0.1428` n `230`; crypto_major avg `0.2701` n `8`; equity avg `-0.0585` n `92`; fx avg `-0.0018` n `6`; index avg `-0.0128` n `25`; metal avg `-0.0195` n `20`; unknown avg `0.0184` n `766`
- 1h: commodity avg `0.0668` n `12`; crypto_alt avg `0.1545` n `230`; crypto_major avg `0.3887` n `8`; equity avg `0.0066` n `92`; fx avg `0.0038` n `6`; index avg `0.0122` n `25`; metal avg `-0.1032` n `20`; unknown avg `0.0034` n `766`
- 4h: commodity avg `0.2093` n `12`; crypto_alt avg `-0.1533` n `230`; crypto_major avg `0.2256` n `8`; equity avg `0.2744` n `92`; fx avg `0.0436` n `6`; index avg `0.0307` n `25`; metal avg `-0.139` n `20`; unknown avg `-0.1163` n `766`
- 24h: commodity avg `1.462` n `12`; crypto_alt avg `-0.9078` n `230`; crypto_major avg `-0.2701` n `8`; equity avg `-0.4835` n `92`; fx avg `-0.0197` n `6`; index avg `-0.0697` n `25`; metal avg `-0.1381` n `20`; unknown avg `-0.2854` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1801`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1646`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
