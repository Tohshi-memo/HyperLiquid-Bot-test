# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T10:52:26.277506+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0206` n `12`; crypto_alt avg `0.0624` n `232`; crypto_major avg `0.0112` n `8`; equity avg `0.0118` n `134`; fx avg `-0.0038` n `6`; index avg `0.0069` n `26`; metal avg `0.002` n `20`; unknown avg `0.0661` n `790`
- 1h: commodity avg `-0.0025` n `12`; crypto_alt avg `-0.0133` n `232`; crypto_major avg `-0.0003` n `8`; equity avg `0.0304` n `134`; fx avg `0.0002` n `6`; index avg `0.015` n `26`; metal avg `0.0024` n `20`; unknown avg `-0.0836` n `788`
- 4h: commodity avg `-0.0174` n `12`; crypto_alt avg `0.3376` n `232`; crypto_major avg `0.6481` n `8`; equity avg `0.0387` n `134`; fx avg `-0.0121` n `6`; index avg `0.0181` n `26`; metal avg `-0.0078` n `20`; unknown avg `-0.0856` n `780`
- 24h: commodity avg `0.2137` n `12`; crypto_alt avg `0.7728` n `232`; crypto_major avg `-1.145` n `8`; equity avg `0.813` n `134`; fx avg `-0.1158` n `6`; index avg `0.0476` n `26`; metal avg `-0.1461` n `20`; unknown avg `16.4523` n `648`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1682`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
