# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T12:07:29.310922+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0035` n `12`; crypto_alt avg `-0.0729` n `229`; crypto_major avg `-0.101` n `8`; equity avg `-0.0028` n `88`; fx avg `0.0` n `6`; index avg `0.0064` n `25`; metal avg `-0.0132` n `20`; unknown avg `0.0182` n `765`
- 1h: commodity avg `-0.0215` n `12`; crypto_alt avg `-0.1369` n `229`; crypto_major avg `-0.0017` n `8`; equity avg `-0.0222` n `88`; fx avg `0.0044` n `6`; index avg `0.0156` n `25`; metal avg `0.0009` n `20`; unknown avg `0.0123` n `765`
- 4h: commodity avg `-0.005` n `12`; crypto_alt avg `-0.6037` n `229`; crypto_major avg `-0.2249` n `8`; equity avg `0.0371` n `88`; fx avg `0.0027` n `6`; index avg `0.0033` n `25`; metal avg `0.036` n `20`; unknown avg `-0.0842` n `765`
- 24h: commodity avg `-0.0296` n `12`; crypto_alt avg `-1.4713` n `229`; crypto_major avg `-0.7651` n `8`; equity avg `0.2743` n `88`; fx avg `0.0066` n `6`; index avg `0.0556` n `25`; metal avg `0.0831` n `20`; unknown avg `-1.1944` n `725`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
