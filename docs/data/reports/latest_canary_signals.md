# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T18:22:35.205565+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0144` n `12`; crypto_alt avg `0.1465` n `234`; crypto_major avg `0.0637` n `8`; equity avg `0.0165` n `140`; fx avg `0.0083` n `6`; index avg `0.0054` n `26`; metal avg `0.0069` n `20`; unknown avg `0.6726` n `940`
- 1h: commodity avg `0.021` n `12`; crypto_alt avg `0.3364` n `234`; crypto_major avg `0.3016` n `8`; equity avg `0.1807` n `140`; fx avg `0.013` n `6`; index avg `0.0323` n `26`; metal avg `0.0492` n `20`; unknown avg `0.2181` n `920`
- 4h: commodity avg `-0.264` n `12`; crypto_alt avg `0.7206` n `234`; crypto_major avg `0.7528` n `8`; equity avg `0.4333` n `140`; fx avg `-0.0668` n `6`; index avg `0.0285` n `26`; metal avg `0.2441` n `20`; unknown avg `-0.11` n `906`
- 24h: commodity avg `-0.203` n `12`; crypto_alt avg `5.9873` n `234`; crypto_major avg `6.5068` n `8`; equity avg `0.7203` n `140`; fx avg `0.1934` n `6`; index avg `-0.0956` n `26`; metal avg `0.3605` n `20`; unknown avg `1.9634` n `717`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1475`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
