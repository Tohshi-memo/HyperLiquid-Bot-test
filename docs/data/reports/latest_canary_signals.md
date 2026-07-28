# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T21:37:37.863698+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0555` n `12`; crypto_alt avg `0.1195` n `230`; crypto_major avg `0.1711` n `8`; equity avg `0.0939` n `102`; fx avg `-0.0031` n `6`; index avg `0.0344` n `25`; metal avg `0.0158` n `20`; unknown avg `-0.0916` n `776`
- 1h: commodity avg `0.17` n `12`; crypto_alt avg `0.2192` n `230`; crypto_major avg `0.2266` n `8`; equity avg `0.1954` n `102`; fx avg `0.0135` n `6`; index avg `0.041` n `25`; metal avg `0.0176` n `20`; unknown avg `-0.0792` n `776`
- 4h: commodity avg `0.0932` n `12`; crypto_alt avg `0.4849` n `230`; crypto_major avg `0.7326` n `8`; equity avg `0.822` n `102`; fx avg `-0.0017` n `6`; index avg `-0.0018` n `25`; metal avg `-0.0505` n `20`; unknown avg `0.4075` n `774`
- 24h: commodity avg `-0.7463` n `12`; crypto_alt avg `-1.797` n `230`; crypto_major avg `-1.3069` n `8`; equity avg `-2.7074` n `102`; fx avg `-0.0764` n `6`; index avg `-0.3561` n `25`; metal avg `-0.4271` n `20`; unknown avg `0.4739` n `758`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
