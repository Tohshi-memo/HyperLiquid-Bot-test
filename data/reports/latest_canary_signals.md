# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T21:07:27.095783+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0688` n `12`; crypto_alt avg `0.1599` n `230`; crypto_major avg `0.1695` n `8`; equity avg `-0.0162` n `96`; fx avg `-0.0031` n `6`; index avg `0.0039` n `25`; metal avg `0.0003` n `20`; unknown avg `-0.0368` n `769`
- 1h: commodity avg `0.0906` n `12`; crypto_alt avg `0.0291` n `230`; crypto_major avg `0.1505` n `8`; equity avg `0.0279` n `96`; fx avg `-0.0258` n `6`; index avg `-0.0034` n `25`; metal avg `-0.0128` n `20`; unknown avg `-0.0634` n `769`
- 4h: commodity avg `0.1639` n `12`; crypto_alt avg `-0.4457` n `230`; crypto_major avg `-0.0606` n `8`; equity avg `-1.4132` n `96`; fx avg `-0.0512` n `6`; index avg `-0.2425` n `25`; metal avg `-0.0664` n `20`; unknown avg `0.0035` n `769`
- 24h: commodity avg `0.6806` n `12`; crypto_alt avg `-1.3223` n `230`; crypto_major avg `-1.2139` n `8`; equity avg `-1.4624` n `94`; fx avg `0.0663` n `6`; index avg `-0.3117` n `25`; metal avg `-0.0039` n `20`; unknown avg `-0.0673` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
