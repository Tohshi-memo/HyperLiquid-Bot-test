# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T11:07:25.314446+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.004` n `12`; crypto_alt avg `0.0224` n `229`; crypto_major avg `-0.0378` n `8`; equity avg `-0.0509` n `88`; fx avg `0.0255` n `6`; index avg `0.0005` n `25`; metal avg `0.0015` n `20`; unknown avg `-0.0037` n `765`
- 1h: commodity avg `0.0168` n `12`; crypto_alt avg `0.1761` n `229`; crypto_major avg `-0.0968` n `8`; equity avg `-0.0162` n `88`; fx avg `-0.0014` n `6`; index avg `0.0068` n `25`; metal avg `0.0026` n `20`; unknown avg `-0.0179` n `765`
- 4h: commodity avg `0.1092` n `12`; crypto_alt avg `-0.1042` n `229`; crypto_major avg `-0.0576` n `8`; equity avg `-0.0265` n `88`; fx avg `-0.0203` n `6`; index avg `0.0079` n `25`; metal avg `0.0291` n `20`; unknown avg `0.531` n `765`
- 24h: commodity avg `0.0415` n `12`; crypto_alt avg `0.5557` n `229`; crypto_major avg `1.1096` n `8`; equity avg `0.1286` n `88`; fx avg `-0.0739` n `6`; index avg `-0.0194` n `25`; metal avg `-0.0639` n `20`; unknown avg `3.1591` n `743`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
