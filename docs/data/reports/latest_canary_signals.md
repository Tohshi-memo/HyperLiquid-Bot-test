# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T02:07:27.412067+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0373` n `13`; crypto_alt avg `-0.1275` n `239`; crypto_major avg `-0.1995` n `8`; equity avg `-0.3878` n `166`; fx avg `-0.0233` n `6`; index avg `-0.0383` n `27`; metal avg `-0.172` n `20`; unknown avg `158.8715` n `1258`
- 1h: commodity avg `-0.1049` n `13`; crypto_alt avg `0.0046` n `239`; crypto_major avg `-0.4011` n `8`; equity avg `-1.104` n `166`; fx avg `-0.0222` n `6`; index avg `-0.0969` n `27`; metal avg `-0.1446` n `20`; unknown avg `158.6705` n `1262`
- 4h: commodity avg `-0.0059` n `13`; crypto_alt avg `0.4103` n `239`; crypto_major avg `-0.1259` n `8`; equity avg `-0.3124` n `166`; fx avg `0.0841` n `6`; index avg `0.052` n `27`; metal avg `-0.0086` n `20`; unknown avg `-0.2358` n `1250`
- 24h: commodity avg `-1.1587` n `13`; crypto_alt avg `1.6287` n `239`; crypto_major avg `1.5547` n `8`; equity avg `5.2419` n `166`; fx avg `-0.2201` n `6`; index avg `0.5758` n `27`; metal avg `0.4572` n `20`; unknown avg `264.1296` n `1051`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
