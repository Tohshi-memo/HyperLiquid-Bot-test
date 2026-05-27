# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T00:07:20.501711+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1016` n `12`; crypto_alt avg `0.2221` n `228`; crypto_major avg `0.2373` n `8`; equity avg `0.0669` n `67`; fx avg `-0.0066` n `6`; index avg `0.0492` n `23`; metal avg `0.0149` n `18`; unknown avg `-0.094` n `418`
- 1h: commodity avg `-0.0291` n `12`; crypto_alt avg `0.0299` n `228`; crypto_major avg `0.1134` n `8`; equity avg `0.2097` n `67`; fx avg `0.0117` n `6`; index avg `0.1867` n `23`; metal avg `0.2053` n `18`; unknown avg `-0.2321` n `418`
- 4h: commodity avg `-0.0184` n `12`; crypto_alt avg `-0.1929` n `228`; crypto_major avg `-0.0999` n `8`; equity avg `0.3408` n `67`; fx avg `0.017` n `6`; index avg `0.2496` n `23`; metal avg `0.3789` n `18`; unknown avg `-0.5954` n `418`
- 24h: commodity avg `0.4917` n `12`; crypto_alt avg `-1.2844` n `228`; crypto_major avg `-1.2131` n `8`; equity avg `0.5759` n `67`; fx avg `-0.072` n `6`; index avg `0.8041` n `23`; metal avg `-0.1186` n `18`; unknown avg `0.2074` n `397`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1781`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1771`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1728`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1624`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1499`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
