# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T04:07:29.092631+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0237` n `12`; crypto_alt avg `0.0283` n `230`; crypto_major avg `0.0586` n `8`; equity avg `-0.012` n `92`; fx avg `0.0007` n `6`; index avg `0.0125` n `25`; metal avg `-0.0054` n `20`; unknown avg `-0.2077` n `765`
- 1h: commodity avg `-0.061` n `12`; crypto_alt avg `0.353` n `230`; crypto_major avg `0.2344` n `8`; equity avg `0.0195` n `92`; fx avg `-0.0024` n `6`; index avg `0.0065` n `25`; metal avg `-0.004` n `20`; unknown avg `-0.4904` n `765`
- 4h: commodity avg `-0.1323` n `12`; crypto_alt avg `1.1652` n `230`; crypto_major avg `0.7565` n `8`; equity avg `0.0941` n `92`; fx avg `-0.0021` n `6`; index avg `-0.0358` n `25`; metal avg `-0.0249` n `20`; unknown avg `0.2628` n `765`
- 24h: commodity avg `0.3863` n `12`; crypto_alt avg `-0.3096` n `229`; crypto_major avg `-0.1399` n `8`; equity avg `0.1044` n `92`; fx avg `0.0185` n `6`; index avg `-0.0953` n `25`; metal avg `-0.0885` n `20`; unknown avg `-0.0265` n `729`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1764`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.141`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
