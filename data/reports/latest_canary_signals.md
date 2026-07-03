# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T11:07:28.760367+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0471` n `12`; crypto_alt avg `0.0986` n `229`; crypto_major avg `0.0171` n `8`; equity avg `-0.0374` n `88`; fx avg `0.005` n `6`; index avg `-0.0047` n `25`; metal avg `-0.0188` n `20`; unknown avg `0.0518` n `765`
- 1h: commodity avg `0.0321` n `12`; crypto_alt avg `0.6523` n `229`; crypto_major avg `0.8215` n `8`; equity avg `0.1631` n `88`; fx avg `0.0081` n `6`; index avg `0.0092` n `25`; metal avg `-0.0621` n `20`; unknown avg `0.7156` n `765`
- 4h: commodity avg `-0.0632` n `12`; crypto_alt avg `0.9751` n `229`; crypto_major avg `0.9861` n `8`; equity avg `0.2659` n `88`; fx avg `0.0473` n `6`; index avg `0.0081` n `25`; metal avg `-0.0615` n `20`; unknown avg `0.9516` n `755`
- 24h: commodity avg `0.4911` n `12`; crypto_alt avg `2.1766` n `229`; crypto_major avg `2.6674` n `8`; equity avg `0.2624` n `88`; fx avg `-0.0827` n `6`; index avg `0.2363` n `25`; metal avg `1.273` n `20`; unknown avg `5.8245` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
