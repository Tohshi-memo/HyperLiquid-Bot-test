# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T23:07:25.755843+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2317` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.001` n `12`; crypto_alt avg `-0.0199` n `233`; crypto_major avg `-0.0567` n `8`; equity avg `-0.0018` n `136`; fx avg `-0.0166` n `6`; index avg `0.0133` n `27`; metal avg `0.0349` n `20`; unknown avg `0.2206` n `838`
- 1h: commodity avg `-0.0177` n `12`; crypto_alt avg `-0.9099` n `233`; crypto_major avg `-0.5921` n `8`; equity avg `-0.2109` n `136`; fx avg `0.0` n `6`; index avg `0.0178` n `27`; metal avg `0.0196` n `20`; unknown avg `-0.2082` n `838`
- 4h: commodity avg `0.3485` n `12`; crypto_alt avg `-2.0993` n `233`; crypto_major avg `-1.2835` n `8`; equity avg `-0.4515` n `136`; fx avg `0.0314` n `6`; index avg `-0.0518` n `27`; metal avg `-0.0647` n `20`; unknown avg `19.4286` n `802`
- 24h: commodity avg `0.6105` n `12`; crypto_alt avg `-1.4971` n `233`; crypto_major avg `-1.6508` n `8`; equity avg `-1.4874` n `136`; fx avg `0.0468` n `6`; index avg `-0.2806` n `26`; metal avg `-0.0985` n `20`; unknown avg `2.7914` n `716`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
