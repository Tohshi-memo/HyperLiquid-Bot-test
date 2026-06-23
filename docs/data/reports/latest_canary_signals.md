# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T04:22:29.302199+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.511` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0035` n `12`; crypto_alt avg `-0.1737` n `228`; crypto_major avg `-0.2613` n `8`; equity avg `-0.2347` n `86`; fx avg `0.0082` n `6`; index avg `-0.0726` n `23`; metal avg `-0.0414` n `20`; unknown avg `0.1318` n `716`
- 1h: commodity avg `-0.013` n `12`; crypto_alt avg `0.2839` n `228`; crypto_major avg `-0.1532` n `8`; equity avg `-0.0369` n `86`; fx avg `-0.0174` n `6`; index avg `-0.064` n `23`; metal avg `0.058` n `20`; unknown avg `2.5113` n `716`
- 4h: commodity avg `-0.1002` n `12`; crypto_alt avg `0.5808` n `228`; crypto_major avg `0.0149` n `8`; equity avg `-1.4961` n `86`; fx avg `-0.0489` n `6`; index avg `-0.2963` n `23`; metal avg `-0.5229` n `20`; unknown avg `0.381` n `708`
- 24h: commodity avg `-0.5585` n `12`; crypto_alt avg `-0.5451` n `228`; crypto_major avg `-0.3903` n `8`; equity avg `-2.4846` n `85`; fx avg `-0.0396` n `6`; index avg `-0.3977` n `23`; metal avg `-0.7173` n `18`; unknown avg `0.8671` n `639`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
