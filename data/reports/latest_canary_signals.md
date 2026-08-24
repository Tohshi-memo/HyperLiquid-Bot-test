# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T04:52:28.205607+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0227` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0266` n `12`; crypto_alt avg `-0.391` n `231`; crypto_major avg `-0.4536` n `8`; equity avg `-0.0149` n `122`; fx avg `-0.0133` n `6`; index avg `0.0096` n `25`; metal avg `0.0108` n `20`; unknown avg `1.0957` n `793`
- 1h: commodity avg `0.0014` n `12`; crypto_alt avg `0.1181` n `231`; crypto_major avg `-0.1853` n `8`; equity avg `0.048` n `122`; fx avg `-0.0156` n `6`; index avg `0.0129` n `25`; metal avg `-0.0448` n `20`; unknown avg `0.0771` n `793`
- 4h: commodity avg `0.0056` n `12`; crypto_alt avg `-1.0292` n `231`; crypto_major avg `-1.1625` n `8`; equity avg `-1.3442` n `122`; fx avg `-0.014` n `6`; index avg `-0.1398` n `25`; metal avg `0.0349` n `20`; unknown avg `0.4893` n `793`
- 24h: commodity avg `-0.2673` n `12`; crypto_alt avg `4.2301` n `231`; crypto_major avg `1.2823` n `8`; equity avg `-1.0286` n `122`; fx avg `-0.1998` n `6`; index avg `-0.0927` n `25`; metal avg `0.1212` n `20`; unknown avg `6.0287` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
