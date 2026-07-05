# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T23:22:26.358505+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0215` n `12`; crypto_alt avg `0.0957` n `229`; crypto_major avg `0.1476` n `8`; equity avg `0.0038` n `88`; fx avg `0.0088` n `6`; index avg `0.0126` n `25`; metal avg `0.0062` n `20`; unknown avg `-0.1325` n `765`
- 1h: commodity avg `-0.0639` n `12`; crypto_alt avg `0.0241` n `229`; crypto_major avg `0.0787` n `8`; equity avg `0.099` n `88`; fx avg `0.0056` n `6`; index avg `0.0487` n `25`; metal avg `0.1307` n `20`; unknown avg `0.1919` n `765`
- 4h: commodity avg `-0.1755` n `12`; crypto_alt avg `0.7637` n `229`; crypto_major avg `1.303` n `8`; equity avg `0.2463` n `88`; fx avg `0.1105` n `6`; index avg `0.0292` n `25`; metal avg `0.1818` n `20`; unknown avg `1.7453` n `765`
- 24h: commodity avg `-0.1848` n `12`; crypto_alt avg `0.3552` n `229`; crypto_major avg `1.1362` n `8`; equity avg `0.536` n `88`; fx avg `0.0235` n `6`; index avg `0.0973` n `25`; metal avg `0.1907` n `20`; unknown avg `1.3266` n `663`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0537`, n `668`, weak_sample_signal
