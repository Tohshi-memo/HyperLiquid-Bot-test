# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T11:07:23.759204+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0069` n `12`; crypto_alt avg `-0.1442` n `231`; crypto_major avg `-0.0859` n `8`; equity avg `-0.0133` n `127`; fx avg `0.0` n `6`; index avg `0.0002` n `26`; metal avg `-0.0096` n `20`; unknown avg `0.0319` n `791`
- 1h: commodity avg `-0.0032` n `12`; crypto_alt avg `0.0045` n `231`; crypto_major avg `0.1448` n `8`; equity avg `-0.0047` n `127`; fx avg `-0.0014` n `6`; index avg `0.0042` n `26`; metal avg `-0.0139` n `20`; unknown avg `0.0843` n `791`
- 4h: commodity avg `0.0041` n `12`; crypto_alt avg `-0.3789` n `231`; crypto_major avg `-0.0319` n `8`; equity avg `-0.0019` n `127`; fx avg `-0.0097` n `6`; index avg `-0.0075` n `26`; metal avg `0.0105` n `20`; unknown avg `0.0136` n `789`
- 24h: commodity avg `-0.0311` n `12`; crypto_alt avg `-2.6719` n `231`; crypto_major avg `-2.488` n `8`; equity avg `-1.4409` n `127`; fx avg `-0.0916` n `6`; index avg `-0.133` n `26`; metal avg `-0.6988` n `20`; unknown avg `-0.4232` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1943`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
