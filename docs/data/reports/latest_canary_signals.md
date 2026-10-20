# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T22:07:30.543661+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0161` n `13`; crypto_alt avg `0.0881` n `237`; crypto_major avg `0.1425` n `8`; equity avg `0.2607` n `151`; fx avg `0.0059` n `6`; index avg `0.0326` n `26`; metal avg `0.0039` n `20`; unknown avg `-0.1639` n `1197`
- 1h: commodity avg `-0.0005` n `13`; crypto_alt avg `0.0858` n `237`; crypto_major avg `0.2087` n `8`; equity avg `0.3719` n `151`; fx avg `0.0283` n `6`; index avg `0.0532` n `26`; metal avg `0.0051` n `20`; unknown avg `-0.0458` n `1163`
- 4h: commodity avg `0.1538` n `13`; crypto_alt avg `0.581` n `237`; crypto_major avg `0.6963` n `8`; equity avg `1.3316` n `151`; fx avg `0.0117` n `6`; index avg `0.1567` n `26`; metal avg `0.0098` n `20`; unknown avg `0.1653` n `1101`
- 24h: commodity avg `-0.0056` n `13`; crypto_alt avg `2.7082` n `237`; crypto_major avg `1.758` n `8`; equity avg `1.4685` n `151`; fx avg `0.0212` n `6`; index avg `0.1559` n `26`; metal avg `0.0706` n `20`; unknown avg `197.3765` n `1058`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1717`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
