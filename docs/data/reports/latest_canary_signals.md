# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T09:52:27.659690+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0025` n `12`; crypto_alt avg `0.0933` n `232`; crypto_major avg `-0.1288` n `8`; equity avg `-0.0138` n `134`; fx avg `-0.0009` n `6`; index avg `0.0012` n `26`; metal avg `-0.0063` n `20`; unknown avg `-0.0512` n `794`
- 1h: commodity avg `0.0009` n `12`; crypto_alt avg `0.4133` n `232`; crypto_major avg `0.3274` n `8`; equity avg `0.0604` n `134`; fx avg `-0.0121` n `6`; index avg `0.0089` n `26`; metal avg `0.0132` n `20`; unknown avg `322.7416` n `792`
- 4h: commodity avg `0.0008` n `12`; crypto_alt avg `-0.2095` n `232`; crypto_major avg `-0.3296` n `8`; equity avg `0.0521` n `134`; fx avg `-0.0098` n `6`; index avg `0.0017` n `26`; metal avg `-0.006` n `20`; unknown avg `-0.2299` n `766`
- 24h: commodity avg `0.1629` n `12`; crypto_alt avg `1.8277` n `232`; crypto_major avg `2.0448` n `8`; equity avg `0.4589` n `134`; fx avg `-0.0285` n `6`; index avg `0.0888` n `26`; metal avg `0.019` n `20`; unknown avg `493.2958` n `676`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
