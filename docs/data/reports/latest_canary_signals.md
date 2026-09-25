# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T04:52:28.789698+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0136` n `12`; crypto_alt avg `-0.0942` n `234`; crypto_major avg `-0.074` n `8`; equity avg `0.0057` n `141`; fx avg `-0.0011` n `6`; index avg `0.0048` n `26`; metal avg `-0.006` n `20`; unknown avg `53.6142` n `946`
- 1h: commodity avg `0.0439` n `12`; crypto_alt avg `0.448` n `234`; crypto_major avg `0.1563` n `8`; equity avg `0.0627` n `141`; fx avg `0.0118` n `6`; index avg `0.0055` n `26`; metal avg `-0.0179` n `20`; unknown avg `19.2191` n `938`
- 4h: commodity avg `-0.0221` n `12`; crypto_alt avg `-0.4208` n `234`; crypto_major avg `-0.4078` n `8`; equity avg `0.3334` n `141`; fx avg `-0.1124` n `6`; index avg `0.0909` n `26`; metal avg `-0.041` n `20`; unknown avg `2.6168` n `938`
- 24h: commodity avg `0.5079` n `12`; crypto_alt avg `2.1788` n `234`; crypto_major avg `0.8335` n `8`; equity avg `0.5462` n `141`; fx avg `-0.1407` n `6`; index avg `0.0412` n `26`; metal avg `-0.1873` n `20`; unknown avg `16.9077` n `815`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1533`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1405`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
