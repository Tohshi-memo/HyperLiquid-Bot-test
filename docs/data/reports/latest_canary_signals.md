# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T19:37:14.521344+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0417` n `12`; crypto_alt avg `0.1075` n `230`; crypto_major avg `0.261` n `8`; equity avg `0.3336` n `96`; fx avg `0.0054` n `6`; index avg `0.0575` n `25`; metal avg `0.0461` n `20`; unknown avg `-0.1219` n `769`
- 1h: commodity avg `-0.0948` n `12`; crypto_alt avg `-0.1561` n `230`; crypto_major avg `0.1498` n `8`; equity avg `-0.1291` n `96`; fx avg `0.0115` n `6`; index avg `-0.0192` n `25`; metal avg `-0.0301` n `20`; unknown avg `-0.1524` n `769`
- 4h: commodity avg `0.1809` n `12`; crypto_alt avg `0.2425` n `230`; crypto_major avg `0.6307` n `8`; equity avg `0.6128` n `96`; fx avg `0.0274` n `6`; index avg `0.0203` n `25`; metal avg `0.0009` n `20`; unknown avg `0.5066` n `769`
- 24h: commodity avg `0.6335` n `12`; crypto_alt avg `-1.1656` n `230`; crypto_major avg `-1.2435` n `8`; equity avg `-0.993` n `94`; fx avg `0.1053` n `6`; index avg `-0.1467` n `25`; metal avg `0.0189` n `20`; unknown avg `-0.047` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
