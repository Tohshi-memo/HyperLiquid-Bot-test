# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T20:55:22.245193+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0162` n `12`; crypto_alt avg `-0.1355` n `230`; crypto_major avg `-0.1296` n `8`; equity avg `-0.0887` n `120`; fx avg `-0.0035` n `6`; index avg `-0.0228` n `25`; metal avg `-0.0334` n `20`; unknown avg `0.4194` n `789`
- 1h: commodity avg `0.0789` n `12`; crypto_alt avg `-0.1737` n `230`; crypto_major avg `-0.1247` n `8`; equity avg `-0.0822` n `120`; fx avg `-0.0044` n `6`; index avg `-0.0373` n `25`; metal avg `-0.0389` n `20`; unknown avg `0.3237` n `789`
- 4h: commodity avg `0.1476` n `12`; crypto_alt avg `-0.4205` n `230`; crypto_major avg `-0.1997` n `8`; equity avg `-0.7467` n `120`; fx avg `-0.0002` n `6`; index avg `-0.1069` n `25`; metal avg `-0.2119` n `20`; unknown avg `-0.0261` n `789`
- 24h: commodity avg `0.2978` n `12`; crypto_alt avg `-0.7963` n `230`; crypto_major avg `0.1532` n `8`; equity avg `-4.3371` n `120`; fx avg `-0.0526` n `6`; index avg `-0.6823` n `25`; metal avg `-0.7922` n `20`; unknown avg `-0.2445` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
