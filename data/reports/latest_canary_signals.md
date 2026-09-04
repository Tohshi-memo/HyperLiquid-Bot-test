# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T09:37:29.832412+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.025` n `12`; crypto_alt avg `0.1052` n `232`; crypto_major avg `0.1705` n `8`; equity avg `0.0312` n `133`; fx avg `0.009` n `6`; index avg `0.0014` n `26`; metal avg `0.0108` n `20`; unknown avg `0.0188` n `793`
- 1h: commodity avg `-0.0068` n `12`; crypto_alt avg `0.7428` n `232`; crypto_major avg `0.4908` n `8`; equity avg `-0.0384` n `133`; fx avg `0.021` n `6`; index avg `-0.0043` n `26`; metal avg `-0.146` n `20`; unknown avg `1.889` n `791`
- 4h: commodity avg `-0.0846` n `12`; crypto_alt avg `0.9968` n `232`; crypto_major avg `0.508` n `8`; equity avg `0.06` n `133`; fx avg `-0.011` n `6`; index avg `-0.0335` n `26`; metal avg `-0.0103` n `20`; unknown avg `2.598` n `749`
- 24h: commodity avg `-0.3447` n `12`; crypto_alt avg `2.8374` n `232`; crypto_major avg `4.5332` n `8`; equity avg `2.102` n `133`; fx avg `-0.0038` n `6`; index avg `3.7206` n `26`; metal avg `0.4132` n `20`; unknown avg `3.3008` n `730`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
