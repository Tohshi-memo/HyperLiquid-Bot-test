# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T05:07:34.547311+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0296` n `13`; crypto_alt avg `-0.0691` n `239`; crypto_major avg `-0.0431` n `8`; equity avg `-0.0291` n `168`; fx avg `-0.0011` n `6`; index avg `0.0046` n `27`; metal avg `0.0187` n `20`; unknown avg `1.5228` n `1255`
- 1h: commodity avg `-0.0171` n `13`; crypto_alt avg `-0.1735` n `239`; crypto_major avg `-0.0582` n `8`; equity avg `-0.0065` n `168`; fx avg `0.0018` n `6`; index avg `0.0272` n `27`; metal avg `0.1033` n `20`; unknown avg `-0.0782` n `1253`
- 4h: commodity avg `0.0311` n `13`; crypto_alt avg `0.2137` n `239`; crypto_major avg `0.5495` n `8`; equity avg `0.2922` n `168`; fx avg `-0.0267` n `6`; index avg `0.028` n `27`; metal avg `0.3736` n `20`; unknown avg `191.4085` n `1241`
- 24h: commodity avg `0.7028` n `13`; crypto_alt avg `3.0059` n `239`; crypto_major avg `3.1113` n `8`; equity avg `2.7003` n `168`; fx avg `0.0227` n `6`; index avg `0.2093` n `27`; metal avg `0.7241` n `20`; unknown avg `774.9447` n `1019`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1642`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
