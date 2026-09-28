# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T01:52:30.039927+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0059` n `12`; crypto_alt avg `-0.4695` n `234`; crypto_major avg `-0.4198` n `8`; equity avg `-0.2564` n `141`; fx avg `0.0056` n `6`; index avg `-0.0437` n `26`; metal avg `0.0074` n `20`; unknown avg `-0.0718` n `956`
- 1h: commodity avg `0.0521` n `12`; crypto_alt avg `-1.2562` n `234`; crypto_major avg `-1.0272` n `8`; equity avg `-0.7509` n `141`; fx avg `0.0517` n `6`; index avg `-0.1036` n `26`; metal avg `-0.2198` n `20`; unknown avg `2.4048` n `950`
- 4h: commodity avg `-0.4012` n `12`; crypto_alt avg `-1.0379` n `234`; crypto_major avg `-1.1235` n `8`; equity avg `-1.2627` n `141`; fx avg `0.1329` n `6`; index avg `-0.1439` n `26`; metal avg `-0.5707` n `20`; unknown avg `2.6635` n `910`
- 24h: commodity avg `-0.4175` n `12`; crypto_alt avg `-0.293` n `234`; crypto_major avg `-1.0584` n `8`; equity avg `-0.9966` n `141`; fx avg `0.0961` n `6`; index avg `-0.0931` n `26`; metal avg `-0.5937` n `20`; unknown avg `13.4565` n `819`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1688`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1563`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
