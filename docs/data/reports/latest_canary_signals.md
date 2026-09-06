# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T05:37:28.790625+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0079` n `12`; crypto_alt avg `0.1697` n `232`; crypto_major avg `0.3235` n `8`; equity avg `0.0376` n `134`; fx avg `0.0145` n `6`; index avg `-0.0` n `26`; metal avg `0.0026` n `20`; unknown avg `31.9879` n `792`
- 1h: commodity avg `0.0108` n `12`; crypto_alt avg `0.5471` n `232`; crypto_major avg `0.4926` n `8`; equity avg `0.0413` n `134`; fx avg `0.0327` n `6`; index avg `-0.006` n `26`; metal avg `0.0071` n `20`; unknown avg `0.8243` n `782`
- 4h: commodity avg `-0.011` n `12`; crypto_alt avg `0.2026` n `232`; crypto_major avg `0.6821` n `8`; equity avg `0.0613` n `134`; fx avg `0.0373` n `6`; index avg `0.014` n `26`; metal avg `-0.0019` n `20`; unknown avg `449.0268` n `746`
- 24h: commodity avg `0.1127` n `12`; crypto_alt avg `3.0844` n `232`; crypto_major avg `3.3676` n `8`; equity avg `0.4124` n `134`; fx avg `-0.023` n `6`; index avg `0.0945` n `26`; metal avg `-0.0216` n `20`; unknown avg `494.0016` n `676`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
