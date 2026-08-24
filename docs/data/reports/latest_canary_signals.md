# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T07:22:27.025120+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0459` n `12`; crypto_alt avg `0.2053` n `231`; crypto_major avg `0.063` n `8`; equity avg `0.043` n `122`; fx avg `0.0031` n `6`; index avg `0.0137` n `25`; metal avg `0.0099` n `20`; unknown avg `-0.0107` n `793`
- 1h: commodity avg `0.0369` n `12`; crypto_alt avg `-0.0004` n `231`; crypto_major avg `0.3428` n `8`; equity avg `0.1138` n `122`; fx avg `0.0441` n `6`; index avg `0.0186` n `25`; metal avg `0.0171` n `20`; unknown avg `-0.0682` n `793`
- 4h: commodity avg `-0.024` n `12`; crypto_alt avg `0.4992` n `231`; crypto_major avg `0.5841` n `8`; equity avg `-0.2912` n `122`; fx avg `0.0471` n `6`; index avg `-0.0484` n `25`; metal avg `0.085` n `20`; unknown avg `-0.0464` n `777`
- 24h: commodity avg `-0.296` n `12`; crypto_alt avg `3.5041` n `231`; crypto_major avg `1.7329` n `8`; equity avg `-1.1266` n `122`; fx avg `-0.3097` n `6`; index avg `-0.1002` n `25`; metal avg `0.225` n `20`; unknown avg `5.312` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0581`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
