# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T14:07:29.768254+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0764` n `12`; crypto_alt avg `-0.0349` n `230`; crypto_major avg `-0.2529` n `8`; equity avg `-0.0617` n `98`; fx avg `0.0088` n `6`; index avg `-0.031` n `25`; metal avg `-0.0696` n `20`; unknown avg `0.0756` n `770`
- 1h: commodity avg `-0.0157` n `12`; crypto_alt avg `-0.2764` n `230`; crypto_major avg `-0.5029` n `8`; equity avg `-0.4365` n `98`; fx avg `-0.0141` n `6`; index avg `0.0018` n `25`; metal avg `0.0066` n `20`; unknown avg `0.3189` n `770`
- 4h: commodity avg `0.082` n `12`; crypto_alt avg `0.1724` n `230`; crypto_major avg `0.1189` n `8`; equity avg `0.0749` n `98`; fx avg `-0.0343` n `6`; index avg `0.0839` n `25`; metal avg `-0.0935` n `20`; unknown avg `0.5018` n `770`
- 24h: commodity avg `-0.4925` n `12`; crypto_alt avg `0.3252` n `230`; crypto_major avg `-0.2811` n `8`; equity avg `0.4793` n `97`; fx avg `-0.0759` n `6`; index avg `0.1906` n `25`; metal avg `0.1294` n `20`; unknown avg `-0.0039` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.111`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1105`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.102`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0894`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0783`, n `666`, weak_sample_signal
