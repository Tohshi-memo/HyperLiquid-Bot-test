# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T04:07:24.606657+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0022` n `12`; crypto_alt avg `0.0588` n `231`; crypto_major avg `0.008` n `8`; equity avg `-0.0533` n `122`; fx avg `0.0026` n `6`; index avg `-0.0046` n `25`; metal avg `-0.0544` n `20`; unknown avg `-0.0206` n `793`
- 1h: commodity avg `0.0087` n `12`; crypto_alt avg `-0.0519` n `231`; crypto_major avg `-0.1924` n `8`; equity avg `-0.2894` n `122`; fx avg `0.0025` n `6`; index avg `-0.0547` n `25`; metal avg `-0.0168` n `20`; unknown avg `-0.0709` n `793`
- 4h: commodity avg `-0.0796` n `12`; crypto_alt avg `-1.3961` n `231`; crypto_major avg `-1.1765` n `8`; equity avg `-1.7198` n `122`; fx avg `-0.0258` n `6`; index avg `-0.1858` n `25`; metal avg `-0.1263` n `20`; unknown avg `0.3982` n `793`
- 24h: commodity avg `-0.2864` n `12`; crypto_alt avg `3.6365` n `231`; crypto_major avg `0.7111` n `8`; equity avg `-1.1746` n `122`; fx avg `-0.1813` n `6`; index avg `-0.1113` n `25`; metal avg `0.1024` n `20`; unknown avg `5.97` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
