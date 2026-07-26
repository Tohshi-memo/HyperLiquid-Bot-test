# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T08:37:24.149644+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0088` n `12`; crypto_alt avg `-0.0298` n `230`; crypto_major avg `0.0027` n `8`; equity avg `-0.0441` n `100`; fx avg `-0.0011` n `6`; index avg `0.0021` n `25`; metal avg `-0.0052` n `20`; unknown avg `0.0007` n `775`
- 1h: commodity avg `-0.0201` n `12`; crypto_alt avg `0.0008` n `230`; crypto_major avg `-0.0419` n `8`; equity avg `-0.0734` n `100`; fx avg `-0.0342` n `6`; index avg `0.0034` n `25`; metal avg `0.0172` n `20`; unknown avg `0.0327` n `775`
- 4h: commodity avg `-0.0615` n `12`; crypto_alt avg `0.4006` n `230`; crypto_major avg `-0.0576` n `8`; equity avg `-0.0923` n `100`; fx avg `-0.0401` n `6`; index avg `-0.0011` n `25`; metal avg `0.0255` n `20`; unknown avg `0.0174` n `759`
- 24h: commodity avg `-0.6189` n `12`; crypto_alt avg `1.7935` n `230`; crypto_major avg `1.7597` n `8`; equity avg `0.4863` n `100`; fx avg `0.0075` n `6`; index avg `0.141` n `25`; metal avg `0.0751` n `20`; unknown avg `0.0557` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1853`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1731`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1436`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1288`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1265`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1236`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1211`, n `666`, weak_sample_signal
