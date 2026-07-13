# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T23:22:24.402020+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0449` n `12`; crypto_alt avg `0.2781` n `230`; crypto_major avg `0.371` n `8`; equity avg `0.0556` n `92`; fx avg `0.0147` n `6`; index avg `-0.0018` n `25`; metal avg `-0.0139` n `20`; unknown avg `0.1498` n `766`
- 1h: commodity avg `0.2059` n `12`; crypto_alt avg `0.0168` n `230`; crypto_major avg `0.0403` n `8`; equity avg `-0.3883` n `92`; fx avg `-0.0139` n `6`; index avg `-0.0761` n `25`; metal avg `-0.0537` n `20`; unknown avg `0.0176` n `766`
- 4h: commodity avg `0.2818` n `12`; crypto_alt avg `-0.1892` n `230`; crypto_major avg `0.0778` n `8`; equity avg `-0.2066` n `92`; fx avg `-0.0142` n `6`; index avg `-0.0978` n `25`; metal avg `0.0269` n `20`; unknown avg `-0.2543` n `766`
- 24h: commodity avg `1.0775` n `12`; crypto_alt avg `-1.7981` n `230`; crypto_major avg `-2.2152` n `8`; equity avg `-3.2342` n `92`; fx avg `-0.0464` n `6`; index avg `-0.6479` n `25`; metal avg `-0.2971` n `20`; unknown avg `-0.3823` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.185`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1741`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
