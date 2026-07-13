# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T18:22:26.433278+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1431` n `12`; crypto_alt avg `-0.2048` n `230`; crypto_major avg `-0.2035` n `8`; equity avg `-0.2136` n `92`; fx avg `-0.0045` n `6`; index avg `-0.0224` n `25`; metal avg `-0.0228` n `20`; unknown avg `-0.1063` n `766`
- 1h: commodity avg `0.4801` n `12`; crypto_alt avg `-0.691` n `230`; crypto_major avg `-0.6992` n `8`; equity avg `-0.3097` n `92`; fx avg `-0.0174` n `6`; index avg `-0.0702` n `25`; metal avg `-0.1009` n `20`; unknown avg `-0.1554` n `766`
- 4h: commodity avg `0.8281` n `12`; crypto_alt avg `-1.1555` n `230`; crypto_major avg `-0.9347` n `8`; equity avg `-0.654` n `92`; fx avg `-0.0274` n `6`; index avg `-0.1246` n `25`; metal avg `-0.2093` n `20`; unknown avg `-0.3367` n `766`
- 24h: commodity avg `0.7319` n `12`; crypto_alt avg `-2.4696` n `230`; crypto_major avg `-3.2721` n `8`; equity avg `-3.244` n `92`; fx avg `-0.0742` n `6`; index avg `-0.6486` n `25`; metal avg `-0.6146` n `20`; unknown avg `-0.2843` n `749`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1912`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1781`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
