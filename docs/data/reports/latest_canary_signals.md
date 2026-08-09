# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T04:03:06.099753+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0122` n `12`; crypto_alt avg `0.0359` n `230`; crypto_major avg `-0.0049` n `8`; equity avg `0.0073` n `112`; fx avg `0.0062` n `6`; index avg `-0.0008` n `25`; metal avg `-0.0024` n `20`; unknown avg `-0.0773` n `784`
- 1h: commodity avg `-0.0084` n `12`; crypto_alt avg `0.0918` n `230`; crypto_major avg `0.018` n `8`; equity avg `-0.0784` n `112`; fx avg `0.0004` n `6`; index avg `-0.0027` n `25`; metal avg `0.0038` n `20`; unknown avg `0.2215` n `784`
- 4h: commodity avg `0.069` n `12`; crypto_alt avg `0.0672` n `230`; crypto_major avg `-0.2508` n `8`; equity avg `-0.0202` n `112`; fx avg `0.0117` n `6`; index avg `-0.01` n `25`; metal avg `-0.0058` n `20`; unknown avg `-0.201` n `784`
- 24h: commodity avg `0.2084` n `12`; crypto_alt avg `1.4628` n `230`; crypto_major avg `0.4115` n `8`; equity avg `0.4778` n `112`; fx avg `0.0044` n `6`; index avg `0.0212` n `25`; metal avg `0.004` n `20`; unknown avg `-0.0006` n `751`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1678`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.054`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0527`, n `668`, weak_sample_signal
