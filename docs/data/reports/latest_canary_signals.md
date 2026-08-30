# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T09:07:24.570303+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0101` n `12`; crypto_alt avg `0.072` n `231`; crypto_major avg `0.0934` n `8`; equity avg `0.0144` n `128`; fx avg `0.0041` n `6`; index avg `-0.0065` n `26`; metal avg `0.0019` n `20`; unknown avg `0.0124` n `793`
- 1h: commodity avg `0.01` n `12`; crypto_alt avg `-0.0134` n `231`; crypto_major avg `0.0027` n `8`; equity avg `0.0173` n `128`; fx avg `0.003` n `6`; index avg `-0.006` n `26`; metal avg `-0.0048` n `20`; unknown avg `-0.038` n `793`
- 4h: commodity avg `-0.0026` n `12`; crypto_alt avg `0.044` n `231`; crypto_major avg `-0.0782` n `8`; equity avg `0.0114` n `128`; fx avg `0.0092` n `6`; index avg `-0.0137` n `26`; metal avg `0.0107` n `20`; unknown avg `-0.0599` n `759`
- 24h: commodity avg `-0.0158` n `12`; crypto_alt avg `1.1022` n `231`; crypto_major avg `0.9851` n `8`; equity avg `0.2849` n `128`; fx avg `0.0` n `6`; index avg `0.05` n `26`; metal avg `0.0903` n `20`; unknown avg `0.713` n `714`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1511`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
