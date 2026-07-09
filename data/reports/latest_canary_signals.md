# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T16:22:35.185809+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.038` n `12`; crypto_alt avg `-0.2145` n `229`; crypto_major avg `-0.2265` n `8`; equity avg `-0.1639` n `91`; fx avg `-0.0048` n `6`; index avg `-0.0031` n `25`; metal avg `0.0523` n `20`; unknown avg `-0.0372` n `765`
- 1h: commodity avg `-0.1194` n `12`; crypto_alt avg `-0.5148` n `229`; crypto_major avg `-0.5758` n `8`; equity avg `-0.0547` n `91`; fx avg `0.0169` n `6`; index avg `0.0228` n `25`; metal avg `0.0449` n `20`; unknown avg `-0.0039` n `765`
- 4h: commodity avg `-0.9303` n `12`; crypto_alt avg `-0.2823` n `229`; crypto_major avg `-0.184` n `8`; equity avg `0.7401` n `91`; fx avg `-0.0361` n `6`; index avg `0.1948` n `25`; metal avg `0.3112` n `20`; unknown avg `0.1708` n `765`
- 24h: commodity avg `-1.292` n `12`; crypto_alt avg `1.1051` n `229`; crypto_major avg `0.6098` n `8`; equity avg `2.9434` n `91`; fx avg `0.0477` n `6`; index avg `0.4551` n `25`; metal avg `1.3457` n `20`; unknown avg `1.2676` n `748`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
