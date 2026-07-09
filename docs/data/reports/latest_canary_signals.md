# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T19:22:27.935564+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0087` n `12`; crypto_alt avg `-0.0509` n `229`; crypto_major avg `-0.0925` n `8`; equity avg `-0.0048` n `91`; fx avg `-0.0057` n `6`; index avg `0.0011` n `25`; metal avg `-0.0093` n `20`; unknown avg `0.0203` n `765`
- 1h: commodity avg `-0.1419` n `12`; crypto_alt avg `-0.135` n `229`; crypto_major avg `-0.2672` n `8`; equity avg `-0.1136` n `91`; fx avg `-0.0163` n `6`; index avg `-0.0234` n `25`; metal avg `-0.192` n `20`; unknown avg `-0.0721` n `765`
- 4h: commodity avg `-0.2466` n `12`; crypto_alt avg `-0.0355` n `229`; crypto_major avg `-0.2469` n `8`; equity avg `-0.0611` n `91`; fx avg `-0.0076` n `6`; index avg `0.0617` n `25`; metal avg `-0.2948` n `20`; unknown avg `-0.1779` n `765`
- 24h: commodity avg `-1.0347` n `12`; crypto_alt avg `1.2046` n `229`; crypto_major avg `0.6455` n `8`; equity avg `2.2013` n `91`; fx avg `0.0427` n `6`; index avg `0.3642` n `25`; metal avg `0.5313` n `20`; unknown avg `-0.024` n `748`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
