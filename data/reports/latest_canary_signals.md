# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T02:32:32.401363+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0576` n `13`; crypto_alt avg `-0.1027` n `238`; crypto_major avg `-0.1215` n `8`; equity avg `0.0147` n `156`; fx avg `0.0` n `6`; index avg `-0.0007` n `27`; metal avg `-0.0145` n `20`; unknown avg `0.1293` n `1258`
- 1h: commodity avg `0.1056` n `13`; crypto_alt avg `-0.4765` n `238`; crypto_major avg `-0.2679` n `8`; equity avg `-0.0559` n `156`; fx avg `0.007` n `6`; index avg `-0.0075` n `27`; metal avg `-0.0263` n `20`; unknown avg `-0.198` n `1254`
- 4h: commodity avg `-0.0047` n `13`; crypto_alt avg `0.0045` n `238`; crypto_major avg `0.3773` n `8`; equity avg `0.1686` n `156`; fx avg `0.0061` n `6`; index avg `0.0095` n `27`; metal avg `-0.0141` n `20`; unknown avg `0.061` n `1245`
- 24h: commodity avg `-0.0942` n `13`; crypto_alt avg `3.2107` n `238`; crypto_major avg `0.2324` n `8`; equity avg `-2.1461` n `156`; fx avg `-0.1403` n `6`; index avg `-0.0947` n `27`; metal avg `-0.7069` n `20`; unknown avg `-0.9142` n `1016`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1536`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
