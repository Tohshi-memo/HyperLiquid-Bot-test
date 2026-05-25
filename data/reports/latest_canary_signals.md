# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T14:22:18.294147+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1234` n `12`; crypto_alt avg `0.2128` n `228`; crypto_major avg `0.0596` n `8`; equity avg `-0.0103` n `67`; fx avg `-0.0016` n `6`; index avg `-0.0139` n `23`; metal avg `0.034` n `18`; unknown avg `-0.2672` n `405`
- 1h: commodity avg `-0.3335` n `12`; crypto_alt avg `0.5785` n `228`; crypto_major avg `0.2772` n `8`; equity avg `0.1162` n `67`; fx avg `-0.0169` n `6`; index avg `0.0523` n `23`; metal avg `0.3328` n `18`; unknown avg `0.0955` n `405`
- 4h: commodity avg `0.3142` n `12`; crypto_alt avg `0.4488` n `228`; crypto_major avg `0.2582` n `8`; equity avg `0.0809` n `67`; fx avg `0.0147` n `6`; index avg `0.0892` n `23`; metal avg `-0.0564` n `18`; unknown avg `-0.1255` n `397`
- 24h: commodity avg `-0.8232` n `12`; crypto_alt avg `2.4373` n `228`; crypto_major avg `1.1474` n `8`; equity avg `0.9185` n `67`; fx avg `-0.0015` n `6`; index avg `0.331` n `23`; metal avg `1.378` n `18`; unknown avg `0.76` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1474`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
