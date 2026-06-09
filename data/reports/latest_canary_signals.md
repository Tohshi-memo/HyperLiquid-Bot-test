# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T14:52:49.413104+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0083` n `12`; crypto_alt avg `-0.0114` n `228`; crypto_major avg `-0.0324` n `8`; equity avg `-1.0143` n `74`; fx avg `-0.0064` n `6`; index avg `-0.6036` n `23`; metal avg `-0.4271` n `18`; unknown avg `0.0002` n `547`
- 1h: commodity avg `0.1427` n `12`; crypto_alt avg `-1.7071` n `228`; crypto_major avg `-1.689` n `8`; equity avg `-2.6096` n `74`; fx avg `0.0046` n `6`; index avg `-1.5455` n `23`; metal avg `-1.5182` n `18`; unknown avg `-0.19` n `545`
- 4h: commodity avg `-0.4041` n `12`; crypto_alt avg `-1.1229` n `228`; crypto_major avg `-1.9572` n `8`; equity avg `-2.2633` n `74`; fx avg `0.0274` n `6`; index avg `-1.4591` n `23`; metal avg `-1.4058` n `18`; unknown avg `-0.3272` n `545`
- 24h: commodity avg `-1.029` n `12`; crypto_alt avg `-2.8123` n `228`; crypto_major avg `-3.2102` n `8`; equity avg `-1.978` n `74`; fx avg `0.1253` n `6`; index avg `-1.1535` n `23`; metal avg `-0.7685` n `18`; unknown avg `-1.388` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0503`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0476`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0468`, n `668`, weak_sample_signal
