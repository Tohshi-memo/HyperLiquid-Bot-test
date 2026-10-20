# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T16:37:29.011315+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0243` n `13`; crypto_alt avg `0.3708` n `237`; crypto_major avg `0.3699` n `8`; equity avg `0.3027` n `151`; fx avg `0.0108` n `6`; index avg `0.0695` n `26`; metal avg `0.0394` n `20`; unknown avg `0.0063` n `1199`
- 1h: commodity avg `0.0372` n `13`; crypto_alt avg `0.4963` n `237`; crypto_major avg `0.3898` n `8`; equity avg `0.3839` n `151`; fx avg `0.0091` n `6`; index avg `0.0604` n `26`; metal avg `-0.0118` n `20`; unknown avg `-0.5449` n `1191`
- 4h: commodity avg `-0.4887` n `13`; crypto_alt avg `2.0637` n `237`; crypto_major avg `1.3979` n `8`; equity avg `2.2209` n `151`; fx avg `0.0503` n `6`; index avg `0.3558` n `26`; metal avg `0.2403` n `20`; unknown avg `3.199` n `1100`
- 24h: commodity avg `-0.4283` n `13`; crypto_alt avg `2.086` n `237`; crypto_major avg `1.2995` n `8`; equity avg `-0.0717` n `151`; fx avg `0.0338` n `6`; index avg `-0.0069` n `26`; metal avg `0.0144` n `20`; unknown avg `3.8669` n `1044`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1793`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
