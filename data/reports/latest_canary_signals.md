# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T05:37:30.589987+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0069` n `12`; crypto_alt avg `0.1222` n `229`; crypto_major avg `0.1207` n `8`; equity avg `0.0618` n `88`; fx avg `0.0015` n `6`; index avg `0.0072` n `25`; metal avg `0.0068` n `20`; unknown avg `0.0291` n `765`
- 1h: commodity avg `0.0026` n `12`; crypto_alt avg `-0.176` n `229`; crypto_major avg `-0.3407` n `8`; equity avg `0.0152` n `88`; fx avg `0.0015` n `6`; index avg `-0.0037` n `25`; metal avg `-0.0021` n `20`; unknown avg `0.4048` n `765`
- 4h: commodity avg `-0.0312` n `12`; crypto_alt avg `0.3918` n `229`; crypto_major avg `0.5811` n `8`; equity avg `0.2606` n `88`; fx avg `0.0129` n `6`; index avg `0.0187` n `25`; metal avg `0.0249` n `20`; unknown avg `0.9827` n `763`
- 24h: commodity avg `-0.1232` n `12`; crypto_alt avg `2.0251` n `229`; crypto_major avg `2.4594` n `8`; equity avg `0.5243` n `88`; fx avg `-0.1652` n `6`; index avg `0.0212` n `25`; metal avg `-0.1316` n `20`; unknown avg `4.3013` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.052`, n `668`, weak_sample_signal
