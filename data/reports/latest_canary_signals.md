# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T22:39:56.879643+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0183` n `12`; crypto_alt avg `0.2545` n `230`; crypto_major avg `0.1919` n `8`; equity avg `0.0383` n `100`; fx avg `-0.0014` n `6`; index avg `0.0043` n `25`; metal avg `0.0023` n `20`; unknown avg `0.1409` n `774`
- 1h: commodity avg `-0.0792` n `12`; crypto_alt avg `-0.0702` n `230`; crypto_major avg `0.0341` n `8`; equity avg `-0.0449` n `100`; fx avg `0.0103` n `6`; index avg `-0.0166` n `25`; metal avg `0.0089` n `20`; unknown avg `-0.0674` n `774`
- 4h: commodity avg `0.2799` n `12`; crypto_alt avg `-0.0295` n `230`; crypto_major avg `-0.0051` n `8`; equity avg `-0.1363` n `100`; fx avg `-0.0087` n `6`; index avg `-0.0269` n `25`; metal avg `-0.0177` n `20`; unknown avg `-0.1564` n `773`
- 24h: commodity avg `-0.2954` n `12`; crypto_alt avg `-1.0129` n `230`; crypto_major avg `-1.1071` n `8`; equity avg `-3.1995` n `100`; fx avg `-0.1626` n `6`; index avg `-0.4282` n `25`; metal avg `-0.0069` n `20`; unknown avg `14.0232` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1512`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1266`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1221`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1124`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.11`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
