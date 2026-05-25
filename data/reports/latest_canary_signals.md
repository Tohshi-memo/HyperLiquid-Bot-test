# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T10:07:15.559367+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0411` n `12`; crypto_alt avg `0.0537` n `228`; crypto_major avg `-0.0015` n `8`; equity avg `-0.0035` n `67`; fx avg `0.0048` n `6`; index avg `-0.0089` n `23`; metal avg `0.089` n `18`; unknown avg `0.0058` n `397`
- 1h: commodity avg `-0.1065` n `12`; crypto_alt avg `0.0028` n `228`; crypto_major avg `-0.0478` n `8`; equity avg `0.1316` n `67`; fx avg `0.0056` n `6`; index avg `-0.0086` n `23`; metal avg `0.2316` n `18`; unknown avg `-0.0379` n `397`
- 4h: commodity avg `0.0889` n `12`; crypto_alt avg `0.1556` n `228`; crypto_major avg `0.1857` n `8`; equity avg `0.2277` n `67`; fx avg `0.0421` n `6`; index avg `0.0771` n `23`; metal avg `0.5107` n `18`; unknown avg `0.0259` n `397`
- 24h: commodity avg `-0.1019` n `12`; crypto_alt avg `0.3134` n `228`; crypto_major avg `-0.0408` n `8`; equity avg `0.6519` n `67`; fx avg `0.0024` n `6`; index avg `-0.0368` n `23`; metal avg `0.6462` n `18`; unknown avg `0.9222` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1341`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
