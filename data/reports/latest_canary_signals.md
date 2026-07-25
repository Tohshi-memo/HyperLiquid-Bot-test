# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T17:27:10.087404+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0089` n `12`; crypto_alt avg `0.1746` n `230`; crypto_major avg `0.1839` n `8`; equity avg `0.0869` n `100`; fx avg `-0.0042` n `6`; index avg `0.0067` n `25`; metal avg `0.0084` n `20`; unknown avg `-0.0504` n `774`
- 1h: commodity avg `-0.027` n `12`; crypto_alt avg `0.3568` n `230`; crypto_major avg `0.5033` n `8`; equity avg `0.1383` n `100`; fx avg `0.0007` n `6`; index avg `0.0146` n `25`; metal avg `0.0046` n `20`; unknown avg `-0.0475` n `774`
- 4h: commodity avg `-0.3811` n `12`; crypto_alt avg `0.6123` n `230`; crypto_major avg `0.9367` n `8`; equity avg `0.1514` n `100`; fx avg `-0.0069` n `6`; index avg `0.0248` n `25`; metal avg `0.0195` n `20`; unknown avg `-0.0254` n `774`
- 24h: commodity avg `-0.3004` n `12`; crypto_alt avg `0.3305` n `230`; crypto_major avg `1.071` n `8`; equity avg `-0.6767` n `100`; fx avg `-0.0026` n `6`; index avg `-0.0643` n `25`; metal avg `-0.1086` n `20`; unknown avg `-0.3473` n `757`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1648`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1647`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1286`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1174`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1122`, n `666`, weak_sample_signal
