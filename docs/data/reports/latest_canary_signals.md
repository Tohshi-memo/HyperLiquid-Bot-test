# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T00:22:26.609302+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.26` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0249` n `12`; crypto_alt avg `0.0743` n `231`; crypto_major avg `0.0142` n `8`; equity avg `0.0055` n `127`; fx avg `0.0039` n `6`; index avg `0.0069` n `26`; metal avg `0.006` n `20`; unknown avg `0.096` n `793`
- 1h: commodity avg `-0.0398` n `12`; crypto_alt avg `0.3096` n `231`; crypto_major avg `0.2723` n `8`; equity avg `0.0663` n `127`; fx avg `-0.0016` n `6`; index avg `0.0147` n `26`; metal avg `0.0499` n `20`; unknown avg `-0.0892` n `793`
- 4h: commodity avg `-0.049` n `12`; crypto_alt avg `0.7045` n `231`; crypto_major avg `0.6289` n `8`; equity avg `0.0639` n `127`; fx avg `-0.021` n `6`; index avg `0.0185` n `26`; metal avg `0.0968` n `20`; unknown avg `0.2351` n `793`
- 24h: commodity avg `-0.1679` n `12`; crypto_alt avg `-2.8646` n `231`; crypto_major avg `-3.1799` n `8`; equity avg `-2.0166` n `127`; fx avg `-0.1352` n `6`; index avg `-0.1869` n `26`; metal avg `-0.2612` n `20`; unknown avg `-0.7146` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
