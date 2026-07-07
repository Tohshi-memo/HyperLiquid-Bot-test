# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T19:53:03.328180+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.058` n `12`; crypto_alt avg `0.0361` n `229`; crypto_major avg `0.0404` n `8`; equity avg `0.0394` n `91`; fx avg `-0.0014` n `6`; index avg `0.0104` n `25`; metal avg `0.0133` n `20`; unknown avg `0.0021` n `763`
- 1h: commodity avg `0.2128` n `12`; crypto_alt avg `-0.1884` n `229`; crypto_major avg `0.063` n `8`; equity avg `-0.1783` n `91`; fx avg `-0.0052` n `6`; index avg `-0.0588` n `25`; metal avg `-0.1647` n `20`; unknown avg `-0.0348` n `761`
- 4h: commodity avg `0.2792` n `12`; crypto_alt avg `-1.3032` n `229`; crypto_major avg `-0.853` n `8`; equity avg `-0.1392` n `91`; fx avg `-0.0343` n `6`; index avg `0.015` n `25`; metal avg `-0.2745` n `20`; unknown avg `0.1395` n `761`
- 24h: commodity avg `0.7928` n `12`; crypto_alt avg `-1.8925` n `229`; crypto_major avg `-1.0722` n `8`; equity avg `-3.4216` n `91`; fx avg `-0.2576` n `6`; index avg `-0.639` n `25`; metal avg `-0.5752` n `20`; unknown avg `-0.2895` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
