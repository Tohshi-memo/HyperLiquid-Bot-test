# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T21:52:26.841102+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0427` n `12`; crypto_alt avg `0.1571` n `234`; crypto_major avg `0.1794` n `8`; equity avg `0.0177` n `141`; fx avg `0.0151` n `6`; index avg `0.0005` n `26`; metal avg `0.0059` n `20`; unknown avg `0.2031` n `960`
- 1h: commodity avg `0.0324` n `12`; crypto_alt avg `-0.6371` n `234`; crypto_major avg `-0.2557` n `8`; equity avg `0.0357` n `141`; fx avg `-0.0063` n `6`; index avg `0.0148` n `26`; metal avg `0.0041` n `20`; unknown avg `-0.1809` n `956`
- 4h: commodity avg `0.1076` n `12`; crypto_alt avg `0.3149` n `234`; crypto_major avg `0.184` n `8`; equity avg `-0.0371` n `141`; fx avg `-0.0061` n `6`; index avg `0.0329` n `26`; metal avg `0.0378` n `20`; unknown avg `-0.3564` n `876`
- 24h: commodity avg `-0.5915` n `12`; crypto_alt avg `1.4995` n `234`; crypto_major avg `0.3345` n `8`; equity avg `0.1044` n `141`; fx avg `-0.2354` n `6`; index avg `0.2527` n `26`; metal avg `0.2` n `20`; unknown avg `1147.3319` n `794`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1805`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
