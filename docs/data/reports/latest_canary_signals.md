# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T21:37:29.791940+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0122` n `12`; crypto_alt avg `0.0854` n `230`; crypto_major avg `0.0642` n `8`; equity avg `0.0544` n `98`; fx avg `-0.003` n `6`; index avg `0.0116` n `25`; metal avg `0.0008` n `20`; unknown avg `0.4363` n `771`
- 1h: commodity avg `0.0596` n `12`; crypto_alt avg `0.1532` n `230`; crypto_major avg `0.0739` n `8`; equity avg `0.2668` n `98`; fx avg `-0.0343` n `6`; index avg `0.0396` n `25`; metal avg `-0.0138` n `20`; unknown avg `0.3691` n `771`
- 4h: commodity avg `0.1151` n `12`; crypto_alt avg `0.3025` n `230`; crypto_major avg `0.0311` n `8`; equity avg `0.5934` n `98`; fx avg `-0.0048` n `6`; index avg `0.0321` n `25`; metal avg `0.0565` n `20`; unknown avg `0.2638` n `771`
- 24h: commodity avg `0.5026` n `12`; crypto_alt avg `0.7398` n `230`; crypto_major avg `0.5391` n `8`; equity avg `4.4706` n `98`; fx avg `0.0452` n `6`; index avg `0.6761` n `25`; metal avg `0.7278` n `20`; unknown avg `0.2563` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0872`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0537`, n `668`, weak_sample_signal
