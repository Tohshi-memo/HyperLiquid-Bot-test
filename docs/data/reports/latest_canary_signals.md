# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T08:07:38.712863+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0086` n `12`; crypto_alt avg `0.0229` n `230`; crypto_major avg `-0.0076` n `8`; equity avg `0.0037` n `102`; fx avg `-0.0242` n `6`; index avg `-0.0141` n `25`; metal avg `-0.0411` n `20`; unknown avg `-0.0142` n `779`
- 1h: commodity avg `-0.0754` n `12`; crypto_alt avg `0.3721` n `230`; crypto_major avg `-0.1922` n `8`; equity avg `0.3243` n `102`; fx avg `-0.0187` n `6`; index avg `0.0429` n `25`; metal avg `-0.01` n `20`; unknown avg `-0.0134` n `779`
- 4h: commodity avg `-0.0263` n `12`; crypto_alt avg `0.225` n `230`; crypto_major avg `-0.2606` n `8`; equity avg `0.3191` n `102`; fx avg `-0.1127` n `6`; index avg `0.0938` n `25`; metal avg `-0.0264` n `20`; unknown avg `-0.037` n `747`
- 24h: commodity avg `-0.3544` n `12`; crypto_alt avg `0.3824` n `230`; crypto_major avg `0.6287` n `8`; equity avg `8.8838` n `102`; fx avg `-0.1977` n `6`; index avg `1.3402` n `25`; metal avg `0.4604` n `20`; unknown avg `0.0419` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
