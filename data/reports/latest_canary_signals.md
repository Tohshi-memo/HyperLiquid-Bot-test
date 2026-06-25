# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T09:22:31.243688+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0411` n `12`; crypto_alt avg `-0.3544` n `228`; crypto_major avg `-0.2068` n `8`; equity avg `-0.0759` n `86`; fx avg `0.0105` n `6`; index avg `-0.0292` n `23`; metal avg `0.0039` n `20`; unknown avg `-0.1957` n `765`
- 1h: commodity avg `-0.0335` n `12`; crypto_alt avg `-0.523` n `228`; crypto_major avg `-0.286` n `8`; equity avg `-0.1233` n `86`; fx avg `0.0415` n `6`; index avg `-0.0263` n `23`; metal avg `0.0112` n `20`; unknown avg `-0.0731` n `765`
- 4h: commodity avg `0.1612` n `12`; crypto_alt avg `-0.4823` n `228`; crypto_major avg `-0.083` n `8`; equity avg `-0.0332` n `86`; fx avg `-0.0048` n `6`; index avg `-0.0304` n `23`; metal avg `0.1328` n `20`; unknown avg `0.0292` n `733`
- 24h: commodity avg `-0.1905` n `12`; crypto_alt avg `-1.4101` n `228`; crypto_major avg `-0.9053` n `8`; equity avg `-0.0523` n `86`; fx avg `-0.0292` n `6`; index avg `0.4887` n `23`; metal avg `-1.3248` n `20`; unknown avg `-0.6777` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0577`, n `668`, weak_sample_signal
