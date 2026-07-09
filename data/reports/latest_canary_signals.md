# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T07:17:29.716303+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0266` n `12`; crypto_alt avg `-0.1314` n `229`; crypto_major avg `-0.0502` n `8`; equity avg `0.1019` n `91`; fx avg `-0.0024` n `6`; index avg `0.0276` n `25`; metal avg `0.0113` n `20`; unknown avg `-0.0655` n `764`
- 1h: commodity avg `0.1103` n `12`; crypto_alt avg `0.1038` n `229`; crypto_major avg `0.0812` n `8`; equity avg `0.2832` n `91`; fx avg `0.0451` n `6`; index avg `0.0543` n `25`; metal avg `0.0862` n `20`; unknown avg `0.0136` n `764`
- 4h: commodity avg `-0.1544` n `12`; crypto_alt avg `1.1971` n `229`; crypto_major avg `1.1732` n `8`; equity avg `0.9893` n `91`; fx avg `0.0703` n `6`; index avg `0.2178` n `25`; metal avg `0.6019` n `20`; unknown avg `0.0831` n `748`
- 24h: commodity avg `0.1309` n `12`; crypto_alt avg `0.7591` n `229`; crypto_major avg `0.4966` n `8`; equity avg `1.9221` n `91`; fx avg `0.1716` n `6`; index avg `0.2327` n `25`; metal avg `-0.4074` n `20`; unknown avg `0.371` n `741`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.102`, n `669`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.101`, n `669`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0731`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0667`, n `669`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0653`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0651`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0634`, n `669`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.059`, n `669`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0587`, n `669`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0556`, n `669`, weak_sample_signal
