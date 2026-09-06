# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T04:37:24.575917+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0117` n `12`; crypto_alt avg `0.0839` n `232`; crypto_major avg `0.0249` n `8`; equity avg `0.0094` n `134`; fx avg `-0.0043` n `6`; index avg `0.0039` n `26`; metal avg `-0.0023` n `20`; unknown avg `0.2427` n `786`
- 1h: commodity avg `-0.003` n `12`; crypto_alt avg `-0.3365` n `232`; crypto_major avg `-0.2661` n `8`; equity avg `-0.0244` n `134`; fx avg `-0.0129` n `6`; index avg `0.017` n `26`; metal avg `-0.0106` n `20`; unknown avg `0.2264` n `752`
- 4h: commodity avg `-0.0012` n `12`; crypto_alt avg `0.1448` n `232`; crypto_major avg `0.4636` n `8`; equity avg `0.0814` n `134`; fx avg `-0.0055` n `6`; index avg `0.0193` n `26`; metal avg `-0.0177` n `20`; unknown avg `1.1684` n `752`
- 24h: commodity avg `0.0938` n `12`; crypto_alt avg `2.8605` n `232`; crypto_major avg `2.9364` n `8`; equity avg `0.4763` n `134`; fx avg `-0.0667` n `6`; index avg `0.1204` n `26`; metal avg `0.0239` n `20`; unknown avg `1.2538` n `680`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
