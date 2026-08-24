# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T02:52:29.467363+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0337` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0356` n `12`; crypto_alt avg `-0.3312` n `231`; crypto_major avg `-0.3913` n `8`; equity avg `-0.2191` n `122`; fx avg `-0.0029` n `6`; index avg `-0.0365` n `25`; metal avg `-0.1263` n `20`; unknown avg `0.1064` n `793`
- 1h: commodity avg `0.0516` n `12`; crypto_alt avg `0.2014` n `231`; crypto_major avg `0.3051` n `8`; equity avg `-0.4615` n `122`; fx avg `-0.0288` n `6`; index avg `-0.039` n `25`; metal avg `0.0342` n `20`; unknown avg `0.9054` n `793`
- 4h: commodity avg `-0.1573` n `12`; crypto_alt avg `-1.8837` n `231`; crypto_major avg `-1.1463` n `8`; equity avg `-1.2393` n `122`; fx avg `-0.0715` n `6`; index avg `-0.1126` n `25`; metal avg `0.0484` n `20`; unknown avg `1.7237` n `793`
- 24h: commodity avg `-0.3585` n `12`; crypto_alt avg `2.2261` n `231`; crypto_major avg `0.2226` n `8`; equity avg `-0.7441` n `122`; fx avg `-0.2046` n `6`; index avg `-0.0263` n `25`; metal avg `0.0692` n `20`; unknown avg `5.9825` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
