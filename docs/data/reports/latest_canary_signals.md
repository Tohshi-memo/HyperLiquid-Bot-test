# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T10:53:22.170860+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.065` n `12`; crypto_alt avg `-0.3643` n `227`; crypto_major avg `-0.3431` n `8`; equity avg `-0.1833` n `106`; fx avg `0.0173` n `6`; index avg `-0.0324` n `25`; metal avg `-0.0285` n `20`; unknown avg `0.0158` n `785`
- 1h: commodity avg `0.0393` n `12`; crypto_alt avg `-0.0139` n `231`; crypto_major avg `0.0467` n `8`; equity avg `-0.1565` n `122`; fx avg `0.0205` n `6`; index avg `-0.0298` n `25`; metal avg `-0.0038` n `20`; unknown avg `-0.0031` n `793`
- 4h: commodity avg `0.1999` n `12`; crypto_alt avg `0.0273` n `231`; crypto_major avg `-0.2825` n `8`; equity avg `0.0089` n `122`; fx avg `0.0192` n `6`; index avg `0.0194` n `25`; metal avg `-0.1069` n `20`; unknown avg `0.3913` n `793`
- 24h: commodity avg `-0.1541` n `12`; crypto_alt avg `1.3798` n `231`; crypto_major avg `0.4023` n `8`; equity avg `-1.4079` n `122`; fx avg `-0.117` n `6`; index avg `-0.1479` n `25`; metal avg `0.1474` n `20`; unknown avg `5.0665` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal
