# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T11:37:24.770584+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0093` n `12`; crypto_alt avg `0.1126` n `232`; crypto_major avg `-0.0167` n `8`; equity avg `-0.0143` n `134`; fx avg `-0.0107` n `6`; index avg `-0.0012` n `26`; metal avg `0.0026` n `20`; unknown avg `-0.1597` n `794`
- 1h: commodity avg `-0.0119` n `12`; crypto_alt avg `0.3892` n `232`; crypto_major avg `0.096` n `8`; equity avg `0.0222` n `134`; fx avg `-0.0163` n `6`; index avg `0.0074` n `26`; metal avg `0.0025` n `20`; unknown avg `0.4177` n `792`
- 4h: commodity avg `0.0118` n `12`; crypto_alt avg `1.1291` n `232`; crypto_major avg `0.4986` n `8`; equity avg `0.2` n `134`; fx avg `-0.0107` n `6`; index avg `0.011` n `26`; metal avg `0.0059` n `20`; unknown avg `-0.0244` n `786`
- 24h: commodity avg `0.1419` n `12`; crypto_alt avg `2.4337` n `232`; crypto_major avg `2.0862` n `8`; equity avg `0.4967` n `134`; fx avg `-0.0076` n `6`; index avg `0.0762` n `26`; metal avg `0.0062` n `20`; unknown avg `492.5729` n `677`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
