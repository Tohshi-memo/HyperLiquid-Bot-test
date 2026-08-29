# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T11:52:23.376854+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0026` n `12`; crypto_alt avg `-0.016` n `231`; crypto_major avg `0.0294` n `8`; equity avg `-0.0055` n `127`; fx avg `0.0` n `6`; index avg `-0.0022` n `26`; metal avg `-0.0008` n `20`; unknown avg `-0.1937` n `787`
- 1h: commodity avg `0.0097` n `12`; crypto_alt avg `-0.1033` n `231`; crypto_major avg `-0.0465` n `8`; equity avg `0.0098` n `127`; fx avg `-0.0022` n `6`; index avg `0.0071` n `26`; metal avg `-0.0003` n `20`; unknown avg `-0.015` n `769`
- 4h: commodity avg `0.0092` n `12`; crypto_alt avg `-0.2912` n `231`; crypto_major avg `0.0118` n `8`; equity avg `-0.0045` n `127`; fx avg `-0.0138` n `6`; index avg `0.0015` n `26`; metal avg `0.0069` n `20`; unknown avg `-0.0758` n `767`
- 24h: commodity avg `0.0975` n `12`; crypto_alt avg `-2.445` n `231`; crypto_major avg `-2.1647` n `8`; equity avg `-1.2805` n `127`; fx avg `-0.0881` n `6`; index avg `-0.1222` n `26`; metal avg `-0.7208` n `20`; unknown avg `-0.6618` n `750`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1929`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
