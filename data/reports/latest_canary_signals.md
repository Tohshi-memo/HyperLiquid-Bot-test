# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T01:07:24.708278+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.77` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0037` n `12`; crypto_alt avg `-0.4683` n `229`; crypto_major avg `-0.3905` n `8`; equity avg `-0.0879` n `88`; fx avg `0.005` n `6`; index avg `0.0007` n `25`; metal avg `-0.0105` n `20`; unknown avg `-0.0141` n `765`
- 1h: commodity avg `0.0371` n `12`; crypto_alt avg `-0.81` n `229`; crypto_major avg `-0.4244` n `8`; equity avg `0.0163` n `88`; fx avg `0.0207` n `6`; index avg `-0.0361` n `25`; metal avg `-0.0403` n `20`; unknown avg `-0.2717` n `765`
- 4h: commodity avg `0.0864` n `12`; crypto_alt avg `-0.7809` n `229`; crypto_major avg `-0.4635` n `8`; equity avg `0.0028` n `88`; fx avg `0.0059` n `6`; index avg `-0.0616` n `25`; metal avg `-0.0179` n `20`; unknown avg `-0.2697` n `765`
- 24h: commodity avg `0.1606` n `12`; crypto_alt avg `2.2537` n `229`; crypto_major avg `2.8931` n `8`; equity avg `1.4266` n `88`; fx avg `-0.1282` n `6`; index avg `0.3101` n `25`; metal avg `0.0405` n `20`; unknown avg `2.002` n `739`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0526`, n `668`, weak_sample_signal
