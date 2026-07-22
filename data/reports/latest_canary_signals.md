# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T16:07:32.617462+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.011` n `12`; crypto_alt avg `0.0355` n `230`; crypto_major avg `0.008` n `8`; equity avg `0.1021` n `98`; fx avg `0.0006` n `6`; index avg `0.0134` n `25`; metal avg `-0.0105` n `20`; unknown avg `-0.015` n `773`
- 1h: commodity avg `-0.1284` n `12`; crypto_alt avg `0.1103` n `230`; crypto_major avg `0.142` n `8`; equity avg `0.1153` n `98`; fx avg `0.0098` n `6`; index avg `0.0545` n `25`; metal avg `0.0412` n `20`; unknown avg `-0.0113` n `773`
- 4h: commodity avg `-0.1803` n `12`; crypto_alt avg `0.4806` n `230`; crypto_major avg `0.6255` n `8`; equity avg `1.5822` n `98`; fx avg `-0.022` n `6`; index avg `0.2986` n `25`; metal avg `0.1356` n `20`; unknown avg `9.454` n `773`
- 24h: commodity avg `0.3931` n `12`; crypto_alt avg `-0.2261` n `230`; crypto_major avg `-0.8594` n `8`; equity avg `0.2566` n `98`; fx avg `-0.0152` n `6`; index avg `-0.0131` n `25`; metal avg `0.4658` n `20`; unknown avg `1.0233` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1723`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1062`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0905`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0709`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0694`, n `666`, weak_sample_signal
