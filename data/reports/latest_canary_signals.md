# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T22:27:37.687938+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0213` n `12`; crypto_alt avg `0.0669` n `229`; crypto_major avg `0.0823` n `8`; equity avg `0.0069` n `91`; fx avg `-0.0028` n `6`; index avg `0.0008` n `25`; metal avg `-0.0081` n `20`; unknown avg `0.0983` n `765`
- 1h: commodity avg `-0.0681` n `12`; crypto_alt avg `-0.0746` n `229`; crypto_major avg `-0.0509` n `8`; equity avg `0.0302` n `91`; fx avg `-0.0095` n `6`; index avg `0.0041` n `25`; metal avg `0.0072` n `20`; unknown avg `-0.3353` n `765`
- 4h: commodity avg `-0.1079` n `12`; crypto_alt avg `-0.1647` n `229`; crypto_major avg `-0.043` n `8`; equity avg `-0.273` n `91`; fx avg `-0.0108` n `6`; index avg `-0.0189` n `25`; metal avg `-0.1827` n `20`; unknown avg `-0.4528` n `765`
- 24h: commodity avg `-1.1855` n `12`; crypto_alt avg `1.1549` n `229`; crypto_major avg `0.7773` n `8`; equity avg `1.5979` n `91`; fx avg `0.0109` n `6`; index avg `0.3648` n `25`; metal avg `0.651` n `20`; unknown avg `-0.2144` n `748`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
