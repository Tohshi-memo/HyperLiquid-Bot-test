# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T09:37:29.325843+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0121` n `12`; crypto_alt avg `-0.1199` n `231`; crypto_major avg `-0.1143` n `8`; equity avg `0.0062` n `128`; fx avg `-0.0006` n `6`; index avg `0.0175` n `26`; metal avg `-0.0003` n `20`; unknown avg `0.052` n `793`
- 1h: commodity avg `-0.0123` n `12`; crypto_alt avg `-0.0244` n `231`; crypto_major avg `-0.1401` n `8`; equity avg `-0.0051` n `128`; fx avg `-0.0012` n `6`; index avg `0.012` n `26`; metal avg `-0.0079` n `20`; unknown avg `-0.0866` n `793`
- 4h: commodity avg `-0.0133` n `12`; crypto_alt avg `-0.1232` n `231`; crypto_major avg `-0.1672` n `8`; equity avg `0.0095` n `128`; fx avg `0.005` n `6`; index avg `-0.0165` n `26`; metal avg `0.0029` n `20`; unknown avg `-0.0362` n `759`
- 24h: commodity avg `-0.0176` n `12`; crypto_alt avg `0.8783` n `231`; crypto_major avg `0.7165` n `8`; equity avg `0.28` n `128`; fx avg `-0.0021` n `6`; index avg `0.0709` n `26`; metal avg `0.0725` n `20`; unknown avg `0.8045` n `716`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1458`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
