# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T23:37:27.764259+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0005` n `12`; crypto_alt avg `0.1055` n `230`; crypto_major avg `0.1487` n `8`; equity avg `0.0069` n `96`; fx avg `0.0` n `6`; index avg `-0.0051` n `25`; metal avg `-0.0002` n `20`; unknown avg `-0.0815` n `769`
- 1h: commodity avg `0.0093` n `12`; crypto_alt avg `0.3275` n `230`; crypto_major avg `0.2036` n `8`; equity avg `-0.0304` n `96`; fx avg `0.0092` n `6`; index avg `-0.0058` n `25`; metal avg `-0.0049` n `20`; unknown avg `-0.1242` n `769`
- 4h: commodity avg `0.2143` n `12`; crypto_alt avg `0.0143` n `230`; crypto_major avg `-0.0378` n `8`; equity avg `-0.4783` n `96`; fx avg `-0.061` n `6`; index avg `-0.1064` n `25`; metal avg `0.0205` n `20`; unknown avg `-0.1056` n `769`
- 24h: commodity avg `0.7379` n `12`; crypto_alt avg `-0.284` n `230`; crypto_major avg `-0.2851` n `8`; equity avg `-0.7461` n `94`; fx avg `0.0399` n `6`; index avg `-0.2547` n `25`; metal avg `0.0228` n `20`; unknown avg `0.1264` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
