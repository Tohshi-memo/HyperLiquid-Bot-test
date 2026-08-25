# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T23:07:23.922455+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1092` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0009` n `12`; crypto_alt avg `0.051` n `231`; crypto_major avg `0.0036` n `8`; equity avg `-0.0145` n `122`; fx avg `0.0026` n `6`; index avg `-0.0021` n `25`; metal avg `-0.0155` n `20`; unknown avg `0.1847` n `795`
- 1h: commodity avg `-0.0208` n `12`; crypto_alt avg `0.166` n `231`; crypto_major avg `-0.0012` n `8`; equity avg `0.0235` n `122`; fx avg `0.0206` n `6`; index avg `-0.013` n `25`; metal avg `0.0448` n `20`; unknown avg `0.1163` n `795`
- 4h: commodity avg `-0.2405` n `12`; crypto_alt avg `-1.0776` n `231`; crypto_major avg `-1.0754` n `8`; equity avg `0.1206` n `122`; fx avg `-0.0014` n `6`; index avg `0.0338` n `25`; metal avg `0.0628` n `20`; unknown avg `-0.1969` n `795`
- 24h: commodity avg `-0.7198` n `12`; crypto_alt avg `-1.4158` n `231`; crypto_major avg `-0.5329` n `8`; equity avg `2.1118` n `122`; fx avg `0.0588` n `6`; index avg `0.2539` n `25`; metal avg `-0.0993` n `20`; unknown avg `-0.4035` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1557`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
