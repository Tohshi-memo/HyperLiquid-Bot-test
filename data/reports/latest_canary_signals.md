# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T05:37:31.778554+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1177` n `12`; crypto_alt avg `0.1426` n `229`; crypto_major avg `0.1121` n `8`; equity avg `-0.176` n `91`; fx avg `0.0055` n `6`; index avg `-0.0372` n `25`; metal avg `0.1339` n `20`; unknown avg `0.2124` n `764`
- 1h: commodity avg `-0.1177` n `12`; crypto_alt avg `0.1426` n `229`; crypto_major avg `0.1121` n `8`; equity avg `-0.176` n `91`; fx avg `0.0055` n `6`; index avg `-0.0372` n `25`; metal avg `0.1339` n `20`; unknown avg `0.2124` n `764`
- 4h: commodity avg `-0.092` n `12`; crypto_alt avg `0.1518` n `229`; crypto_major avg `0.0769` n `8`; equity avg `-0.6831` n `91`; fx avg `-0.0304` n `6`; index avg `-0.1306` n `25`; metal avg `0.0727` n `20`; unknown avg `-0.574` n `764`
- 24h: commodity avg `0.1181` n `12`; crypto_alt avg `0.1132` n `229`; crypto_major avg `-0.2969` n `8`; equity avg `0.9494` n `91`; fx avg `0.0649` n `6`; index avg `0.0364` n `25`; metal avg `-0.9803` n `20`; unknown avg `0.016` n `739`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.0995`, n `671`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0906`, n `671`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0754`, n `671`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0724`, n `671`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0635`, n `671`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0614`, n `671`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0613`, n `671`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0596`, n `671`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0588`, n `671`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0552`, n `671`, weak_sample_signal
