# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T17:56:07.709062+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0253` n `12`; crypto_alt avg `0.1725` n `234`; crypto_major avg `0.0819` n `8`; equity avg `0.0167` n `141`; fx avg `-0.0082` n `6`; index avg `0.0111` n `26`; metal avg `0.0235` n `20`; unknown avg `0.1466` n `960`
- 1h: commodity avg `0.0442` n `12`; crypto_alt avg `-0.2153` n `234`; crypto_major avg `-0.3114` n `8`; equity avg `-0.0943` n `141`; fx avg `-0.0087` n `6`; index avg `0.0088` n `26`; metal avg `-0.0024` n `20`; unknown avg `-0.0657` n `958`
- 4h: commodity avg `-0.1424` n `12`; crypto_alt avg `0.306` n `234`; crypto_major avg `-0.2575` n `8`; equity avg `-0.0722` n `141`; fx avg `0.002` n `6`; index avg `0.0538` n `26`; metal avg `0.1091` n `20`; unknown avg `4.3694` n `894`
- 24h: commodity avg `-0.9996` n `12`; crypto_alt avg `1.7751` n `234`; crypto_major avg `0.5518` n `8`; equity avg `0.2417` n `141`; fx avg `-0.2497` n `6`; index avg `0.2284` n `26`; metal avg `0.2114` n `20`; unknown avg `1601.7988` n `805`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1787`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
