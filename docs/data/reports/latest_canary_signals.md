# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T20:07:41.991200+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.13` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0386` n `12`; crypto_alt avg `-0.0967` n `230`; crypto_major avg `-0.169` n `8`; equity avg `0.0288` n `92`; fx avg `0.0001` n `6`; index avg `-0.0125` n `25`; metal avg `0.0282` n `20`; unknown avg `0.1117` n `768`
- 1h: commodity avg `0.0638` n `12`; crypto_alt avg `-0.0516` n `230`; crypto_major avg `-0.0977` n `8`; equity avg `0.2154` n `92`; fx avg `-0.0018` n `6`; index avg `0.0353` n `25`; metal avg `0.0519` n `20`; unknown avg `0.0189` n `768`
- 4h: commodity avg `0.0823` n `12`; crypto_alt avg `-0.4626` n `230`; crypto_major avg `-0.1363` n `8`; equity avg `0.3129` n `92`; fx avg `-0.0154` n `6`; index avg `0.0762` n `25`; metal avg `0.0451` n `20`; unknown avg `-0.0995` n `766`
- 24h: commodity avg `0.3987` n `12`; crypto_alt avg `1.5142` n `230`; crypto_major avg `3.0696` n `8`; equity avg `1.3245` n `92`; fx avg `-0.0196` n `6`; index avg `0.3669` n `25`; metal avg `0.5844` n `20`; unknown avg `0.0117` n `742`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.189`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1532`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
