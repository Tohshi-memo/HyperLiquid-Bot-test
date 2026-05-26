# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T16:37:18.716002+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1298` n `12`; crypto_alt avg `0.1651` n `228`; crypto_major avg `0.0738` n `8`; equity avg `0.2296` n `67`; fx avg `0.0015` n `6`; index avg `0.0835` n `23`; metal avg `0.1152` n `18`; unknown avg `0.2225` n `418`
- 1h: commodity avg `-0.2479` n `12`; crypto_alt avg `-0.0283` n `228`; crypto_major avg `0.0633` n `8`; equity avg `0.1829` n `67`; fx avg `0.0331` n `6`; index avg `0.2286` n `23`; metal avg `0.178` n `18`; unknown avg `0.3855` n `418`
- 4h: commodity avg `0.6216` n `12`; crypto_alt avg `-0.7892` n `228`; crypto_major avg `-0.4706` n `8`; equity avg `0.0961` n `67`; fx avg `0.0016` n `6`; index avg `0.4269` n `23`; metal avg `-0.1326` n `18`; unknown avg `0.1019` n `415`
- 24h: commodity avg `0.9214` n `12`; crypto_alt avg `-1.226` n `228`; crypto_major avg `-0.8894` n `8`; equity avg `-0.2211` n `67`; fx avg `-0.1266` n `6`; index avg `0.4997` n `23`; metal avg `-1.106` n `18`; unknown avg `0.1093` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1768`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1745`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.165`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
