# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T06:22:27.522401+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0165` n `12`; crypto_alt avg `0.1315` n `230`; crypto_major avg `0.131` n `8`; equity avg `-0.0211` n `96`; fx avg `-0.0016` n `6`; index avg `-0.0142` n `25`; metal avg `-0.0176` n `20`; unknown avg `-0.1044` n `769`
- 1h: commodity avg `0.0062` n `12`; crypto_alt avg `-0.0323` n `230`; crypto_major avg `-0.0632` n `8`; equity avg `-0.0823` n `96`; fx avg `-0.0112` n `6`; index avg `-0.0309` n `25`; metal avg `-0.0123` n `20`; unknown avg `-0.0137` n `737`
- 4h: commodity avg `-0.0698` n `12`; crypto_alt avg `-0.3366` n `230`; crypto_major avg `-0.2809` n `8`; equity avg `-0.1494` n `96`; fx avg `-0.0047` n `6`; index avg `0.0287` n `25`; metal avg `0.0084` n `20`; unknown avg `-0.0538` n `737`
- 24h: commodity avg `0.9179` n `12`; crypto_alt avg `-0.2032` n `230`; crypto_major avg `0.522` n `8`; equity avg `1.023` n `96`; fx avg `0.0271` n `6`; index avg `0.1405` n `25`; metal avg `0.1039` n `20`; unknown avg `0.2867` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
