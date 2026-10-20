# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T10:52:32.614204+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0369` n `13`; crypto_alt avg `-0.0493` n `237`; crypto_major avg `-0.0557` n `8`; equity avg `-0.0965` n `151`; fx avg `-0.0068` n `6`; index avg `-0.02` n `26`; metal avg `-0.0035` n `20`; unknown avg `0.0674` n `1198`
- 1h: commodity avg `0.0085` n `13`; crypto_alt avg `0.1059` n `237`; crypto_major avg `0.083` n `8`; equity avg `-0.0973` n `151`; fx avg `-0.0098` n `6`; index avg `-0.003` n `26`; metal avg `0.0256` n `20`; unknown avg `5.0503` n `1196`
- 4h: commodity avg `0.2909` n `13`; crypto_alt avg `-0.625` n `237`; crypto_major avg `-0.4684` n `8`; equity avg `-0.7736` n `151`; fx avg `-0.0296` n `6`; index avg `-0.1437` n `26`; metal avg `-0.1331` n `20`; unknown avg `0.7556` n `1180`
- 24h: commodity avg `0.2523` n `13`; crypto_alt avg `0.0634` n `237`; crypto_major avg `-0.7065` n `8`; equity avg `-2.2931` n `151`; fx avg `-0.0021` n `6`; index avg `-0.3435` n `26`; metal avg `-0.2754` n `20`; unknown avg `0.538` n `1041`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1893`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1447`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
