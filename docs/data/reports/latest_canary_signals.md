# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T12:52:33.582226+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0588` n `12`; crypto_alt avg `-0.2848` n `228`; crypto_major avg `-0.2211` n `8`; equity avg `-0.0144` n `86`; fx avg `0.0086` n `6`; index avg `-0.0033` n `23`; metal avg `0.0717` n `20`; unknown avg `-0.1055` n `764`
- 1h: commodity avg `0.0186` n `12`; crypto_alt avg `-0.2863` n `228`; crypto_major avg `-0.3236` n `8`; equity avg `-0.469` n `86`; fx avg `-0.0291` n `6`; index avg `-0.0978` n `23`; metal avg `0.027` n `20`; unknown avg `-0.0265` n `764`
- 4h: commodity avg `-0.1088` n `12`; crypto_alt avg `0.2564` n `228`; crypto_major avg `0.0061` n `8`; equity avg `0.247` n `86`; fx avg `-0.055` n `6`; index avg `-0.0482` n `23`; metal avg `0.0936` n `20`; unknown avg `-0.3262` n `764`
- 24h: commodity avg `-0.4287` n `12`; crypto_alt avg `-4.9141` n `228`; crypto_major avg `-5.1388` n `8`; equity avg `-4.6707` n `85`; fx avg `-0.1886` n `6`; index avg `-0.9907` n `23`; metal avg `-1.26` n `20`; unknown avg `0.0619` n `604`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1538`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
