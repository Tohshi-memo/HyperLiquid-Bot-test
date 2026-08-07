# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T17:52:30.177161+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2125` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0353` n `12`; crypto_alt avg `-0.012` n `230`; crypto_major avg `0.0526` n `8`; equity avg `-0.031` n `112`; fx avg `0.0102` n `6`; index avg `0.002` n `25`; metal avg `0.0562` n `20`; unknown avg `0.1196` n `782`
- 1h: commodity avg `-0.0369` n `12`; crypto_alt avg `-0.2736` n `230`; crypto_major avg `-0.5693` n `8`; equity avg `-0.1255` n `112`; fx avg `0.001` n `6`; index avg `-0.0165` n `25`; metal avg `0.073` n `20`; unknown avg `0.0878` n `782`
- 4h: commodity avg `0.1908` n `12`; crypto_alt avg `-0.5632` n `230`; crypto_major avg `-1.2334` n `8`; equity avg `0.1699` n `112`; fx avg `-0.0127` n `6`; index avg `-0.0209` n `25`; metal avg `-0.0947` n `20`; unknown avg `0.3006` n `782`
- 24h: commodity avg `0.3565` n `12`; crypto_alt avg `-0.624` n `230`; crypto_major avg `-0.867` n `8`; equity avg `0.5602` n `112`; fx avg `-0.1405` n `6`; index avg `-0.0455` n `25`; metal avg `0.3024` n `20`; unknown avg `-0.1092` n `765`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.2045`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1572`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1548`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1395`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
