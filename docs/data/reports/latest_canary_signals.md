# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T11:07:29.203406+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0241` n `12`; crypto_alt avg `0.0035` n `230`; crypto_major avg `0.013` n `8`; equity avg `-0.0112` n `96`; fx avg `-0.0039` n `6`; index avg `0.0073` n `25`; metal avg `0.0035` n `20`; unknown avg `-0.0115` n `770`
- 1h: commodity avg `0.0861` n `12`; crypto_alt avg `-0.0507` n `230`; crypto_major avg `0.0612` n `8`; equity avg `-0.005` n `96`; fx avg `-0.0051` n `6`; index avg `0.0027` n `25`; metal avg `0.0007` n `20`; unknown avg `-0.0217` n `769`
- 4h: commodity avg `0.1259` n `12`; crypto_alt avg `-0.1235` n `230`; crypto_major avg `0.0898` n `8`; equity avg `-0.0461` n `96`; fx avg `-0.0015` n `6`; index avg `0.0599` n `25`; metal avg `0.0207` n `20`; unknown avg `-0.144` n `769`
- 24h: commodity avg `0.7326` n `12`; crypto_alt avg `-0.5556` n `230`; crypto_major avg `0.1786` n `8`; equity avg `0.3897` n `96`; fx avg `0.0341` n `6`; index avg `0.1103` n `25`; metal avg `0.2815` n `20`; unknown avg `0.2692` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
