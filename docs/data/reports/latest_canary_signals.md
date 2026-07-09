# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T18:07:34.421560+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0382` n `12`; crypto_alt avg `0.2729` n `229`; crypto_major avg `0.3674` n `8`; equity avg `0.0169` n `91`; fx avg `0.0008` n `6`; index avg `0.01` n `25`; metal avg `-0.051` n `20`; unknown avg `0.086` n `765`
- 1h: commodity avg `-0.0897` n `12`; crypto_alt avg `0.6503` n `229`; crypto_major avg `0.6511` n `8`; equity avg `0.2308` n `91`; fx avg `0.0014` n `6`; index avg `0.0582` n `25`; metal avg `0.0328` n `20`; unknown avg `0.2369` n `765`
- 4h: commodity avg `-0.5722` n `12`; crypto_alt avg `0.2051` n `229`; crypto_major avg `0.4143` n `8`; equity avg `0.1065` n `91`; fx avg `-0.0118` n `6`; index avg `0.0734` n `25`; metal avg `-0.0213` n `20`; unknown avg `-0.1138` n `765`
- 24h: commodity avg `-1.0321` n `12`; crypto_alt avg `1.4973` n `229`; crypto_major avg `1.0441` n `8`; equity avg `2.6553` n `91`; fx avg `0.0375` n `6`; index avg `0.4242` n `25`; metal avg `0.9537` n `20`; unknown avg `1.0052` n `748`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
