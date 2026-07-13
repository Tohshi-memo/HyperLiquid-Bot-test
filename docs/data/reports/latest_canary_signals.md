# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T21:37:34.215507+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0072` n `12`; crypto_alt avg `-0.2475` n `230`; crypto_major avg `-0.244` n `8`; equity avg `-0.004` n `92`; fx avg `0.0046` n `6`; index avg `0.0004` n `25`; metal avg `0.0085` n `20`; unknown avg `-0.0134` n `766`
- 1h: commodity avg `-0.02` n `12`; crypto_alt avg `-0.454` n `230`; crypto_major avg `-0.4656` n `8`; equity avg `-0.0217` n `92`; fx avg `0.0223` n `6`; index avg `0.0055` n `25`; metal avg `0.0278` n `20`; unknown avg `-0.1189` n `766`
- 4h: commodity avg `0.27` n `12`; crypto_alt avg `-0.6048` n `230`; crypto_major avg `-0.3898` n `8`; equity avg `-0.1184` n `92`; fx avg `0.0017` n `6`; index avg `-0.0987` n `25`; metal avg `0.0303` n `20`; unknown avg `-0.3687` n `766`
- 24h: commodity avg `0.6354` n `12`; crypto_alt avg `-2.6218` n `230`; crypto_major avg `-3.2044` n `8`; equity avg `-3.3312` n `92`; fx avg `-0.0383` n `6`; index avg `-0.6696` n `25`; metal avg `-0.525` n `20`; unknown avg `-0.4117` n `749`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1866`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1743`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
