# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T03:37:24.382953+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0461` n `13`; crypto_alt avg `0.2475` n `237`; crypto_major avg `0.1233` n `8`; equity avg `0.0248` n `151`; fx avg `0.0053` n `6`; index avg `0.0063` n `26`; metal avg `0.0164` n `20`; unknown avg `0.0273` n `1198`
- 1h: commodity avg `0.074` n `13`; crypto_alt avg `0.5922` n `237`; crypto_major avg `0.4083` n `8`; equity avg `0.0799` n `151`; fx avg `0.0056` n `6`; index avg `0.009` n `26`; metal avg `0.1021` n `20`; unknown avg `9.6155` n `1196`
- 4h: commodity avg `0.1135` n `13`; crypto_alt avg `0.1077` n `237`; crypto_major avg `-0.1659` n `8`; equity avg `-0.4803` n `151`; fx avg `-0.0072` n `6`; index avg `-0.1281` n `26`; metal avg `0.119` n `20`; unknown avg `7.901` n `1190`
- 24h: commodity avg `0.3153` n `13`; crypto_alt avg `0.4338` n `237`; crypto_major avg `-0.2921` n `8`; equity avg `-0.8175` n `151`; fx avg `-0.0203` n `6`; index avg `-0.1378` n `26`; metal avg `-0.2152` n `20`; unknown avg `5.0609` n `1012`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1881`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1351`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
