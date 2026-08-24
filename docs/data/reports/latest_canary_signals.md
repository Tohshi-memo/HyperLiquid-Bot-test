# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T22:11:09.089358+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0142` n `12`; crypto_alt avg `-0.0757` n `231`; crypto_major avg `0.0216` n `8`; equity avg `0.0021` n `122`; fx avg `-0.0086` n `6`; index avg `0.0027` n `25`; metal avg `0.0307` n `20`; unknown avg `-0.1665` n `794`
- 1h: commodity avg `-0.0094` n `12`; crypto_alt avg `-0.129` n `231`; crypto_major avg `0.0774` n `8`; equity avg `0.019` n `122`; fx avg `-0.0031` n `6`; index avg `0.0026` n `25`; metal avg `0.0457` n `20`; unknown avg `-0.2376` n `794`
- 4h: commodity avg `-0.0258` n `12`; crypto_alt avg `0.0512` n `231`; crypto_major avg `0.3586` n `8`; equity avg `-0.2909` n `122`; fx avg `-0.0083` n `6`; index avg `-0.0271` n `25`; metal avg `0.1368` n `20`; unknown avg `-0.6046` n `794`
- 24h: commodity avg `-0.2009` n `12`; crypto_alt avg `-1.5392` n `231`; crypto_major avg `-0.7965` n `8`; equity avg `-2.7167` n `122`; fx avg `-0.0636` n `6`; index avg `-0.3168` n `25`; metal avg `0.1853` n `20`; unknown avg `0.7232` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0471`, n `668`, weak_sample_signal
