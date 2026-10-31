# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T11:22:26.971553+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0046` n `13`; crypto_alt avg `0.2821` n `238`; crypto_major avg `0.0961` n `8`; equity avg `0.0233` n `156`; fx avg `0.0004` n `6`; index avg `0.0016` n `27`; metal avg `0.0021` n `20`; unknown avg `0.2714` n `1252`
- 1h: commodity avg `0.0491` n `13`; crypto_alt avg `0.1947` n `238`; crypto_major avg `0.0661` n `8`; equity avg `-0.0175` n `156`; fx avg `-0.005` n `6`; index avg `-0.0067` n `27`; metal avg `0.0006` n `20`; unknown avg `0.1592` n `1228`
- 4h: commodity avg `0.006` n `13`; crypto_alt avg `-0.0149` n `238`; crypto_major avg `-0.0226` n `8`; equity avg `-0.0578` n `156`; fx avg `0.012` n `6`; index avg `-0.0058` n `27`; metal avg `0.0114` n `20`; unknown avg `0.9599` n `1212`
- 24h: commodity avg `-0.2311` n `13`; crypto_alt avg `0.3596` n `238`; crypto_major avg `-0.957` n `8`; equity avg `-1.399` n `156`; fx avg `-0.0567` n `6`; index avg `-0.1299` n `27`; metal avg `-0.3237` n `20`; unknown avg `2.5541` n `1041`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1359`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
