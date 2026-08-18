# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T04:37:22.913730+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0075` n `12`; crypto_alt avg `0.1732` n `230`; crypto_major avg `0.1386` n `8`; equity avg `0.1548` n `114`; fx avg `0.0148` n `6`; index avg `0.0188` n `25`; metal avg `0.0068` n `20`; unknown avg `0.0052` n `793`
- 1h: commodity avg `0.0329` n `12`; crypto_alt avg `0.2773` n `230`; crypto_major avg `0.2259` n `8`; equity avg `0.3838` n `114`; fx avg `0.0293` n `6`; index avg `0.0409` n `25`; metal avg `-0.0273` n `20`; unknown avg `0.0531` n `793`
- 4h: commodity avg `0.0759` n `12`; crypto_alt avg `-0.8525` n `230`; crypto_major avg `-0.3847` n `8`; equity avg `-1.6197` n `114`; fx avg `0.0065` n `6`; index avg `-0.2906` n `25`; metal avg `-0.3556` n `20`; unknown avg `0.1976` n `793`
- 24h: commodity avg `0.6369` n `12`; crypto_alt avg `-1.363` n `230`; crypto_major avg `0.0958` n `8`; equity avg `-0.9429` n `114`; fx avg `0.0149` n `6`; index avg `-0.2744` n `25`; metal avg `-0.1863` n `20`; unknown avg `0.0157` n `776`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.2094`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1978`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1614`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
