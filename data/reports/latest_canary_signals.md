# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T20:07:26.798575+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0026` n `12`; crypto_alt avg `-0.0492` n `232`; crypto_major avg `-0.0511` n `8`; equity avg `0.0066` n `134`; fx avg `-0.0031` n `6`; index avg `-0.0026` n `26`; metal avg `-0.001` n `20`; unknown avg `1.1075` n `781`
- 1h: commodity avg `-0.0172` n `12`; crypto_alt avg `-0.0345` n `232`; crypto_major avg `-0.1217` n `8`; equity avg `0.0341` n `134`; fx avg `-0.0034` n `6`; index avg `-0.0012` n `26`; metal avg `-0.0021` n `20`; unknown avg `1.0119` n `781`
- 4h: commodity avg `-0.0277` n `12`; crypto_alt avg `0.1999` n `232`; crypto_major avg `0.0656` n `8`; equity avg `0.2194` n `134`; fx avg `-0.0003` n `6`; index avg `0.0172` n `26`; metal avg `0.0107` n `20`; unknown avg `0.9745` n `755`
- 24h: commodity avg `0.0218` n `12`; crypto_alt avg `0.9856` n `232`; crypto_major avg `-0.1311` n `8`; equity avg `0.3261` n `134`; fx avg `-0.0008` n `6`; index avg `-0.0027` n `26`; metal avg `-0.0241` n `20`; unknown avg `105.2084` n `672`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1654`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
