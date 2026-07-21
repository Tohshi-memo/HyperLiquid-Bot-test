# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T15:52:27.142907+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0005` n `12`; crypto_alt avg `0.0318` n `230`; crypto_major avg `0.1814` n `8`; equity avg `0.018` n `98`; fx avg `-0.0052` n `6`; index avg `-0.0057` n `25`; metal avg `-0.0508` n `20`; unknown avg `0.0744` n `771`
- 1h: commodity avg `0.0653` n `12`; crypto_alt avg `0.0458` n `230`; crypto_major avg `-0.0431` n `8`; equity avg `0.3426` n `98`; fx avg `-0.0171` n `6`; index avg `0.073` n `25`; metal avg `0.0486` n `20`; unknown avg `0.0462` n `771`
- 4h: commodity avg `0.0867` n `12`; crypto_alt avg `-0.0112` n `230`; crypto_major avg `-0.0697` n `8`; equity avg `1.2773` n `98`; fx avg `-0.0119` n `6`; index avg `0.2106` n `25`; metal avg `0.0907` n `20`; unknown avg `0.1115` n `771`
- 24h: commodity avg `0.6482` n `12`; crypto_alt avg `1.0232` n `230`; crypto_major avg `1.0131` n `8`; equity avg `2.7571` n `98`; fx avg `0.0049` n `6`; index avg `0.4031` n `25`; metal avg `0.6198` n `20`; unknown avg `0.2038` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0868`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0563`, n `666`, weak_sample_signal
