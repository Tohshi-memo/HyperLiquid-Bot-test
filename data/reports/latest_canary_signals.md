# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T14:07:33.779329+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0527` n `12`; crypto_alt avg `0.0859` n `230`; crypto_major avg `0.0961` n `8`; equity avg `-0.084` n `98`; fx avg `0.0117` n `6`; index avg `-0.0127` n `25`; metal avg `0.0557` n `20`; unknown avg `0.1088` n `771`
- 1h: commodity avg `-0.0002` n `12`; crypto_alt avg `0.0085` n `230`; crypto_major avg `-0.112` n `8`; equity avg `0.4388` n `98`; fx avg `0.0052` n `6`; index avg `-0.0004` n `25`; metal avg `-0.0917` n `20`; unknown avg `0.0492` n `771`
- 4h: commodity avg `0.1579` n `12`; crypto_alt avg `-0.0154` n `230`; crypto_major avg `-0.0279` n `8`; equity avg `0.387` n `98`; fx avg `-0.0046` n `6`; index avg `0.0041` n `25`; metal avg `-0.1122` n `20`; unknown avg `0.1404` n `771`
- 24h: commodity avg `0.4947` n `12`; crypto_alt avg `2.1698` n `230`; crypto_major avg `2.7003` n `8`; equity avg `2.0364` n `98`; fx avg `-0.0468` n `6`; index avg `0.1773` n `25`; metal avg `0.5514` n `20`; unknown avg `0.2593` n `754`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0878`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0589`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0565`, n `666`, weak_sample_signal
