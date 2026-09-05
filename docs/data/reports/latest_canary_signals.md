# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T09:52:26.784506+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0145` n `12`; crypto_alt avg `0.0319` n `232`; crypto_major avg `-0.0355` n `8`; equity avg `-0.0089` n `134`; fx avg `-0.0057` n `6`; index avg `0.0013` n `26`; metal avg `-0.0038` n `20`; unknown avg `-0.0384` n `792`
- 1h: commodity avg `0.0024` n `12`; crypto_alt avg `0.2109` n `232`; crypto_major avg `0.0374` n `8`; equity avg `0.0361` n `134`; fx avg `-0.0015` n `6`; index avg `0.0086` n `26`; metal avg `0.0003` n `20`; unknown avg `0.086` n `788`
- 4h: commodity avg `-0.0262` n `12`; crypto_alt avg `0.909` n `232`; crypto_major avg `0.9588` n `8`; equity avg `0.0349` n `134`; fx avg `-0.0145` n `6`; index avg `0.0037` n `26`; metal avg `-0.0029` n `20`; unknown avg `6.466` n `744`
- 24h: commodity avg `0.117` n `12`; crypto_alt avg `0.6028` n `232`; crypto_major avg `-1.0695` n `8`; equity avg `0.8804` n `134`; fx avg `-0.1379` n `6`; index avg `0.0666` n `26`; metal avg `-0.1091` n `20`; unknown avg `16.5298` n `648`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1687`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
