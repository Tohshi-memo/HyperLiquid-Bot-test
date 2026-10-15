# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T13:07:37.344627+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0396` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0672` n `13`; crypto_alt avg `-0.1886` n `236`; crypto_major avg `-0.29` n `8`; equity avg `-0.1012` n `151`; fx avg `-0.0167` n `6`; index avg `-0.0293` n `26`; metal avg `0.0038` n `20`; unknown avg `-0.041` n `1134`
- 1h: commodity avg `-0.1522` n `13`; crypto_alt avg `-0.4595` n `236`; crypto_major avg `-0.471` n `8`; equity avg `-0.2694` n `151`; fx avg `-0.0228` n `6`; index avg `-0.0154` n `26`; metal avg `0.0165` n `20`; unknown avg `0.5234` n `1134`
- 4h: commodity avg `-0.1061` n `13`; crypto_alt avg `-1.0604` n `236`; crypto_major avg `-1.0925` n `8`; equity avg `-0.7301` n `151`; fx avg `-0.0214` n `6`; index avg `-0.0529` n `26`; metal avg `0.0162` n `20`; unknown avg `0.2599` n `1048`
- 24h: commodity avg `-0.2905` n `13`; crypto_alt avg `-3.9082` n `236`; crypto_major avg `-3.1889` n `8`; equity avg `-5.0991` n `151`; fx avg `0.1467` n `6`; index avg `-0.7456` n `26`; metal avg `0.004` n `20`; unknown avg `0.6341` n `957`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1207`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0974`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0946`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0878`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0807`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0783`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0718`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
