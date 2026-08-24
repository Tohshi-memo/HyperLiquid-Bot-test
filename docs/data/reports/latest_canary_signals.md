# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T14:37:32.011670+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.5461` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0028` n `12`; crypto_alt avg `0.3894` n `231`; crypto_major avg `0.4963` n `8`; equity avg `0.2949` n `122`; fx avg `-0.007` n `6`; index avg `0.0324` n `25`; metal avg `0.065` n `20`; unknown avg `-0.0494` n `793`
- 1h: commodity avg `-0.1683` n `12`; crypto_alt avg `0.8074` n `231`; crypto_major avg `0.8796` n `8`; equity avg `0.0916` n `122`; fx avg `0.0026` n `6`; index avg `-0.029` n `25`; metal avg `0.0103` n `20`; unknown avg `-0.0742` n `793`
- 4h: commodity avg `0.083` n `12`; crypto_alt avg `1.0008` n `227`; crypto_major avg `1.51` n `8`; equity avg `-1.0361` n `106`; fx avg `0.0232` n `6`; index avg `-0.1823` n `25`; metal avg `0.2228` n `20`; unknown avg `0.9153` n `785`
- 24h: commodity avg `-0.1195` n `12`; crypto_alt avg `1.4509` n `231`; crypto_major avg `1.8686` n `8`; equity avg `-2.425` n `122`; fx avg `-0.1053` n `6`; index avg `-0.3217` n `25`; metal avg `0.3837` n `20`; unknown avg `3.9187` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0568`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
