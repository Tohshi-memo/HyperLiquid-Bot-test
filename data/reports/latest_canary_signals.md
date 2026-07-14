# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T19:37:34.776593+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.85` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0721` n `12`; crypto_alt avg `-0.192` n `230`; crypto_major avg `-0.2443` n `8`; equity avg `-0.0597` n `92`; fx avg `-0.0035` n `6`; index avg `0.0074` n `25`; metal avg `-0.0116` n `20`; unknown avg `0.1428` n `768`
- 1h: commodity avg `0.0727` n `12`; crypto_alt avg `-0.0091` n `230`; crypto_major avg `0.0135` n `8`; equity avg `0.038` n `92`; fx avg `0.0022` n `6`; index avg `-0.0159` n `25`; metal avg `0.0581` n `20`; unknown avg `-0.0356` n `768`
- 4h: commodity avg `0.133` n `12`; crypto_alt avg `-0.7127` n `230`; crypto_major avg `-0.2202` n `8`; equity avg `-0.0017` n `92`; fx avg `-0.0171` n `6`; index avg `-0.0233` n `25`; metal avg `-0.1616` n `20`; unknown avg `-0.1964` n `766`
- 24h: commodity avg `0.3882` n `12`; crypto_alt avg `1.6121` n `230`; crypto_major avg `3.2565` n `8`; equity avg `1.4806` n `92`; fx avg `-0.0122` n `6`; index avg `0.4081` n `25`; metal avg `0.6291` n `20`; unknown avg `-0.0003` n `742`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1923`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1545`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
