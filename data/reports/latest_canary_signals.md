# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T08:52:30.538756+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1239` n `12`; crypto_alt avg `-0.0645` n `230`; crypto_major avg `0.0213` n `8`; equity avg `-0.0475` n `112`; fx avg `0.0133` n `6`; index avg `-0.0026` n `25`; metal avg `-0.0263` n `20`; unknown avg `0.0649` n `785`
- 1h: commodity avg `0.2393` n `12`; crypto_alt avg `0.0052` n `230`; crypto_major avg `-0.0372` n `8`; equity avg `-0.0658` n `112`; fx avg `0.025` n `6`; index avg `-0.0012` n `25`; metal avg `-0.0965` n `20`; unknown avg `0.0071` n `785`
- 4h: commodity avg `0.2404` n `12`; crypto_alt avg `0.4326` n `230`; crypto_major avg `0.4823` n `8`; equity avg `0.3106` n `112`; fx avg `0.1038` n `6`; index avg `0.0749` n `25`; metal avg `0.0349` n `20`; unknown avg `57.2599` n `753`
- 24h: commodity avg `0.5079` n `12`; crypto_alt avg `1.0947` n `230`; crypto_major avg `0.3953` n `8`; equity avg `0.0013` n `112`; fx avg `0.2332` n `6`; index avg `0.0812` n `25`; metal avg `-0.1158` n `20`; unknown avg `57.0091` n `753`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1872`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
