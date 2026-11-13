# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T07:22:25.187617+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.006` n `13`; crypto_alt avg `0.3063` n `239`; crypto_major avg `0.1238` n `8`; equity avg `0.0473` n `162`; fx avg `0.0008` n `6`; index avg `0.005` n `27`; metal avg `-0.0581` n `20`; unknown avg `0.455` n `1260`
- 1h: commodity avg `0.0389` n `13`; crypto_alt avg `1.1228` n `239`; crypto_major avg `0.7511` n `8`; equity avg `0.3059` n `162`; fx avg `-0.0035` n `6`; index avg `0.0282` n `27`; metal avg `-0.0201` n `20`; unknown avg `1.1807` n `1258`
- 4h: commodity avg `0.0364` n `13`; crypto_alt avg `1.8611` n `239`; crypto_major avg `0.7401` n `8`; equity avg `-0.4051` n `162`; fx avg `0.0488` n `6`; index avg `-0.0575` n `27`; metal avg `-0.2326` n `20`; unknown avg `0.2605` n `1216`
- 24h: commodity avg `0.582` n `13`; crypto_alt avg `-0.6123` n `239`; crypto_major avg `-2.8844` n `8`; equity avg `-0.8547` n `162`; fx avg `-0.0114` n `6`; index avg `0.0617` n `27`; metal avg `-0.4831` n `20`; unknown avg `98.7348` n `1133`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
