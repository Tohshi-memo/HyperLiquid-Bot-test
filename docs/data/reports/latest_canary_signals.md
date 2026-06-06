# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T16:52:24.747172+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0469` n `12`; crypto_alt avg `0.5451` n `228`; crypto_major avg `0.5074` n `8`; equity avg `0.1641` n `74`; fx avg `0.0412` n `6`; index avg `-0.0391` n `23`; metal avg `0.0245` n `18`; unknown avg `-0.0094` n `515`
- 1h: commodity avg `0.0881` n `12`; crypto_alt avg `0.1939` n `228`; crypto_major avg `-0.0887` n `8`; equity avg `0.1506` n `74`; fx avg `0.061` n `6`; index avg `0.0066` n `23`; metal avg `0.0738` n `18`; unknown avg `-2.3099` n `515`
- 4h: commodity avg `0.1957` n `12`; crypto_alt avg `-0.2329` n `228`; crypto_major avg `-0.7251` n `8`; equity avg `0.0293` n `74`; fx avg `0.0838` n `6`; index avg `0.1365` n `23`; metal avg `-0.1792` n `18`; unknown avg `-0.4745` n `415`
- 24h: commodity avg `0.5702` n `12`; crypto_alt avg `-2.0328` n `228`; crypto_major avg `-1.8133` n `8`; equity avg `-1.9969` n `74`; fx avg `0.0095` n `6`; index avg `-1.2347` n `23`; metal avg `-1.1751` n `18`; unknown avg `-0.3098` n `400`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
