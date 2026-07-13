# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T19:22:25.363220+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0004` n `12`; crypto_alt avg `-0.0748` n `230`; crypto_major avg `0.0189` n `8`; equity avg `-0.1307` n `92`; fx avg `-0.002` n `6`; index avg `-0.0401` n `25`; metal avg `-0.0333` n `20`; unknown avg `-0.0431` n `766`
- 1h: commodity avg `-0.1749` n `12`; crypto_alt avg `0.0827` n `230`; crypto_major avg `0.3158` n `8`; equity avg `-0.1077` n `92`; fx avg `-0.0003` n `6`; index avg `-0.0155` n `25`; metal avg `0.0272` n `20`; unknown avg `0.1789` n `766`
- 4h: commodity avg `0.6229` n `12`; crypto_alt avg `-1.4943` n `230`; crypto_major avg `-1.1735` n `8`; equity avg `-1.4532` n `92`; fx avg `-0.0145` n `6`; index avg `-0.229` n `25`; metal avg `-0.2574` n `20`; unknown avg `0.023` n `766`
- 24h: commodity avg `0.6329` n `12`; crypto_alt avg `-2.5455` n `230`; crypto_major avg `-3.2043` n `8`; equity avg `-3.4228` n `92`; fx avg `-0.0891` n `6`; index avg `-0.6462` n `25`; metal avg `-0.5824` n `20`; unknown avg `-0.2969` n `749`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1896`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1765`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
