# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T14:52:31.717461+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_metal_divergence: score `1.9198` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0539` n `13`; crypto_alt avg `0.8247` n `236`; crypto_major avg `0.5862` n `8`; equity avg `0.8549` n `151`; fx avg `-0.0262` n `6`; index avg `0.0919` n `26`; metal avg `0.0823` n `20`; unknown avg `0.3014` n `1136`
- 1h: commodity avg `0.2122` n `13`; crypto_alt avg `2.6076` n `236`; crypto_major avg `2.0629` n `8`; equity avg `1.7613` n `151`; fx avg `0.0163` n `6`; index avg `0.2369` n `26`; metal avg `0.1431` n `20`; unknown avg `4.3176` n `1092`
- 4h: commodity avg `0.0669` n `13`; crypto_alt avg `1.8035` n `236`; crypto_major avg `0.9881` n `8`; equity avg `0.8108` n `151`; fx avg `0.0113` n `6`; index avg `0.1812` n `26`; metal avg `0.093` n `20`; unknown avg `2.8189` n `1086`
- 24h: commodity avg `-0.0561` n `13`; crypto_alt avg `-0.9133` n `236`; crypto_major avg `-0.5243` n `8`; equity avg `-3.4529` n `151`; fx avg `0.182` n `6`; index avg `-0.5297` n `26`; metal avg `0.3288` n `20`; unknown avg `-0.6165` n `942`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1106`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1062`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0867`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0812`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0749`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0613`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
