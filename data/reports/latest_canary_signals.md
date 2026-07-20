# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T00:37:29.364179+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0073` n `12`; crypto_alt avg `0.1221` n `230`; crypto_major avg `0.0667` n `8`; equity avg `-0.0492` n `98`; fx avg `-0.0059` n `6`; index avg `-0.0101` n `25`; metal avg `-0.0173` n `20`; unknown avg `1.2078` n `769`
- 1h: commodity avg `-0.0279` n `12`; crypto_alt avg `0.5997` n `230`; crypto_major avg `0.336` n `8`; equity avg `0.6256` n `98`; fx avg `-0.0078` n `6`; index avg `0.1321` n `25`; metal avg `0.1491` n `20`; unknown avg `-0.0893` n `767`
- 4h: commodity avg `-0.0651` n `12`; crypto_alt avg `0.6229` n `230`; crypto_major avg `0.4688` n `8`; equity avg `0.7712` n `98`; fx avg `-0.053` n `6`; index avg `0.1977` n `25`; metal avg `0.0086` n `20`; unknown avg `0.0245` n `767`
- 24h: commodity avg `-0.1002` n `12`; crypto_alt avg `0.5163` n `230`; crypto_major avg `0.6642` n `8`; equity avg `1.1111` n `97`; fx avg `0.0342` n `6`; index avg `0.1964` n `25`; metal avg `0.0145` n `20`; unknown avg `0.1169` n `749`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1228`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1096`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1042`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0849`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
