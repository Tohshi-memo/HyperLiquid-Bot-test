# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T08:07:24.500353+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0476` n `12`; crypto_alt avg `-0.1561` n `231`; crypto_major avg `-0.2147` n `8`; equity avg `0.0595` n `122`; fx avg `-0.0001` n `6`; index avg `0.0106` n `25`; metal avg `-0.0195` n `20`; unknown avg `-0.0232` n `797`
- 1h: commodity avg `-0.0266` n `12`; crypto_alt avg `-0.2216` n `231`; crypto_major avg `-0.2509` n `8`; equity avg `-0.0823` n `122`; fx avg `-0.0002` n `6`; index avg `-0.0247` n `25`; metal avg `-0.0164` n `20`; unknown avg `-0.0516` n `797`
- 4h: commodity avg `-0.0125` n `12`; crypto_alt avg `-0.1303` n `231`; crypto_major avg `-0.1016` n `8`; equity avg `-0.3949` n `122`; fx avg `-0.0007` n `6`; index avg `-0.0559` n `25`; metal avg `-0.1207` n `20`; unknown avg `0.1292` n `781`
- 24h: commodity avg `-0.7166` n `12`; crypto_alt avg `-1.6639` n `231`; crypto_major avg `-1.7199` n `8`; equity avg `0.7578` n `122`; fx avg `-0.045` n `6`; index avg `0.0796` n `25`; metal avg `0.2119` n `20`; unknown avg `0.8263` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.186`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
