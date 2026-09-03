# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T21:22:29.403764+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0071` n `12`; crypto_alt avg `0.17` n `232`; crypto_major avg `0.1907` n `8`; equity avg `0.011` n `133`; fx avg `0.0086` n `6`; index avg `-0.0016` n `26`; metal avg `0.0088` n `20`; unknown avg `0.0404` n `786`
- 1h: commodity avg `0.0361` n `12`; crypto_alt avg `0.3293` n `232`; crypto_major avg `0.1758` n `8`; equity avg `-0.0171` n `133`; fx avg `0.0063` n `6`; index avg `-0.0108` n `26`; metal avg `0.0144` n `20`; unknown avg `0.1046` n `774`
- 4h: commodity avg `-0.1242` n `12`; crypto_alt avg `0.5789` n `232`; crypto_major avg `0.6516` n `8`; equity avg `0.1145` n `133`; fx avg `0.0152` n `6`; index avg `0.0229` n `26`; metal avg `-0.0834` n `20`; unknown avg `-0.1366` n `772`
- 24h: commodity avg `-0.0315` n `12`; crypto_alt avg `4.6511` n `232`; crypto_major avg `5.5732` n `8`; equity avg `1.3293` n `133`; fx avg `-0.2055` n `6`; index avg `0.177` n `26`; metal avg `0.7724` n `20`; unknown avg `29.3714` n `736`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
