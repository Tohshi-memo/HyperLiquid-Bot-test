# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T21:43:14.052439+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0206` n `12`; crypto_alt avg `0.0314` n `230`; crypto_major avg `-0.0125` n `8`; equity avg `0.0489` n `98`; fx avg `-0.0087` n `6`; index avg `0.012` n `25`; metal avg `0.0034` n `20`; unknown avg `0.0406` n `771`
- 1h: commodity avg `0.0511` n `12`; crypto_alt avg `0.0991` n `230`; crypto_major avg `-0.0029` n `8`; equity avg `0.2614` n `98`; fx avg `-0.0401` n `6`; index avg `0.04` n `25`; metal avg `-0.0112` n `20`; unknown avg `0.039` n `771`
- 4h: commodity avg `0.1066` n `12`; crypto_alt avg `0.2482` n `230`; crypto_major avg `-0.0456` n `8`; equity avg `0.5879` n `98`; fx avg `-0.0106` n `6`; index avg `0.0325` n `25`; metal avg `0.0591` n `20`; unknown avg `-0.0388` n `771`
- 24h: commodity avg `0.4941` n `12`; crypto_alt avg `0.686` n `230`; crypto_major avg `0.4631` n `8`; equity avg `4.4634` n `98`; fx avg `0.0395` n `6`; index avg `0.6764` n `25`; metal avg `0.7305` n `20`; unknown avg `0.2532` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0874`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0543`, n `668`, weak_sample_signal
