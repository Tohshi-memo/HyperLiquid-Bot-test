# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T01:52:25.664821+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0246` n `12`; crypto_alt avg `0.1511` n `234`; crypto_major avg `0.2598` n `8`; equity avg `0.0321` n `141`; fx avg `0.0166` n `6`; index avg `0.0098` n `26`; metal avg `-0.0602` n `20`; unknown avg `0.4717` n `946`
- 1h: commodity avg `-0.0267` n `12`; crypto_alt avg `-0.0193` n `234`; crypto_major avg `0.0426` n `8`; equity avg `0.2777` n `141`; fx avg `-0.043` n `6`; index avg `0.081` n `26`; metal avg `0.0649` n `20`; unknown avg `1.3605` n `944`
- 4h: commodity avg `-0.3471` n `12`; crypto_alt avg `-0.3613` n `234`; crypto_major avg `-0.1524` n `8`; equity avg `0.2663` n `141`; fx avg `-0.0538` n `6`; index avg `0.0709` n `26`; metal avg `0.0274` n `20`; unknown avg `4.2255` n `898`
- 24h: commodity avg `0.469` n `12`; crypto_alt avg `3.7946` n `234`; crypto_major avg `1.406` n `8`; equity avg `0.2035` n `141`; fx avg `-0.0514` n `6`; index avg `0.0008` n `26`; metal avg `-0.0582` n `20`; unknown avg `22.1027` n `815`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1409`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
