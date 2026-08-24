# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T17:52:23.625637+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.1717` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0329` n `12`; crypto_alt avg `0.1104` n `231`; crypto_major avg `0.0399` n `8`; equity avg `-0.0546` n `122`; fx avg `-0.0031` n `6`; index avg `-0.0124` n `25`; metal avg `-0.0698` n `20`; unknown avg `-0.0523` n `794`
- 1h: commodity avg `-0.1059` n `12`; crypto_alt avg `-1.3344` n `231`; crypto_major avg `-1.2308` n `8`; equity avg `-0.2763` n `122`; fx avg `-0.0174` n `6`; index avg `-0.0591` n `25`; metal avg `-0.1352` n `20`; unknown avg `-0.0514` n `793`
- 4h: commodity avg `-0.2246` n `12`; crypto_alt avg `-0.1245` n `231`; crypto_major avg `-0.4953` n `8`; equity avg `0.8837` n `122`; fx avg `-0.0323` n `6`; index avg `0.0835` n `25`; metal avg `-0.1861` n `20`; unknown avg `-0.1223` n `793`
- 24h: commodity avg `-0.2563` n `12`; crypto_alt avg `-1.6617` n `231`; crypto_major avg `-0.8088` n `8`; equity avg `-2.6026` n `122`; fx avg `-0.1585` n `6`; index avg `-0.342` n `25`; metal avg `0.0323` n `20`; unknown avg `3.3565` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
