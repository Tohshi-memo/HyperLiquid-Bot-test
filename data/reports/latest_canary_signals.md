# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T00:37:24.244614+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0061` n `13`; crypto_alt avg `0.1689` n `237`; crypto_major avg `0.1702` n `8`; equity avg `0.0163` n `152`; fx avg `0.0045` n `6`; index avg `0.0002` n `26`; metal avg `-0.0001` n `20`; unknown avg `0.0326` n `1231`
- 1h: commodity avg `-0.0069` n `13`; crypto_alt avg `0.0572` n `237`; crypto_major avg `0.0853` n `8`; equity avg `0.0286` n `152`; fx avg `-0.0033` n `6`; index avg `-0.0013` n `26`; metal avg `-0.0031` n `20`; unknown avg `0.5465` n `1225`
- 4h: commodity avg `-0.0382` n `13`; crypto_alt avg `0.6941` n `237`; crypto_major avg `0.6895` n `8`; equity avg `0.1221` n `152`; fx avg `0.0011` n `6`; index avg `0.0102` n `26`; metal avg `0.0027` n `20`; unknown avg `0.1463` n `1151`
- 24h: commodity avg `-0.1206` n `13`; crypto_alt avg `-0.1552` n `237`; crypto_major avg `0.2072` n `8`; equity avg `0.1453` n `152`; fx avg `-0.0374` n `6`; index avg `0.0071` n `26`; metal avg `-0.0615` n `20`; unknown avg `0.6475` n `1064`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1926`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1751`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1596`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1353`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
