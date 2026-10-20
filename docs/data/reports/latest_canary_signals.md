# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T23:07:30.216813+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0201` n `13`; crypto_alt avg `-0.2278` n `237`; crypto_major avg `-0.2571` n `8`; equity avg `-0.1258` n `151`; fx avg `0.0045` n `6`; index avg `-0.0318` n `26`; metal avg `-0.0067` n `20`; unknown avg `0.2364` n `1181`
- 1h: commodity avg `0.0232` n `13`; crypto_alt avg `-0.3439` n `237`; crypto_major avg `-0.2543` n `8`; equity avg `-0.1389` n `151`; fx avg `-0.0179` n `6`; index avg `-0.0421` n `26`; metal avg `-0.0328` n `20`; unknown avg `0.0561` n `1141`
- 4h: commodity avg `0.0606` n `13`; crypto_alt avg `0.5225` n `237`; crypto_major avg `0.5854` n `8`; equity avg `1.2178` n `151`; fx avg `-0.0083` n `6`; index avg `0.1354` n `26`; metal avg `0.0055` n `20`; unknown avg `-0.0829` n `1049`
- 24h: commodity avg `-0.0054` n `13`; crypto_alt avg `2.2907` n `237`; crypto_major avg `1.6216` n `8`; equity avg `1.2413` n `151`; fx avg `0.0316` n `6`; index avg `0.1052` n `26`; metal avg `0.0853` n `20`; unknown avg `207.7198` n `1004`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1668`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
