# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T09:22:26.060142+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2477` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0973` n `13`; crypto_alt avg `-0.0884` n `239`; crypto_major avg `-0.0866` n `8`; equity avg `0.0748` n `166`; fx avg `0.0171` n `6`; index avg `-0.0027` n `27`; metal avg `-0.0344` n `20`; unknown avg `-0.207` n `1262`
- 1h: commodity avg `0.0291` n `13`; crypto_alt avg `-1.0509` n `239`; crypto_major avg `-1.0307` n `8`; equity avg `-1.4788` n `166`; fx avg `0.0315` n `6`; index avg `-0.1708` n `27`; metal avg `-0.1738` n `20`; unknown avg `423.3867` n `1256`
- 4h: commodity avg `0.2934` n `13`; crypto_alt avg `-1.4519` n `239`; crypto_major avg `-1.4671` n `8`; equity avg `-1.8112` n `166`; fx avg `0.055` n `6`; index avg `-0.2194` n `27`; metal avg `-0.3201` n `20`; unknown avg `333.4839` n `1198`
- 24h: commodity avg `-0.6325` n `13`; crypto_alt avg `-1.13` n `239`; crypto_major avg `-1.7077` n `8`; equity avg `1.2631` n `166`; fx avg `-0.1813` n `6`; index avg `0.338` n `27`; metal avg `-0.5067` n `20`; unknown avg `349.3963` n `1144`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
