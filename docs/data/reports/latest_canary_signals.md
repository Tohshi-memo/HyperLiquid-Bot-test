# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T00:07:28.557934+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0145` n `12`; crypto_alt avg `-0.0486` n `229`; crypto_major avg `-0.1192` n `8`; equity avg `-0.2637` n `91`; fx avg `0.0066` n `6`; index avg `-0.0921` n `25`; metal avg `-0.0358` n `20`; unknown avg `-0.056` n `765`
- 1h: commodity avg `0.0339` n `12`; crypto_alt avg `-0.2465` n `229`; crypto_major avg `-0.2346` n `8`; equity avg `-0.1353` n `91`; fx avg `0.0019` n `6`; index avg `-0.084` n `25`; metal avg `-0.0391` n `20`; unknown avg `-0.0647` n `765`
- 4h: commodity avg `0.049` n `12`; crypto_alt avg `-0.197` n `229`; crypto_major avg `-0.2109` n `8`; equity avg `-0.0837` n `91`; fx avg `0.0228` n `6`; index avg `-0.0817` n `25`; metal avg `0.0003` n `20`; unknown avg `-0.3433` n `765`
- 24h: commodity avg `-1.0608` n `12`; crypto_alt avg `0.597` n `229`; crypto_major avg `0.2739` n `8`; equity avg `1.1156` n `91`; fx avg `0.0596` n `6`; index avg `0.234` n `25`; metal avg `0.5587` n `20`; unknown avg `-0.1631` n `748`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
