# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T01:52:25.816105+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0013` n `12`; crypto_alt avg `0.0446` n `229`; crypto_major avg `-0.0404` n `8`; equity avg `0.0213` n `88`; fx avg `0.0012` n `6`; index avg `0.0021` n `25`; metal avg `0.0043` n `20`; unknown avg `-0.0821` n `765`
- 1h: commodity avg `-0.0516` n `12`; crypto_alt avg `-0.5403` n `229`; crypto_major avg `-0.5932` n `8`; equity avg `-0.073` n `88`; fx avg `-0.0177` n `6`; index avg `0.0057` n `25`; metal avg `-0.0191` n `20`; unknown avg `0.7214` n `765`
- 4h: commodity avg `-0.0082` n `12`; crypto_alt avg `-0.9033` n `229`; crypto_major avg `-0.5854` n `8`; equity avg `-0.0265` n `88`; fx avg `-0.0162` n `6`; index avg `-0.0496` n `25`; metal avg `-0.0266` n `20`; unknown avg `0.1699` n `765`
- 24h: commodity avg `0.031` n `12`; crypto_alt avg `1.5357` n `229`; crypto_major avg `2.033` n `8`; equity avg `0.9017` n `88`; fx avg `-0.1373` n `6`; index avg `0.216` n `25`; metal avg `-0.0753` n `20`; unknown avg `3.9346` n `739`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
