# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T18:52:23.558239+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0038` n `12`; crypto_alt avg `0.5566` n `228`; crypto_major avg `0.2719` n `8`; equity avg `0.0934` n `67`; fx avg `0.0101` n `6`; index avg `0.021` n `23`; metal avg `0.0078` n `18`; unknown avg `-0.0041` n `418`
- 1h: commodity avg `-0.322` n `12`; crypto_alt avg `0.1948` n `228`; crypto_major avg `0.1386` n `8`; equity avg `0.2802` n `67`; fx avg `0.0058` n `6`; index avg `0.129` n `23`; metal avg `0.0402` n `18`; unknown avg `0.0981` n `418`
- 4h: commodity avg `-0.667` n `12`; crypto_alt avg `0.0524` n `228`; crypto_major avg `-0.2335` n `8`; equity avg `0.0088` n `67`; fx avg `0.0006` n `6`; index avg `0.2066` n `23`; metal avg `0.1444` n `18`; unknown avg `-0.3252` n `418`
- 24h: commodity avg `-1.2783` n `12`; crypto_alt avg `-0.4273` n `228`; crypto_major avg `-0.7337` n `8`; equity avg `-0.1106` n `67`; fx avg `-0.0591` n `6`; index avg `-0.4706` n `23`; metal avg `-0.9874` n `18`; unknown avg `-0.2828` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1763`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1738`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1638`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1591`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
