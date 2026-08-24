# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T20:22:28.249620+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.6133` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.61` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0232` n `12`; crypto_alt avg `-0.0576` n `231`; crypto_major avg `-0.0627` n `8`; equity avg `-0.0363` n `122`; fx avg `-0.001` n `6`; index avg `-0.0029` n `25`; metal avg `0.0115` n `20`; unknown avg `-0.074` n `794`
- 1h: commodity avg `-0.138` n `12`; crypto_alt avg `0.1706` n `231`; crypto_major avg `0.1293` n `8`; equity avg `-0.3122` n `122`; fx avg `-0.0034` n `6`; index avg `-0.0504` n `25`; metal avg `0.0264` n `20`; unknown avg `-0.2323` n `794`
- 4h: commodity avg `-0.1069` n `12`; crypto_alt avg `-1.5287` n `231`; crypto_major avg `-1.68` n `8`; equity avg `-0.6816` n `122`; fx avg `-0.0064` n `6`; index avg `-0.0667` n `25`; metal avg `-0.07` n `20`; unknown avg `-0.4683` n `793`
- 24h: commodity avg `-0.2615` n `12`; crypto_alt avg `-1.7332` n `231`; crypto_major avg `-0.8694` n `8`; equity avg `-2.8923` n `122`; fx avg `-0.0844` n `6`; index avg `-0.3645` n `25`; metal avg `0.11` n `20`; unknown avg `1.6916` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0511`, n `668`, weak_sample_signal
