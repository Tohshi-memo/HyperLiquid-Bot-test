# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T07:52:28.678862+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0556` n `12`; crypto_alt avg `0.1069` n `231`; crypto_major avg `0.0807` n `8`; equity avg `0.0053` n `122`; fx avg `-0.0087` n `6`; index avg `0.0008` n `25`; metal avg `-0.0235` n `20`; unknown avg `0.0153` n `797`
- 1h: commodity avg `-0.115` n `12`; crypto_alt avg `0.0824` n `231`; crypto_major avg `0.2094` n `8`; equity avg `-0.2203` n `122`; fx avg `0.0144` n `6`; index avg `-0.0462` n `25`; metal avg `0.0055` n `20`; unknown avg `0.0742` n `797`
- 4h: commodity avg `-0.0372` n `12`; crypto_alt avg `0.0561` n `231`; crypto_major avg `0.22` n `8`; equity avg `-0.4578` n `122`; fx avg `-0.019` n `6`; index avg `-0.0862` n `25`; metal avg `-0.1055` n `20`; unknown avg `0.1209` n `781`
- 24h: commodity avg `-0.763` n `12`; crypto_alt avg `-1.4667` n `231`; crypto_major avg `-1.5722` n `8`; equity avg `0.6166` n `122`; fx avg `-0.0398` n `6`; index avg `0.0676` n `25`; metal avg `0.1814` n `20`; unknown avg `0.8416` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1859`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
