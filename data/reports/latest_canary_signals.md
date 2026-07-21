# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T03:37:29.315857+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0136` n `12`; crypto_alt avg `0.0077` n `230`; crypto_major avg `0.042` n `8`; equity avg `0.3065` n `98`; fx avg `-0.0021` n `6`; index avg `0.0341` n `25`; metal avg `0.0259` n `20`; unknown avg `-0.0551` n `771`
- 1h: commodity avg `-0.0297` n `12`; crypto_alt avg `0.4256` n `230`; crypto_major avg `0.3668` n `8`; equity avg `0.905` n `98`; fx avg `-0.034` n `6`; index avg `0.0984` n `25`; metal avg `0.0674` n `20`; unknown avg `0.3056` n `771`
- 4h: commodity avg `-0.0554` n `12`; crypto_alt avg `0.548` n `230`; crypto_major avg `0.5823` n `8`; equity avg `1.1675` n `98`; fx avg `0.0216` n `6`; index avg `0.2329` n `25`; metal avg `0.3357` n `20`; unknown avg `0.415` n `770`
- 24h: commodity avg `-0.3479` n `12`; crypto_alt avg `1.8205` n `230`; crypto_major avg `1.5646` n `8`; equity avg `1.0122` n `98`; fx avg `-0.1234` n `6`; index avg `0.2537` n `25`; metal avg `0.2397` n `20`; unknown avg `0.0253` n `747`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0924`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0921`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.089`, n `666`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0823`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0801`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0775`, n `666`, weak_sample_signal
