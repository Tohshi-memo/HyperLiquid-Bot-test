# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T10:07:32.606004+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0371` n `12`; crypto_alt avg `-0.1377` n `230`; crypto_major avg `-0.0913` n `8`; equity avg `0.0198` n `100`; fx avg `0.0033` n `6`; index avg `-0.0023` n `25`; metal avg `-0.0102` n `20`; unknown avg `-0.0048` n `774`
- 1h: commodity avg `-0.0375` n `12`; crypto_alt avg `0.1654` n `230`; crypto_major avg `0.3279` n `8`; equity avg `0.0335` n `100`; fx avg `-0.016` n `6`; index avg `0.0189` n `25`; metal avg `0.0032` n `20`; unknown avg `0.0163` n `774`
- 4h: commodity avg `0.0273` n `12`; crypto_alt avg `-0.2116` n `230`; crypto_major avg `0.1194` n `8`; equity avg `-0.0818` n `100`; fx avg `0.0193` n `6`; index avg `0.0048` n `25`; metal avg `0.0081` n `20`; unknown avg `-0.1948` n `774`
- 24h: commodity avg `0.0243` n `12`; crypto_alt avg `-1.6296` n `230`; crypto_major avg `-1.2391` n `8`; equity avg `-3.047` n `100`; fx avg `-0.0112` n `6`; index avg `-0.2641` n `25`; metal avg `-0.1539` n `20`; unknown avg `13.1411` n `757`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1552`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1172`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1111`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1012`, n `666`, weak_sample_signal
