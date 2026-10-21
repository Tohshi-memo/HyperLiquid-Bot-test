# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-21T03:52:26.616210+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.034` n `13`; crypto_alt avg `0.0294` n `237`; crypto_major avg `-0.0462` n `8`; equity avg `-0.0404` n `151`; fx avg `-0.0109` n `6`; index avg `-0.0013` n `26`; metal avg `-0.0123` n `20`; unknown avg `0.0483` n `1200`
- 1h: commodity avg `-0.0272` n `13`; crypto_alt avg `-0.0971` n `237`; crypto_major avg `-0.1809` n `8`; equity avg `-0.0972` n `151`; fx avg `-0.0426` n `6`; index avg `-0.0426` n `26`; metal avg `-0.004` n `20`; unknown avg `1.5835` n `1198`
- 4h: commodity avg `0.1178` n `13`; crypto_alt avg `0.2909` n `237`; crypto_major avg `-0.0531` n `8`; equity avg `0.0515` n `151`; fx avg `0.0034` n `6`; index avg `-0.0137` n `26`; metal avg `-0.0977` n `20`; unknown avg `0.6273` n `1191`
- 24h: commodity avg `0.0092` n `13`; crypto_alt avg `2.1798` n `237`; crypto_major avg `1.43` n `8`; equity avg `2.0537` n `151`; fx avg `-0.0019` n `6`; index avg `0.2894` n `26`; metal avg `-0.1604` n `20`; unknown avg `212.8187` n `988`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1688`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
