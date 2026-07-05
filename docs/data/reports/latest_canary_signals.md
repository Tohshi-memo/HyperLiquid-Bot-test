# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T08:29:36.735047+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0224` n `12`; crypto_alt avg `-0.0531` n `229`; crypto_major avg `-0.0124` n `8`; equity avg `0.0206` n `88`; fx avg `-0.0007` n `6`; index avg `-0.0056` n `25`; metal avg `0.013` n `20`; unknown avg `-0.025` n `765`
- 1h: commodity avg `0.0324` n `12`; crypto_alt avg `0.2388` n `229`; crypto_major avg `0.1951` n `8`; equity avg `0.0285` n `88`; fx avg `-0.0022` n `6`; index avg `-0.0059` n `25`; metal avg `0.0133` n `20`; unknown avg `0.0211` n `765`
- 4h: commodity avg `0.0203` n `12`; crypto_alt avg `0.0013` n `229`; crypto_major avg `-0.0267` n `8`; equity avg `0.0433` n `88`; fx avg `0.0093` n `6`; index avg `0.0292` n `25`; metal avg `0.0068` n `20`; unknown avg `-0.0931` n `731`
- 24h: commodity avg `0.0889` n `12`; crypto_alt avg `-0.3603` n `229`; crypto_major avg `-0.7292` n `8`; equity avg `0.2156` n `88`; fx avg `0.0176` n `6`; index avg `0.051` n `25`; metal avg `0.0714` n `20`; unknown avg `-1.28` n `725`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
