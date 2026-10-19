# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T06:07:36.062960+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0446` n `13`; crypto_alt avg `0.1156` n `237`; crypto_major avg `0.1198` n `8`; equity avg `0.25` n `151`; fx avg `0.0221` n `6`; index avg `0.0476` n `26`; metal avg `-0.005` n `20`; unknown avg `2.3637` n `1172`
- 1h: commodity avg `-0.0499` n `13`; crypto_alt avg `0.3791` n `237`; crypto_major avg `0.2161` n `8`; equity avg `0.2403` n `151`; fx avg `-0.0145` n `6`; index avg `0.0359` n `26`; metal avg `0.0281` n `20`; unknown avg `0.03` n `1172`
- 4h: commodity avg `-0.0911` n `13`; crypto_alt avg `-0.0854` n `237`; crypto_major avg `0.263` n `8`; equity avg `0.7` n `151`; fx avg `-0.0287` n `6`; index avg `0.122` n `26`; metal avg `0.0532` n `20`; unknown avg `5.9866` n `1164`
- 24h: commodity avg `-0.4707` n `13`; crypto_alt avg `0.4931` n `237`; crypto_major avg `1.2141` n `8`; equity avg `2.9547` n `151`; fx avg `-0.0337` n `6`; index avg `0.55` n `26`; metal avg `0.3482` n `20`; unknown avg `3.7894` n `901`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1968`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1427`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1208`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1004`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0708`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.067`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0627`, n `666`, weak_sample_signal
