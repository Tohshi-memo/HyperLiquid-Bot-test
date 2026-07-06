# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T21:37:38.144419+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0046` n `12`; crypto_alt avg `-0.0739` n `229`; crypto_major avg `-0.3282` n `8`; equity avg `0.0358` n `91`; fx avg `0.0048` n `6`; index avg `0.0005` n `25`; metal avg `-0.0021` n `20`; unknown avg `1.2284` n `763`
- 1h: commodity avg `0.0054` n `12`; crypto_alt avg `0.523` n `229`; crypto_major avg `0.4519` n `8`; equity avg `0.0336` n `91`; fx avg `-0.004` n `6`; index avg `0.0195` n `25`; metal avg `0.0265` n `20`; unknown avg `0.0707` n `763`
- 4h: commodity avg `0.1001` n `12`; crypto_alt avg `0.5538` n `229`; crypto_major avg `0.6016` n `8`; equity avg `-0.064` n `91`; fx avg `-0.0106` n `6`; index avg `0.0493` n `25`; metal avg `0.0596` n `20`; unknown avg `-0.2482` n `763`
- 24h: commodity avg `0.0402` n `12`; crypto_alt avg `0.9858` n `229`; crypto_major avg `0.7193` n `8`; equity avg `-0.6306` n `90`; fx avg `0.1901` n `6`; index avg `0.0464` n `25`; metal avg `-0.1729` n `20`; unknown avg `0.1569` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
