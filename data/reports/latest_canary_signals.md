# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T10:52:26.565032+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0387` n `13`; crypto_alt avg `-0.074` n `237`; crypto_major avg `0.0156` n `8`; equity avg `-0.1335` n `152`; fx avg `-0.0111` n `6`; index avg `-0.0195` n `26`; metal avg `-0.0229` n `20`; unknown avg `0.1521` n `1240`
- 1h: commodity avg `-0.05` n `13`; crypto_alt avg `-0.1269` n `237`; crypto_major avg `-0.0325` n `8`; equity avg `-0.3903` n `152`; fx avg `-0.006` n `6`; index avg `-0.0838` n `26`; metal avg `-0.1051` n `20`; unknown avg `3.6706` n `1240`
- 4h: commodity avg `0.0638` n `13`; crypto_alt avg `0.488` n `237`; crypto_major avg `0.4905` n `8`; equity avg `0.2156` n `152`; fx avg `-0.0043` n `6`; index avg `0.0713` n `26`; metal avg `0.0521` n `20`; unknown avg `2.6467` n `1142`
- 24h: commodity avg `-0.5205` n `13`; crypto_alt avg `0.7585` n `237`; crypto_major avg `0.6318` n `8`; equity avg `-0.2686` n `152`; fx avg `0.0402` n `6`; index avg `0.0143` n `26`; metal avg `0.153` n `20`; unknown avg `-0.1309` n `977`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.263`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2321`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2317`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.2043`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.16`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1555`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1513`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1491`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
