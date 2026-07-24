# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T22:22:25.292400+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0291` n `12`; crypto_alt avg `-0.0446` n `230`; crypto_major avg `-0.0266` n `8`; equity avg `-0.0497` n `100`; fx avg `0.0012` n `6`; index avg `-0.0006` n `25`; metal avg `0.008` n `20`; unknown avg `-0.0107` n `774`
- 1h: commodity avg `-0.0476` n `12`; crypto_alt avg `-0.1873` n `230`; crypto_major avg `-0.0379` n `8`; equity avg `-0.0032` n `100`; fx avg `0.0094` n `6`; index avg `-0.0095` n `25`; metal avg `0.0141` n `20`; unknown avg `-0.0831` n `774`
- 4h: commodity avg `0.2591` n `12`; crypto_alt avg `-0.4255` n `230`; crypto_major avg `-0.3505` n `8`; equity avg `-0.4953` n `100`; fx avg `-0.0064` n `6`; index avg `-0.1049` n `25`; metal avg `-0.0361` n `20`; unknown avg `-0.0614` n `773`
- 24h: commodity avg `-0.2978` n `12`; crypto_alt avg `-1.2134` n `230`; crypto_major avg `-1.2411` n `8`; equity avg `-3.2083` n `100`; fx avg `-0.1597` n `6`; index avg `-0.4377` n `25`; metal avg `0.0133` n `20`; unknown avg `14.0398` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1517`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1266`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1218`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.112`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.11`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
