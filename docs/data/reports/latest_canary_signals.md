# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T14:52:30.096648+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0931` n `12`; crypto_alt avg `0.06` n `230`; crypto_major avg `0.0949` n `8`; equity avg `0.0112` n `100`; fx avg `0.0017` n `6`; index avg `0.0097` n `25`; metal avg `0.0028` n `20`; unknown avg `-0.0048` n `775`
- 1h: commodity avg `-0.0953` n `12`; crypto_alt avg `0.1002` n `230`; crypto_major avg `0.1492` n `8`; equity avg `0.06` n `100`; fx avg `-0.0002` n `6`; index avg `0.0098` n `25`; metal avg `0.006` n `20`; unknown avg `0.2069` n `775`
- 4h: commodity avg `-0.0562` n `12`; crypto_alt avg `-0.0915` n `230`; crypto_major avg `0.0418` n `8`; equity avg `0.0965` n `100`; fx avg `0.0002` n `6`; index avg `0.0045` n `25`; metal avg `0.0265` n `20`; unknown avg `-0.0845` n `775`
- 24h: commodity avg `-0.5392` n `12`; crypto_alt avg `1.2436` n `230`; crypto_major avg `1.3985` n `8`; equity avg `0.808` n `100`; fx avg `0.0209` n `6`; index avg `0.1845` n `25`; metal avg `0.1732` n `20`; unknown avg `0.4445` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1908`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.181`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1619`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
