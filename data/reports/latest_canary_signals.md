# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T01:22:22.412910+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.006` n `12`; crypto_alt avg `0.1353` n `234`; crypto_major avg `0.1805` n `8`; equity avg `0.0533` n `137`; fx avg `0.0064` n `6`; index avg `0.0171` n `27`; metal avg `0.077` n `20`; unknown avg `0.1595` n `919`
- 1h: commodity avg `0.0372` n `12`; crypto_alt avg `-0.1891` n `234`; crypto_major avg `0.1143` n `8`; equity avg `-0.0748` n `137`; fx avg `0.0697` n `6`; index avg `-0.0037` n `27`; metal avg `0.0392` n `20`; unknown avg `0.067` n `911`
- 4h: commodity avg `-0.0626` n `12`; crypto_alt avg `-0.2158` n `234`; crypto_major avg `0.2115` n `8`; equity avg `-0.0127` n `137`; fx avg `0.1218` n `6`; index avg `0.0137` n `27`; metal avg `0.0229` n `20`; unknown avg `0.2121` n `863`
- 24h: commodity avg `0.3903` n `12`; crypto_alt avg `-3.9156` n `234`; crypto_major avg `-3.8601` n `8`; equity avg `-1.6293` n `137`; fx avg `0.301` n `6`; index avg `-0.171` n `27`; metal avg `0.1535` n `20`; unknown avg `0.9527` n `802`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
