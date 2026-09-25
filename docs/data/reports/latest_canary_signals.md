# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T09:07:34.909441+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0946` n `12`; crypto_alt avg `0.2634` n `234`; crypto_major avg `0.3913` n `8`; equity avg `0.1172` n `141`; fx avg `-0.0261` n `6`; index avg `0.0194` n `26`; metal avg `0.009` n `20`; unknown avg `-0.1967` n `944`
- 1h: commodity avg `-0.3063` n `12`; crypto_alt avg `1.0911` n `234`; crypto_major avg `0.8807` n `8`; equity avg `0.4264` n `141`; fx avg `-0.0229` n `6`; index avg `0.0924` n `26`; metal avg `0.1544` n `20`; unknown avg `1.9627` n `942`
- 4h: commodity avg `-0.2458` n `12`; crypto_alt avg `1.7544` n `234`; crypto_major avg `1.0603` n `8`; equity avg `0.6361` n `141`; fx avg `-0.0576` n `6`; index avg `0.1418` n `26`; metal avg `0.2736` n `20`; unknown avg `4.0962` n `904`
- 24h: commodity avg `-0.1606` n `12`; crypto_alt avg `4.4549` n `234`; crypto_major avg `2.2613` n `8`; equity avg `2.1663` n `141`; fx avg `-0.244` n `6`; index avg `0.3365` n `26`; metal avg `0.1653` n `20`; unknown avg `17.5678` n `797`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1635`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
