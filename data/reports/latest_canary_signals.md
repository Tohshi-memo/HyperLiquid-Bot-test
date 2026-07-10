# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T09:37:31.180007+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0396` n `12`; crypto_alt avg `0.2161` n `229`; crypto_major avg `0.2027` n `8`; equity avg `0.1287` n `91`; fx avg `0.0024` n `6`; index avg `0.001` n `25`; metal avg `-0.0048` n `20`; unknown avg `-0.0063` n `766`
- 1h: commodity avg `-0.0534` n `12`; crypto_alt avg `0.1338` n `229`; crypto_major avg `0.233` n `8`; equity avg `0.2434` n `91`; fx avg `-0.0039` n `6`; index avg `0.0644` n `25`; metal avg `0.0022` n `20`; unknown avg `-0.0458` n `765`
- 4h: commodity avg `-0.1913` n `12`; crypto_alt avg `0.2234` n `229`; crypto_major avg `0.4593` n `8`; equity avg `-0.3567` n `91`; fx avg `-0.0633` n `6`; index avg `-0.0602` n `25`; metal avg `-0.1211` n `20`; unknown avg `1.119` n `733`
- 24h: commodity avg `-0.897` n `12`; crypto_alt avg `1.1693` n `229`; crypto_major avg `1.7351` n `8`; equity avg `0.3596` n `91`; fx avg `-0.1275` n `6`; index avg `0.2327` n `25`; metal avg `0.0618` n `20`; unknown avg `0.1212` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
