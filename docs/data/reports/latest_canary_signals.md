# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T20:07:36.791315+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.017` n `12`; crypto_alt avg `-0.0332` n `230`; crypto_major avg `-0.0519` n `8`; equity avg `0.1483` n `98`; fx avg `0.0027` n `6`; index avg `-0.0122` n `25`; metal avg `-0.0039` n `20`; unknown avg `-0.0147` n `771`
- 1h: commodity avg `0.0313` n `12`; crypto_alt avg `-0.0719` n `230`; crypto_major avg `-0.0166` n `8`; equity avg `0.4663` n `98`; fx avg `0.0152` n `6`; index avg `0.0044` n `25`; metal avg `-0.0076` n `20`; unknown avg `-0.1142` n `771`
- 4h: commodity avg `0.0802` n `12`; crypto_alt avg `-0.1541` n `230`; crypto_major avg `-0.46` n `8`; equity avg `0.333` n `98`; fx avg `0.051` n `6`; index avg `0.0338` n `25`; metal avg `0.008` n `20`; unknown avg `-0.1313` n `771`
- 24h: commodity avg `0.496` n `12`; crypto_alt avg `0.9053` n `230`; crypto_major avg `0.8066` n `8`; equity avg `4.0419` n `98`; fx avg `0.0626` n `6`; index avg `0.629` n `25`; metal avg `0.7726` n `20`; unknown avg `0.3751` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0856`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0518`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0513`, n `668`, weak_sample_signal
