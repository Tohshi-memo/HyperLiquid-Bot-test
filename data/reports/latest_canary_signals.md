# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T11:07:28.897674+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0115` n `12`; crypto_alt avg `-0.006` n `228`; crypto_major avg `0.0651` n `8`; equity avg `0.1454` n `88`; fx avg `-0.0126` n `6`; index avg `0.0439` n `23`; metal avg `0.022` n `20`; unknown avg `0.0069` n `765`
- 1h: commodity avg `-0.0394` n `12`; crypto_alt avg `0.0367` n `228`; crypto_major avg `0.067` n `8`; equity avg `0.2218` n `88`; fx avg `-0.0005` n `6`; index avg `0.0486` n `23`; metal avg `0.1214` n `20`; unknown avg `0.0551` n `765`
- 4h: commodity avg `0.2018` n `12`; crypto_alt avg `-0.4293` n `228`; crypto_major avg `-0.1901` n `8`; equity avg `-0.0097` n `88`; fx avg `0.004` n `6`; index avg `-0.0131` n `23`; metal avg `0.1134` n `20`; unknown avg `0.0324` n `765`
- 24h: commodity avg `0.1051` n `12`; crypto_alt avg `-0.7506` n `228`; crypto_major avg `0.4038` n `8`; equity avg `1.5177` n `88`; fx avg `0.1253` n `6`; index avg `0.1411` n `23`; metal avg `0.3749` n `20`; unknown avg `9.2567` n `734`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
