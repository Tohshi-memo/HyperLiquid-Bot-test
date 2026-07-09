# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T21:52:30.128624+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0207` n `12`; crypto_alt avg `-0.0218` n `229`; crypto_major avg `-0.0146` n `8`; equity avg `0.0097` n `91`; fx avg `-0.0034` n `6`; index avg `-0.0012` n `25`; metal avg `0.005` n `20`; unknown avg `-0.1836` n `765`
- 1h: commodity avg `0.0578` n `12`; crypto_alt avg `-0.1031` n `229`; crypto_major avg `-0.0037` n `8`; equity avg `0.0143` n `91`; fx avg `0.0202` n `6`; index avg `0.011` n `25`; metal avg `0.0075` n `20`; unknown avg `-0.3473` n `765`
- 4h: commodity avg `0.1557` n `12`; crypto_alt avg `-0.0713` n `229`; crypto_major avg `0.0447` n `8`; equity avg `-0.4227` n `91`; fx avg `-0.0208` n `6`; index avg `-0.0249` n `25`; metal avg `-0.2936` n `20`; unknown avg `-0.4212` n `765`
- 24h: commodity avg `-1.1412` n `12`; crypto_alt avg `1.2769` n `229`; crypto_major avg `0.7617` n `8`; equity avg `1.581` n `91`; fx avg `0.0379` n `6`; index avg `0.3666` n `25`; metal avg `0.6825` n `20`; unknown avg `-0.1822` n `748`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
