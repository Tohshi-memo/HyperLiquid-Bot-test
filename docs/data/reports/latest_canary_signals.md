# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T08:52:24.597986+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.3` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0048` n `12`; crypto_alt avg `-0.0569` n `231`; crypto_major avg `0.0372` n `8`; equity avg `-0.0245` n `127`; fx avg `-0.0138` n `6`; index avg `-0.0033` n `26`; metal avg `0.0022` n `20`; unknown avg `-0.4884` n `793`
- 1h: commodity avg `-0.0128` n `12`; crypto_alt avg `-0.3442` n `231`; crypto_major avg `-0.1157` n `8`; equity avg `-0.0549` n `127`; fx avg `0.0016` n `6`; index avg `0.0001` n `26`; metal avg `0.01` n `20`; unknown avg `-0.1019` n `793`
- 4h: commodity avg `-0.025` n `12`; crypto_alt avg `-0.7002` n `231`; crypto_major avg `-0.3686` n `8`; equity avg `0.0244` n `127`; fx avg `-0.0068` n `6`; index avg `-0.003` n `26`; metal avg `0.0231` n `20`; unknown avg `-0.0349` n `761`
- 24h: commodity avg `-0.0262` n `12`; crypto_alt avg `-2.0297` n `231`; crypto_major avg `-2.4145` n `8`; equity avg `-1.435` n `127`; fx avg `-0.0142` n `6`; index avg `-0.1361` n `26`; metal avg `-0.5708` n `20`; unknown avg `-0.4663` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1838`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
