# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T10:52:25.880390+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0172` n `13`; crypto_alt avg `0.0709` n `236`; crypto_major avg `0.0511` n `8`; equity avg `0.0316` n `151`; fx avg `-0.0053` n `6`; index avg `0.0069` n `26`; metal avg `0.0044` n `20`; unknown avg `0.1545` n `1193`
- 1h: commodity avg `-0.0106` n `13`; crypto_alt avg `-0.0067` n `236`; crypto_major avg `-0.0176` n `8`; equity avg `0.0242` n `151`; fx avg `0.0109` n `6`; index avg `-0.0083` n `26`; metal avg `0.0047` n `20`; unknown avg `0.3515` n `1189`
- 4h: commodity avg `0.0133` n `13`; crypto_alt avg `-0.3533` n `236`; crypto_major avg `-0.0387` n `8`; equity avg `0.0442` n `151`; fx avg `0.0036` n `6`; index avg `0.0205` n `26`; metal avg `-0.0035` n `20`; unknown avg `-0.022` n `1173`
- 24h: commodity avg `0.3198` n `13`; crypto_alt avg `-2.1566` n `236`; crypto_major avg `-1.4626` n `8`; equity avg `-3.551` n `151`; fx avg `-0.0025` n `6`; index avg `-0.5472` n `26`; metal avg `-0.2238` n `20`; unknown avg `8.7338` n `954`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1826`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1504`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1252`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1176`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0717`, n `666`, weak_sample_signal
