# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T19:22:27.181789+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0338` n `12`; crypto_alt avg `-0.048` n `231`; crypto_major avg `0.044` n `8`; equity avg `-0.0136` n `122`; fx avg `-0.0048` n `6`; index avg `-0.0093` n `25`; metal avg `-0.0043` n `20`; unknown avg `-0.0008` n `797`
- 1h: commodity avg `0.0346` n `12`; crypto_alt avg `-0.0856` n `231`; crypto_major avg `-0.0941` n `8`; equity avg `0.1594` n `122`; fx avg `-0.0103` n `6`; index avg `0.0457` n `25`; metal avg `-0.0239` n `20`; unknown avg `-0.1211` n `797`
- 4h: commodity avg `0.018` n `12`; crypto_alt avg `0.2816` n `231`; crypto_major avg `0.4214` n `8`; equity avg `0.3371` n `122`; fx avg `-0.0035` n `6`; index avg `0.0392` n `25`; metal avg `-0.1303` n `20`; unknown avg `0.1092` n `797`
- 24h: commodity avg `0.0967` n `12`; crypto_alt avg `-1.797` n `231`; crypto_major avg `-1.9627` n `8`; equity avg `0.0364` n `122`; fx avg `-0.0586` n `6`; index avg `0.0763` n `25`; metal avg `-0.4336` n `20`; unknown avg `0.4166` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1483`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
