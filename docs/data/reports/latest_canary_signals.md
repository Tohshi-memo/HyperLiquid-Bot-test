# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T01:37:25.222871+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0384` n `12`; crypto_alt avg `-0.2303` n `229`; crypto_major avg `-0.1955` n `8`; equity avg `-0.1673` n `91`; fx avg `-0.0264` n `6`; index avg `-0.0582` n `25`; metal avg `0.118` n `20`; unknown avg `-0.0878` n `763`
- 1h: commodity avg `-0.0352` n `12`; crypto_alt avg `-0.7017` n `229`; crypto_major avg `-0.5141` n `8`; equity avg `-0.4745` n `91`; fx avg `-0.0479` n `6`; index avg `-0.1215` n `25`; metal avg `-0.0963` n `20`; unknown avg `0.8704` n `763`
- 4h: commodity avg `0.0395` n `12`; crypto_alt avg `-1.018` n `229`; crypto_major avg `-0.741` n `8`; equity avg `-1.3545` n `91`; fx avg `-0.0203` n `6`; index avg `-0.3652` n `25`; metal avg `-0.2772` n `20`; unknown avg `1.1454` n `763`
- 24h: commodity avg `0.3437` n `12`; crypto_alt avg `-0.4243` n `229`; crypto_major avg `-1.001` n `8`; equity avg `-1.3658` n `90`; fx avg `0.0606` n `6`; index avg `-0.3172` n `25`; metal avg `-0.6011` n `20`; unknown avg `-0.562` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0524`, n `668`, weak_sample_signal
