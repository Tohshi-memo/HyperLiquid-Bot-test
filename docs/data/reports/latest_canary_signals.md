# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T06:37:30.292952+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2443` n `12`; crypto_alt avg `0.0921` n `228`; crypto_major avg `0.0341` n `8`; equity avg `-0.0285` n `74`; fx avg `0.0134` n `6`; index avg `-0.0635` n `23`; metal avg `0.0137` n `18`; unknown avg `-0.032` n `554`
- 1h: commodity avg `-0.1269` n `12`; crypto_alt avg `0.2443` n `228`; crypto_major avg `0.5004` n `8`; equity avg `0.1079` n `74`; fx avg `0.0354` n `6`; index avg `0.0302` n `23`; metal avg `-0.2037` n `18`; unknown avg `-0.0923` n `538`
- 4h: commodity avg `-0.465` n `12`; crypto_alt avg `1.7134` n `228`; crypto_major avg `1.5214` n `8`; equity avg `0.9468` n `74`; fx avg `0.0137` n `6`; index avg `0.3889` n `23`; metal avg `0.4584` n `18`; unknown avg `0.5447` n `538`
- 24h: commodity avg `1.4585` n `12`; crypto_alt avg `1.6049` n `228`; crypto_major avg `1.6362` n `8`; equity avg `-0.4894` n `74`; fx avg `0.0285` n `6`; index avg `-0.6305` n `23`; metal avg `-1.0183` n `18`; unknown avg `3.5855` n `535`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
