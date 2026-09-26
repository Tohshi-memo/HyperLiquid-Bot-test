# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T17:52:28.530078+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.001` n `12`; crypto_alt avg `-0.1184` n `234`; crypto_major avg `-0.0356` n `8`; equity avg `-0.0011` n `141`; fx avg `-0.0127` n `6`; index avg `-0.0114` n `26`; metal avg `0.0006` n `20`; unknown avg `0.3967` n `961`
- 1h: commodity avg `0.0018` n `12`; crypto_alt avg `-0.5419` n `234`; crypto_major avg `-0.326` n `8`; equity avg `-0.0288` n `141`; fx avg `-0.0106` n `6`; index avg `-0.0114` n `26`; metal avg `0.0024` n `20`; unknown avg `7.1635` n `959`
- 4h: commodity avg `-0.0116` n `12`; crypto_alt avg `0.6034` n `234`; crypto_major avg `0.15` n `8`; equity avg `0.0812` n `141`; fx avg `-0.0197` n `6`; index avg `0.0066` n `26`; metal avg `-0.0007` n `20`; unknown avg `19.7922` n `945`
- 24h: commodity avg `0.3669` n `12`; crypto_alt avg `2.6888` n `234`; crypto_major avg `0.0804` n `8`; equity avg `-0.0371` n `141`; fx avg `0.0065` n `6`; index avg `-0.0142` n `26`; metal avg `-0.0032` n `20`; unknown avg `4.9536` n `814`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1575`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
