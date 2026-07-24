# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T22:52:28.998295+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0071` n `12`; crypto_alt avg `0.0164` n `230`; crypto_major avg `0.0007` n `8`; equity avg `0.0295` n `100`; fx avg `-0.0029` n `6`; index avg `0.0012` n `25`; metal avg `0.0039` n `20`; unknown avg `-0.0186` n `774`
- 1h: commodity avg `-0.0899` n `12`; crypto_alt avg `0.1` n `230`; crypto_major avg `0.1791` n `8`; equity avg `0.0164` n `100`; fx avg `-0.0045` n `6`; index avg `-0.0093` n `25`; metal avg `0.0126` n `20`; unknown avg `-0.0057` n `774`
- 4h: commodity avg `0.2454` n `12`; crypto_alt avg `-0.2127` n `230`; crypto_major avg `-0.2531` n `8`; equity avg `-0.2486` n `100`; fx avg `-0.0112` n `6`; index avg `-0.0317` n `25`; metal avg `-0.0126` n `20`; unknown avg `-0.0889` n `773`
- 24h: commodity avg `-0.3073` n `12`; crypto_alt avg `-0.9629` n `230`; crypto_major avg `-1.0402` n `8`; equity avg `-3.2224` n `100`; fx avg `-0.1727` n `6`; index avg `-0.4734` n `25`; metal avg `-0.0069` n `20`; unknown avg `14.0335` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1507`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1264`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1222`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1125`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1099`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
