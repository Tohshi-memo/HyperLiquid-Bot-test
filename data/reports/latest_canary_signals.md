# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T15:52:32.496270+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.41` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.2905` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0316` n `13`; crypto_alt avg `-0.4107` n `239`; crypto_major avg `-0.449` n `8`; equity avg `-0.1513` n `164`; fx avg `0.0022` n `6`; index avg `-0.0361` n `27`; metal avg `-0.0346` n `20`; unknown avg `-0.2817` n `1265`
- 1h: commodity avg `0.0365` n `13`; crypto_alt avg `-0.7688` n `239`; crypto_major avg `-0.751` n `8`; equity avg `-0.1842` n `164`; fx avg `-0.0253` n `6`; index avg `-0.0384` n `27`; metal avg `-0.1086` n `20`; unknown avg `3.9075` n `1263`
- 4h: commodity avg `-0.0838` n `13`; crypto_alt avg `-1.2383` n `239`; crypto_major avg `-1.4936` n `8`; equity avg `-2.0358` n `164`; fx avg `-0.0159` n `6`; index avg `-0.2031` n `27`; metal avg `-0.1958` n `20`; unknown avg `1.4118` n `1257`
- 24h: commodity avg `-0.2403` n `13`; crypto_alt avg `0.9648` n `239`; crypto_major avg `0.7707` n `8`; equity avg `1.6833` n `164`; fx avg `-0.1731` n `6`; index avg `0.1645` n `27`; metal avg `-1.202` n `20`; unknown avg `-0.148` n `1136`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0548`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0545`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0517`, n `668`, weak_sample_signal
