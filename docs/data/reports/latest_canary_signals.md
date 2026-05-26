# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T15:07:24.973820+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1559` n `12`; crypto_alt avg `-0.6169` n `228`; crypto_major avg `-0.4912` n `8`; equity avg `-0.3002` n `67`; fx avg `0.0031` n `6`; index avg `-0.04` n `23`; metal avg `-0.179` n `18`; unknown avg `-0.2409` n `418`
- 1h: commodity avg `0.2059` n `12`; crypto_alt avg `-0.7811` n `228`; crypto_major avg `-0.7342` n `8`; equity avg `-0.0516` n `67`; fx avg `-0.011` n `6`; index avg `-0.0143` n `23`; metal avg `-0.1505` n `18`; unknown avg `0.2706` n `416`
- 4h: commodity avg `0.8942` n `12`; crypto_alt avg `-0.4351` n `228`; crypto_major avg `-0.1528` n `8`; equity avg `-0.0931` n `67`; fx avg `-0.0203` n `6`; index avg `0.3475` n `23`; metal avg `-0.1875` n `18`; unknown avg `-0.2049` n `415`
- 24h: commodity avg `0.8729` n `12`; crypto_alt avg `-0.934` n `228`; crypto_major avg `-0.9384` n `8`; equity avg `-0.5245` n `67`; fx avg `-0.1486` n `6`; index avg `0.4597` n `23`; metal avg `-1.1385` n `18`; unknown avg `-0.3166` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1865`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1821`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1739`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1707`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1366`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
