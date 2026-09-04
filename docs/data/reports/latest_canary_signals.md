# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T10:37:35.468762+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0184` n `12`; crypto_alt avg `0.168` n `232`; crypto_major avg `0.2653` n `8`; equity avg `0.0778` n `133`; fx avg `-0.0027` n `6`; index avg `0.0132` n `26`; metal avg `0.0089` n `20`; unknown avg `0.133` n `793`
- 1h: commodity avg `0.0121` n `12`; crypto_alt avg `-0.3229` n `232`; crypto_major avg `-0.2559` n `8`; equity avg `0.1807` n `133`; fx avg `-0.0284` n `6`; index avg `0.0385` n `26`; metal avg `0.0112` n `20`; unknown avg `-0.1195` n `791`
- 4h: commodity avg `-0.0427` n `12`; crypto_alt avg `1.0795` n `232`; crypto_major avg `0.656` n `8`; equity avg `0.5233` n `133`; fx avg `-0.0009` n `6`; index avg `0.0552` n `26`; metal avg `0.0822` n `20`; unknown avg `0.1431` n `785`
- 24h: commodity avg `-0.5635` n `12`; crypto_alt avg `2.8196` n `232`; crypto_major avg `4.5802` n `8`; equity avg `2.5334` n `133`; fx avg `-0.0297` n `6`; index avg `0.4669` n `26`; metal avg `0.534` n `20`; unknown avg `2.1457` n `730`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
