# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T16:52:26.385746+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2732` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0161` n `12`; crypto_alt avg `0.0879` n `231`; crypto_major avg `0.0763` n `8`; equity avg `-0.035` n `122`; fx avg `-0.0018` n `6`; index avg `-0.0127` n `25`; metal avg `-0.0242` n `20`; unknown avg `0.1224` n `797`
- 1h: commodity avg `0.0549` n `12`; crypto_alt avg `-0.3653` n `231`; crypto_major avg `-0.2147` n `8`; equity avg `-0.1218` n `122`; fx avg `0.0009` n `6`; index avg `-0.0514` n `25`; metal avg `-0.0389` n `20`; unknown avg `-0.0533` n `797`
- 4h: commodity avg `0.6339` n `12`; crypto_alt avg `-1.628` n `231`; crypto_major avg `-1.2729` n `8`; equity avg `-0.0343` n `122`; fx avg `-0.007` n `6`; index avg `0.0003` n `25`; metal avg `-0.2956` n `20`; unknown avg `-0.2977` n `797`
- 24h: commodity avg `0.4042` n `12`; crypto_alt avg `-2.7574` n `231`; crypto_major avg `-2.5007` n `8`; equity avg `-0.5721` n `122`; fx avg `-0.035` n `6`; index avg `-0.0245` n `25`; metal avg `-0.3596` n `20`; unknown avg `0.2395` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1559`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
