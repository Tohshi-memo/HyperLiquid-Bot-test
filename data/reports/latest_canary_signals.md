# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T02:37:27.127868+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.058` n `13`; crypto_alt avg `-0.0815` n `238`; crypto_major avg `-0.0586` n `8`; equity avg `0.001` n `156`; fx avg `0.0` n `6`; index avg `-0.0007` n `27`; metal avg `-0.0212` n `20`; unknown avg `0.0702` n `1258`
- 1h: commodity avg `0.1051` n `13`; crypto_alt avg `-0.4555` n `238`; crypto_major avg `-0.2051` n `8`; equity avg `-0.0696` n `156`; fx avg `0.007` n `6`; index avg `-0.0075` n `27`; metal avg `-0.033` n `20`; unknown avg `0.0024` n `1252`
- 4h: commodity avg `-0.0051` n `13`; crypto_alt avg `0.0256` n `238`; crypto_major avg `0.4406` n `8`; equity avg `0.1548` n `156`; fx avg `0.0061` n `6`; index avg `0.0095` n `27`; metal avg `-0.0208` n `20`; unknown avg `0.2143` n `1245`
- 24h: commodity avg `-0.0946` n `13`; crypto_alt avg `3.2329` n `238`; crypto_major avg `0.2956` n `8`; equity avg `-2.1596` n `156`; fx avg `-0.1403` n `6`; index avg `-0.0947` n `27`; metal avg `-0.7134` n `20`; unknown avg `-0.699` n `1014`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1537`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
