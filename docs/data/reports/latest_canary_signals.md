# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T09:07:25.866181+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0239` n `12`; crypto_alt avg `-0.1507` n `230`; crypto_major avg `-0.0814` n `8`; equity avg `0.008` n `96`; fx avg `-0.0016` n `6`; index avg `0.0107` n `25`; metal avg `-0.001` n `20`; unknown avg `-0.0156` n `769`
- 1h: commodity avg `0.0395` n `12`; crypto_alt avg `-0.1364` n `230`; crypto_major avg `-0.0462` n `8`; equity avg `-0.0217` n `96`; fx avg `-0.0037` n `6`; index avg `0.0522` n `25`; metal avg `-0.0035` n `20`; unknown avg `0.0281` n `769`
- 4h: commodity avg `0.0778` n `12`; crypto_alt avg `-0.3678` n `230`; crypto_major avg `-0.1011` n `8`; equity avg `-0.1324` n `96`; fx avg `-0.0019` n `6`; index avg `0.0317` n `25`; metal avg `0.0149` n `20`; unknown avg `-0.0657` n `737`
- 24h: commodity avg `0.7451` n `12`; crypto_alt avg `-0.3732` n `230`; crypto_major avg `0.4323` n `8`; equity avg `1.6564` n `96`; fx avg `0.0183` n `6`; index avg `0.2986` n `25`; metal avg `0.2301` n `20`; unknown avg `0.301` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
