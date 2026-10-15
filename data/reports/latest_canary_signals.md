# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T06:07:27.590863+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.1` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-1.5664` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.544` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0463` n `13`; crypto_alt avg `0.057` n `236`; crypto_major avg `0.1793` n `8`; equity avg `0.2498` n `151`; fx avg `-0.0146` n `6`; index avg `0.0291` n `26`; metal avg `-0.0529` n `20`; unknown avg `0.1355` n `1102`
- 1h: commodity avg `-0.0078` n `13`; crypto_alt avg `-1.0701` n `236`; crypto_major avg `-0.7871` n `8`; equity avg `-0.4389` n `151`; fx avg `-0.0161` n `6`; index avg `-0.1098` n `26`; metal avg `-0.0549` n `20`; unknown avg `1.1573` n `1102`
- 4h: commodity avg `-0.057` n `13`; crypto_alt avg `-2.9241` n `236`; crypto_major avg `-1.6081` n `8`; equity avg `-0.3357` n `151`; fx avg `-0.0269` n `6`; index avg `-0.0641` n `26`; metal avg `-0.0417` n `20`; unknown avg `0.9874` n `1096`
- 24h: commodity avg `-0.4289` n `13`; crypto_alt avg `-5.589` n `236`; crypto_major avg `-3.9187` n `8`; equity avg `-5.3796` n `151`; fx avg `0.0536` n `6`; index avg `-0.8937` n `26`; metal avg `-0.7067` n `20`; unknown avg `1392.5678` n `890`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1073`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1034`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1028`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0997`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0996`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0858`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0853`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0732`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0649`, n `666`, weak_sample_signal
