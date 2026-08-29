# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T08:37:28.772227+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.42` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0021` n `12`; crypto_alt avg `-0.1059` n `231`; crypto_major avg `-0.0567` n `8`; equity avg `-0.0079` n `127`; fx avg `0.0075` n `6`; index avg `0.0018` n `26`; metal avg `0.0067` n `20`; unknown avg `4.7532` n `793`
- 1h: commodity avg `-0.005` n `12`; crypto_alt avg `-0.3838` n `231`; crypto_major avg `-0.1799` n `8`; equity avg `-0.024` n `127`; fx avg `0.0198` n `6`; index avg `0.0016` n `26`; metal avg `0.0187` n `20`; unknown avg `4.7491` n `793`
- 4h: commodity avg `-0.0071` n `12`; crypto_alt avg `-0.54` n `231`; crypto_major avg `-0.3105` n `8`; equity avg `0.0462` n `127`; fx avg `0.0076` n `6`; index avg `0.0029` n `26`; metal avg `0.0114` n `20`; unknown avg `5.0264` n `761`
- 24h: commodity avg `0.0695` n `12`; crypto_alt avg `-2.2777` n `231`; crypto_major avg `-2.7394` n `8`; equity avg `-1.4641` n `127`; fx avg `0.0031` n `6`; index avg `-0.1419` n `26`; metal avg `-0.6022` n `20`; unknown avg `4.4296` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1842`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
