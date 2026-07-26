# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T20:02:19.350957+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0073` n `12`; crypto_alt avg `0.0242` n `230`; crypto_major avg `0.0221` n `8`; equity avg `-0.0247` n `100`; fx avg `-0.0081` n `6`; index avg `-0.006` n `25`; metal avg `-0.018` n `20`; unknown avg `-0.0009` n `775`
- 1h: commodity avg `0.0318` n `12`; crypto_alt avg `-0.0041` n `230`; crypto_major avg `0.0156` n `8`; equity avg `-0.0745` n `100`; fx avg `0.0167` n `6`; index avg `-0.0089` n `25`; metal avg `-0.0245` n `20`; unknown avg `-0.2306` n `775`
- 4h: commodity avg `0.1968` n `12`; crypto_alt avg `-0.1726` n `230`; crypto_major avg `-0.0552` n `8`; equity avg `-0.0243` n `100`; fx avg `0.0128` n `6`; index avg `-0.0272` n `25`; metal avg `0.0302` n `20`; unknown avg `-0.402` n `775`
- 24h: commodity avg `-0.2088` n `12`; crypto_alt avg `0.7782` n `230`; crypto_major avg `0.7541` n `8`; equity avg `0.6101` n `100`; fx avg `0.0434` n `6`; index avg `0.1065` n `25`; metal avg `0.1865` n `20`; unknown avg `-0.1103` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.192`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1822`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1641`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.148`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
