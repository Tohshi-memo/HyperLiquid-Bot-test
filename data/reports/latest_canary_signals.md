# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T01:36:03.555693+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0109` n `13`; crypto_alt avg `0.0176` n `237`; crypto_major avg `0.07` n `8`; equity avg `-0.0068` n `152`; fx avg `0.0031` n `6`; index avg `0.0005` n `26`; metal avg `-0.0009` n `20`; unknown avg `0.7417` n `1231`
- 1h: commodity avg `-0.0078` n `13`; crypto_alt avg `-0.3547` n `237`; crypto_major avg `-0.0328` n `8`; equity avg `0.0302` n `152`; fx avg `0.0035` n `6`; index avg `0.004` n `26`; metal avg `0.0006` n `20`; unknown avg `0.2441` n `1225`
- 4h: commodity avg `-0.0539` n `13`; crypto_alt avg `0.5428` n `237`; crypto_major avg `0.7203` n `8`; equity avg `0.2353` n `152`; fx avg `-0.0005` n `6`; index avg `0.0144` n `26`; metal avg `0.0277` n `20`; unknown avg `0.2372` n `1173`
- 24h: commodity avg `-0.0997` n `13`; crypto_alt avg `-0.5942` n `237`; crypto_major avg `0.1196` n `8`; equity avg `0.1767` n `152`; fx avg `-0.0275` n `6`; index avg `0.0173` n `26`; metal avg `-0.0646` n `20`; unknown avg `0.9002` n `1064`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.193`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1788`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.174`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1591`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1503`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1346`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
