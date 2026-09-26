# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T17:59:46.586018+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.013` n `12`; crypto_alt avg `-0.1181` n `234`; crypto_major avg `-0.0224` n `8`; equity avg `-0.0138` n `141`; fx avg `0.006` n `6`; index avg `-0.0079` n `26`; metal avg `-0.0002` n `20`; unknown avg `0.4668` n `961`
- 1h: commodity avg `0.0138` n `12`; crypto_alt avg `-0.5418` n `234`; crypto_major avg `-0.3128` n `8`; equity avg `-0.0416` n `141`; fx avg `0.008` n `6`; index avg `-0.0079` n `26`; metal avg `0.0016` n `20`; unknown avg `5.3756` n `959`
- 4h: commodity avg `0.0003` n `12`; crypto_alt avg `0.603` n `234`; crypto_major avg `0.1632` n `8`; equity avg `0.0683` n `141`; fx avg `-0.001` n `6`; index avg `0.0102` n `26`; metal avg `-0.0015` n `20`; unknown avg `19.7602` n `945`
- 24h: commodity avg `0.3791` n `12`; crypto_alt avg `2.6888` n `234`; crypto_major avg `0.0935` n `8`; equity avg `-0.0499` n `141`; fx avg `0.0251` n `6`; index avg `-0.0106` n `26`; metal avg `-0.004` n `20`; unknown avg `4.9741` n `814`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1575`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
