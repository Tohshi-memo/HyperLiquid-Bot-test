# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T12:07:24.947472+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.52` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.008` n `13`; crypto_alt avg `-0.0068` n `239`; crypto_major avg `0.1555` n `8`; equity avg `-0.0175` n `168`; fx avg `0.0016` n `6`; index avg `0.0021` n `27`; metal avg `-0.0012` n `20`; unknown avg `8.1129` n `1249`
- 1h: commodity avg `-0.0111` n `13`; crypto_alt avg `-0.0086` n `239`; crypto_major avg `0.2758` n `8`; equity avg `0.0454` n `168`; fx avg `0.0034` n `6`; index avg `0.0036` n `27`; metal avg `0.0026` n `20`; unknown avg `9.3878` n `1255`
- 4h: commodity avg `-0.04` n `13`; crypto_alt avg `-0.4018` n `239`; crypto_major avg `-0.4227` n `8`; equity avg `-0.1446` n `168`; fx avg `0.0048` n `6`; index avg `-0.0257` n `27`; metal avg `0.0334` n `20`; unknown avg `348.9141` n `1221`
- 24h: commodity avg `-0.5189` n `13`; crypto_alt avg `-3.4716` n `239`; crypto_major avg `-3.0449` n `8`; equity avg `0.318` n `168`; fx avg `-0.0966` n `6`; index avg `0.0671` n `27`; metal avg `-0.1183` n `20`; unknown avg `191.136` n `1087`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
