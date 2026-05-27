# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T04:07:19.311936+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2324` n `12`; crypto_alt avg `-0.0929` n `228`; crypto_major avg `-0.0018` n `8`; equity avg `-0.0507` n `67`; fx avg `-0.0087` n `6`; index avg `-0.0237` n `23`; metal avg `0.0325` n `18`; unknown avg `-0.4623` n `418`
- 1h: commodity avg `-0.1106` n `12`; crypto_alt avg `-0.5231` n `228`; crypto_major avg `-0.5021` n `8`; equity avg `-0.194` n `67`; fx avg `-0.0058` n `6`; index avg `-0.0911` n `23`; metal avg `-0.2317` n `18`; unknown avg `-0.4873` n `418`
- 4h: commodity avg `-0.6636` n `12`; crypto_alt avg `-0.7548` n `228`; crypto_major avg `-0.1915` n `8`; equity avg `-0.1843` n `67`; fx avg `-0.0729` n `6`; index avg `-0.0866` n `23`; metal avg `-0.5439` n `18`; unknown avg `-0.317` n `418`
- 24h: commodity avg `-0.3883` n `12`; crypto_alt avg `-0.7304` n `228`; crypto_major avg `-0.3745` n `8`; equity avg `0.577` n `67`; fx avg `-0.0763` n `6`; index avg `0.9003` n `23`; metal avg `-0.2366` n `18`; unknown avg `0.6062` n `397`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.185`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1716`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1716`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1699`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1684`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1633`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
