# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T22:52:29.176597+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0538` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0239` n `12`; crypto_alt avg `-0.1131` n `233`; crypto_major avg `-0.1038` n `8`; equity avg `-0.0697` n `136`; fx avg `-0.0049` n `6`; index avg `-0.0035` n `27`; metal avg `0.0001` n `20`; unknown avg `-0.1295` n `840`
- 1h: commodity avg `0.4217` n `12`; crypto_alt avg `-1.7106` n `233`; crypto_major avg `-1.0871` n `8`; equity avg `-0.4932` n `136`; fx avg `0.0128` n `6`; index avg `-0.0982` n `27`; metal avg `-0.0957` n `20`; unknown avg `3.9769` n `838`
- 4h: commodity avg `0.3709` n `12`; crypto_alt avg `-2.0086` n `233`; crypto_major avg `-1.115` n `8`; equity avg `-0.4216` n `136`; fx avg `0.0502` n `6`; index avg `-0.0612` n `27`; metal avg `-0.0966` n `20`; unknown avg `14.0977` n `802`
- 24h: commodity avg `0.6085` n `12`; crypto_alt avg `-1.5073` n `233`; crypto_major avg `-1.5573` n `8`; equity avg `-1.4876` n `136`; fx avg `0.0659` n `6`; index avg `-0.2962` n `26`; metal avg `-0.1375` n `20`; unknown avg `2.4471` n `716`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
