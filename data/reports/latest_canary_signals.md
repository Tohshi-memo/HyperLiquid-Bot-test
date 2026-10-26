# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T07:37:27.464384+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0071` n `13`; crypto_alt avg `-0.4344` n `237`; crypto_major avg `-0.3161` n `8`; equity avg `-0.0216` n `152`; fx avg `-0.0068` n `6`; index avg `-0.0077` n `26`; metal avg `0.0384` n `20`; unknown avg `0.2749` n `1240`
- 1h: commodity avg `0.0633` n `13`; crypto_alt avg `-0.2875` n `237`; crypto_major avg `-0.2319` n `8`; equity avg `-0.0393` n `152`; fx avg `-0.0102` n `6`; index avg `0.016` n `26`; metal avg `0.0306` n `20`; unknown avg `0.2779` n `1238`
- 4h: commodity avg `0.1766` n `13`; crypto_alt avg `-0.0886` n `237`; crypto_major avg `0.1482` n `8`; equity avg `-0.0201` n `152`; fx avg `0.0117` n `6`; index avg `-0.0434` n `26`; metal avg `-0.0773` n `20`; unknown avg `-0.0124` n `1200`
- 24h: commodity avg `-0.5731` n `13`; crypto_alt avg `-1.0011` n `237`; crypto_major avg `-0.8615` n `8`; equity avg `-0.5561` n `152`; fx avg `0.0376` n `6`; index avg `-0.0464` n `26`; metal avg `0.1185` n `20`; unknown avg `-0.6831` n `983`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2529`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2069`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1939`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1917`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1558`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
