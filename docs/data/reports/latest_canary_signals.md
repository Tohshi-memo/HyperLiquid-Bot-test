# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T05:22:30.310387+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0562` n `12`; crypto_alt avg `-0.1377` n `228`; crypto_major avg `-0.0542` n `8`; equity avg `-0.1548` n `86`; fx avg `-0.0043` n `6`; index avg `-0.0366` n `23`; metal avg `-0.0326` n `20`; unknown avg `2.7413` n `716`
- 1h: commodity avg `0.0468` n `12`; crypto_alt avg `-0.5376` n `228`; crypto_major avg `-0.4462` n `8`; equity avg `-0.5387` n `86`; fx avg `-0.0108` n `6`; index avg `-0.1185` n `23`; metal avg `-0.0988` n `20`; unknown avg `1.4242` n `716`
- 4h: commodity avg `-0.0405` n `12`; crypto_alt avg `-0.5528` n `228`; crypto_major avg `-0.842` n `8`; equity avg `-1.9793` n `86`; fx avg `-0.0292` n `6`; index avg `-0.4248` n `23`; metal avg `-0.6342` n `20`; unknown avg `-0.1013` n `708`
- 24h: commodity avg `-0.4501` n `12`; crypto_alt avg `-1.3886` n `228`; crypto_major avg `-1.2492` n `8`; equity avg `-3.1284` n `85`; fx avg `-0.0448` n `6`; index avg `-0.5333` n `23`; metal avg `-0.9359` n `18`; unknown avg `1.0676` n `639`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
