# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T22:07:29.472114+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0414` n `12`; crypto_alt avg `0.0789` n `230`; crypto_major avg `0.0371` n `8`; equity avg `0.029` n `120`; fx avg `0.0016` n `6`; index avg `0.0149` n `25`; metal avg `-0.0135` n `20`; unknown avg `2.3141` n `789`
- 1h: commodity avg `0.0185` n `12`; crypto_alt avg `0.0059` n `230`; crypto_major avg `-0.0376` n `8`; equity avg `-0.0445` n `120`; fx avg `0.0034` n `6`; index avg `0.0036` n `25`; metal avg `-0.0088` n `20`; unknown avg `0.1265` n `789`
- 4h: commodity avg `0.1275` n `12`; crypto_alt avg `-0.2947` n `230`; crypto_major avg `-0.0552` n `8`; equity avg `-0.0779` n `120`; fx avg `-0.0034` n `6`; index avg `-0.0005` n `25`; metal avg `-0.1029` n `20`; unknown avg `0.0072` n `789`
- 24h: commodity avg `0.2649` n `12`; crypto_alt avg `-0.7462` n `230`; crypto_major avg `0.1314` n `8`; equity avg `-4.608` n `120`; fx avg `-0.0598` n `6`; index avg `-0.7104` n `25`; metal avg `-0.7815` n `20`; unknown avg `-0.2345` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
