# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T11:22:30.553264+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.9186` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.7184` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.52` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0517` n `12`; crypto_alt avg `-0.184` n `231`; crypto_major avg `-0.3626` n `8`; equity avg `0.0263` n `122`; fx avg `0.0046` n `6`; index avg `0.0027` n `25`; metal avg `0.0281` n `20`; unknown avg `-0.0694` n `795`
- 1h: commodity avg `0.0853` n `12`; crypto_alt avg `-0.0913` n `231`; crypto_major avg `-0.1828` n `8`; equity avg `-0.2031` n `122`; fx avg `-0.0138` n `6`; index avg `-0.0261` n `25`; metal avg `0.0279` n `20`; unknown avg `0.0404` n `795`
- 4h: commodity avg `-0.2783` n `12`; crypto_alt avg `-1.2658` n `231`; crypto_major avg `-1.6236` n `8`; equity avg `0.295` n `122`; fx avg `-0.0237` n `6`; index avg `0.0948` n `25`; metal avg `-0.1036` n `20`; unknown avg `-0.0851` n `794`
- 24h: commodity avg `-0.6627` n `12`; crypto_alt avg `0.1018` n `231`; crypto_major avg `0.8088` n `8`; equity avg `0.7292` n `122`; fx avg `0.0043` n `6`; index avg `0.1463` n `25`; metal avg `-0.1887` n `20`; unknown avg `-0.08` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.056`, n `668`, weak_sample_signal
