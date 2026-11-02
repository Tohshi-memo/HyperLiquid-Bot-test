# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T04:07:30.413961+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0601` n `13`; crypto_alt avg `-0.1442` n `238`; crypto_major avg `0.0061` n `8`; equity avg `0.0375` n `156`; fx avg `-0.0093` n `6`; index avg `0.0136` n `27`; metal avg `0.0355` n `20`; unknown avg `0.8258` n `1249`
- 1h: commodity avg `-0.06` n `13`; crypto_alt avg `0.1641` n `238`; crypto_major avg `0.3305` n `8`; equity avg `0.5986` n `156`; fx avg `0.0168` n `6`; index avg `0.0872` n `27`; metal avg `0.0415` n `20`; unknown avg `1.8227` n `1201`
- 4h: commodity avg `-0.455` n `13`; crypto_alt avg `0.1451` n `238`; crypto_major avg `0.6329` n `8`; equity avg `1.1469` n `156`; fx avg `0.1764` n `6`; index avg `0.2378` n `27`; metal avg `-0.0825` n `20`; unknown avg `3.4812` n `1193`
- 24h: commodity avg `-0.4596` n `13`; crypto_alt avg `-0.2412` n `238`; crypto_major avg `0.9524` n `8`; equity avg `1.6417` n `156`; fx avg `0.204` n `6`; index avg `0.3611` n `27`; metal avg `0.0894` n `20`; unknown avg `3.3993` n `1074`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.184`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1788`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1419`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1355`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
