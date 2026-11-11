# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T08:52:27.863743+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0016` n `13`; crypto_alt avg `0.1381` n `239`; crypto_major avg `0.0938` n `8`; equity avg `-0.0608` n `161`; fx avg `-0.015` n `6`; index avg `-0.0108` n `27`; metal avg `-0.0384` n `20`; unknown avg `1.1471` n `1261`
- 1h: commodity avg `-0.0364` n `13`; crypto_alt avg `0.137` n `239`; crypto_major avg `-0.045` n `8`; equity avg `0.3797` n `161`; fx avg `-0.0468` n `6`; index avg `0.023` n `27`; metal avg `0.0057` n `20`; unknown avg `0.2976` n `1239`
- 4h: commodity avg `0.0088` n `13`; crypto_alt avg `-0.7451` n `239`; crypto_major avg `-0.2289` n `8`; equity avg `0.6677` n `161`; fx avg `-0.0853` n `6`; index avg `0.0236` n `27`; metal avg `0.1481` n `20`; unknown avg `0.1784` n `1201`
- 24h: commodity avg `0.6679` n `13`; crypto_alt avg `-1.1141` n `239`; crypto_major avg `-2.1162` n `8`; equity avg `1.767` n `161`; fx avg `-0.2466` n `6`; index avg `0.1841` n `27`; metal avg `-0.0282` n `20`; unknown avg `50.3553` n `1167`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1704`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1337`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
