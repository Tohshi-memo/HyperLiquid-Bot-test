# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T03:07:39.295424+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.22` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0692` n `12`; crypto_alt avg `-0.0772` n `230`; crypto_major avg `-0.013` n `8`; equity avg `-0.0794` n `102`; fx avg `0.0015` n `6`; index avg `-0.0053` n `25`; metal avg `-0.0134` n `20`; unknown avg `0.08` n `777`
- 1h: commodity avg `-0.0596` n `12`; crypto_alt avg `-0.0633` n `230`; crypto_major avg `0.2193` n `8`; equity avg `-0.1435` n `102`; fx avg `-0.0097` n `6`; index avg `-0.1253` n `25`; metal avg `0.0743` n `20`; unknown avg `0.3702` n `777`
- 4h: commodity avg `-0.0952` n `12`; crypto_alt avg `-0.3332` n `230`; crypto_major avg `0.4496` n `8`; equity avg `-0.1184` n `102`; fx avg `-0.0054` n `6`; index avg `-0.2658` n `25`; metal avg `0.1065` n `20`; unknown avg `0.3599` n `776`
- 24h: commodity avg `0.0595` n `12`; crypto_alt avg `-0.7211` n `230`; crypto_major avg `0.6549` n `8`; equity avg `-1.9034` n `102`; fx avg `-0.1185` n `6`; index avg `-0.3609` n `25`; metal avg `-0.0412` n `20`; unknown avg `0.4694` n `758`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
