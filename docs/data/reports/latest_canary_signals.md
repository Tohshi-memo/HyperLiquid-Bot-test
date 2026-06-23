# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T04:52:31.659838+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0115` n `12`; crypto_alt avg `-0.2377` n `228`; crypto_major avg `-0.2634` n `8`; equity avg `-0.238` n `86`; fx avg `0.0109` n `6`; index avg `-0.065` n `23`; metal avg `-0.0191` n `20`; unknown avg `1.6628` n `716`
- 1h: commodity avg `0.0672` n `12`; crypto_alt avg `-0.2786` n `228`; crypto_major avg `-0.6536` n `8`; equity avg `-0.3995` n `86`; fx avg `0.0018` n `6`; index avg `-0.0844` n `23`; metal avg `-0.0735` n `20`; unknown avg `6.0709` n `716`
- 4h: commodity avg `-0.0194` n `12`; crypto_alt avg `-0.0597` n `228`; crypto_major avg `-0.5502` n `8`; equity avg `-1.9095` n `86`; fx avg `-0.0543` n `6`; index avg `-0.3962` n `23`; metal avg `-0.7352` n `20`; unknown avg `0.0809` n `708`
- 24h: commodity avg `-0.49` n `12`; crypto_alt avg `-0.9519` n `228`; crypto_major avg `-0.8475` n `8`; equity avg `-2.707` n `85`; fx avg `-0.0434` n `6`; index avg `-0.4289` n `23`; metal avg `-0.77` n `18`; unknown avg `1.1441` n `639`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
