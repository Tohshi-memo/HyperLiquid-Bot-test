# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T01:07:29.865749+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0169` n `12`; crypto_alt avg `0.1492` n `229`; crypto_major avg `0.2478` n `8`; equity avg `0.0889` n `91`; fx avg `-0.0248` n `6`; index avg `0.0251` n `25`; metal avg `-0.0801` n `20`; unknown avg `0.2297` n `764`
- 1h: commodity avg `-0.0269` n `12`; crypto_alt avg `-0.1414` n `229`; crypto_major avg `0.1842` n `8`; equity avg `0.1528` n `91`; fx avg `-0.0042` n `6`; index avg `0.0238` n `25`; metal avg `-0.1415` n `20`; unknown avg `0.1864` n `764`
- 4h: commodity avg `-0.1618` n `12`; crypto_alt avg `0.5742` n `229`; crypto_major avg `0.5663` n `8`; equity avg `0.7308` n `91`; fx avg `-0.0164` n `6`; index avg `0.0848` n `25`; metal avg `-0.049` n `20`; unknown avg `0.1937` n `764`
- 24h: commodity avg `0.3494` n `12`; crypto_alt avg `-1.5918` n `229`; crypto_major avg `-1.7892` n `8`; equity avg `1.0886` n `91`; fx avg `-0.0579` n `6`; index avg `-0.1172` n `25`; metal avg `-0.712` n `20`; unknown avg `-0.051` n `739`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.054`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0526`, n `668`, weak_sample_signal
