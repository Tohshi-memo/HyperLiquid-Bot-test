# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-21T07:22:29.605784+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0714` n `13`; crypto_alt avg `0.3471` n `237`; crypto_major avg `0.2153` n `8`; equity avg `0.1771` n `151`; fx avg `0.001` n `6`; index avg `0.0214` n `26`; metal avg `0.0312` n `20`; unknown avg `2.5223` n `1200`
- 1h: commodity avg `-0.1132` n `13`; crypto_alt avg `0.4944` n `237`; crypto_major avg `0.3287` n `8`; equity avg `-0.0216` n `151`; fx avg `0.0012` n `6`; index avg `0.0066` n `26`; metal avg `0.0459` n `20`; unknown avg `2.8842` n `1192`
- 4h: commodity avg `-0.1594` n `13`; crypto_alt avg `0.4735` n `237`; crypto_major avg `0.1483` n `8`; equity avg `-0.272` n `151`; fx avg `-0.0511` n `6`; index avg `-0.0737` n `26`; metal avg `-0.0908` n `20`; unknown avg `1.7784` n `1168`
- 24h: commodity avg `-0.1801` n `13`; crypto_alt avg `3.0786` n `237`; crypto_major avg `2.0791` n `8`; equity avg `2.4759` n `151`; fx avg `0.0037` n `6`; index avg `0.3153` n `26`; metal avg `-0.228` n `20`; unknown avg `5293.0273` n `986`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1656`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
