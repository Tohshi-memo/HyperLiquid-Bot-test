# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T03:37:30.282138+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0531` n `12`; crypto_alt avg `0.0939` n `233`; crypto_major avg `0.0525` n `8`; equity avg `-0.0358` n `134`; fx avg `-0.0024` n `6`; index avg `0.0112` n `26`; metal avg `-0.0267` n `20`; unknown avg `0.2313` n `797`
- 1h: commodity avg `-0.0478` n `12`; crypto_alt avg `-0.2746` n `233`; crypto_major avg `-0.3782` n `8`; equity avg `-0.1542` n `134`; fx avg `-0.0491` n `6`; index avg `-0.0147` n `26`; metal avg `0.0561` n `20`; unknown avg `0.4245` n `791`
- 4h: commodity avg `-0.0514` n `12`; crypto_alt avg `-0.5023` n `233`; crypto_major avg `-0.1146` n `8`; equity avg `0.4279` n `134`; fx avg `-0.0184` n `6`; index avg `0.0994` n `26`; metal avg `0.1164` n `20`; unknown avg `-0.0044` n `785`
- 24h: commodity avg `0.0321` n `12`; crypto_alt avg `-0.8904` n `232`; crypto_major avg `0.3235` n `8`; equity avg `0.1344` n `134`; fx avg `0.0296` n `6`; index avg `-0.2037` n `26`; metal avg `-0.3589` n `20`; unknown avg `0.3037` n `681`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
