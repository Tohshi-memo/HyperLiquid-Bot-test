# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T09:22:29.750338+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0708` n `13`; crypto_alt avg `-0.0564` n `236`; crypto_major avg `-0.0691` n `8`; equity avg `0.0618` n `151`; fx avg `-0.0047` n `6`; index avg `0.0183` n `26`; metal avg `-0.0213` n `20`; unknown avg `-0.0418` n `1136`
- 1h: commodity avg `-0.1451` n `13`; crypto_alt avg `0.1885` n `236`; crypto_major avg `0.1487` n `8`; equity avg `0.0068` n `151`; fx avg `0.0241` n `6`; index avg `0.0122` n `26`; metal avg `0.0195` n `20`; unknown avg `1.0784` n `1132`
- 4h: commodity avg `-0.1263` n `13`; crypto_alt avg `0.2306` n `236`; crypto_major avg `0.1891` n `8`; equity avg `-0.5104` n `151`; fx avg `-0.0266` n `6`; index avg `-0.0697` n `26`; metal avg `0.0229` n `20`; unknown avg `0.0161` n `1048`
- 24h: commodity avg `-0.1481` n `13`; crypto_alt avg `3.9823` n `236`; crypto_major avg `2.0576` n `8`; equity avg `2.4048` n `151`; fx avg `-0.0031` n `6`; index avg `0.3296` n `26`; metal avg `0.3297` n `20`; unknown avg `27.2525` n `864`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.0968`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0944`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0922`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0867`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0751`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
