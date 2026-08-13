# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T23:07:24.786709+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0073` n `12`; crypto_alt avg `-0.0305` n `230`; crypto_major avg `-0.1162` n `8`; equity avg `-0.0248` n `113`; fx avg `0.0001` n `6`; index avg `-0.0078` n `25`; metal avg `-0.0109` n `20`; unknown avg `-0.1077` n `787`
- 1h: commodity avg `-0.0032` n `12`; crypto_alt avg `-0.0457` n `230`; crypto_major avg `-0.1056` n `8`; equity avg `0.01` n `113`; fx avg `0.0023` n `6`; index avg `-0.0019` n `25`; metal avg `0.008` n `20`; unknown avg `0.1756` n `787`
- 4h: commodity avg `0.0155` n `12`; crypto_alt avg `0.1461` n `230`; crypto_major avg `-0.1425` n `8`; equity avg `-0.099` n `113`; fx avg `0.0098` n `6`; index avg `-0.0078` n `25`; metal avg `-0.0591` n `20`; unknown avg `-0.0492` n `787`
- 24h: commodity avg `-0.4544` n `12`; crypto_alt avg `0.7529` n `230`; crypto_major avg `0.7549` n `8`; equity avg `1.7032` n `113`; fx avg `0.0176` n `6`; index avg `0.3343` n `25`; metal avg `-0.4531` n `20`; unknown avg `0.158` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2434`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2067`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2001`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1898`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1697`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1682`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1584`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1527`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1493`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1487`, n `668`, weak_sample_signal
