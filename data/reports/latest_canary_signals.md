# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T00:22:30.711945+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0018` n `13`; crypto_alt avg `-0.0239` n `237`; crypto_major avg `-0.0408` n `8`; equity avg `0.0185` n `152`; fx avg `-0.0025` n `6`; index avg `0.0005` n `26`; metal avg `-0.0022` n `20`; unknown avg `0.2728` n `1231`
- 1h: commodity avg `-0.0053` n `13`; crypto_alt avg `0.3504` n `237`; crypto_major avg `0.3746` n `8`; equity avg `0.0724` n `152`; fx avg `-0.004` n `6`; index avg `0.0023` n `26`; metal avg `0.0101` n `20`; unknown avg `0.3014` n `1225`
- 4h: commodity avg `-0.0897` n `13`; crypto_alt avg `0.5269` n `237`; crypto_major avg `0.4822` n `8`; equity avg `0.1017` n `152`; fx avg `-0.0074` n `6`; index avg `0.0086` n `26`; metal avg `0.0093` n `20`; unknown avg `0.3547` n `1149`
- 24h: commodity avg `-0.128` n `13`; crypto_alt avg `-0.216` n `237`; crypto_major avg `-0.0018` n `8`; equity avg `0.1553` n `152`; fx avg `-0.0426` n `6`; index avg `0.0055` n `26`; metal avg `-0.055` n `20`; unknown avg `0.6198` n `1064`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1926`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1754`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1595`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1498`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1428`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1354`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
