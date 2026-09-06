# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T05:52:24.347046+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.016` n `12`; crypto_alt avg `-0.0562` n `232`; crypto_major avg `-0.0222` n `8`; equity avg `0.0248` n `134`; fx avg `-0.0112` n `6`; index avg `0.0059` n `26`; metal avg `0.0081` n `20`; unknown avg `-0.089` n `792`
- 1h: commodity avg `0.031` n `12`; crypto_alt avg `0.3226` n `232`; crypto_major avg `0.3874` n `8`; equity avg `0.0711` n `134`; fx avg `0.0117` n `6`; index avg `0.018` n `26`; metal avg `0.0089` n `20`; unknown avg `0.372` n `782`
- 4h: commodity avg `0.0245` n `12`; crypto_alt avg `0.0043` n `232`; crypto_major avg `0.6926` n `8`; equity avg `0.0974` n `134`; fx avg `0.0261` n `6`; index avg `0.0291` n `26`; metal avg `0.001` n `20`; unknown avg `449.7356` n `746`
- 24h: commodity avg `0.1358` n `12`; crypto_alt avg `2.9914` n `232`; crypto_major avg `3.3769` n `8`; equity avg `0.4421` n `134`; fx avg `-0.0331` n `6`; index avg `0.0907` n `26`; metal avg `0.0221` n `20`; unknown avg `494.3359` n `676`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1581`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
