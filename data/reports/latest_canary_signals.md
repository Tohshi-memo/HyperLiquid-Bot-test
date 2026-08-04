# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T15:52:36.411715+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1119` n `12`; crypto_alt avg `0.4842` n `230`; crypto_major avg `0.4921` n `8`; equity avg `0.2238` n `107`; fx avg `0.0038` n `6`; index avg `0.0371` n `25`; metal avg `0.0982` n `20`; unknown avg `0.0518` n `782`
- 1h: commodity avg `-0.2481` n `12`; crypto_alt avg `0.246` n `230`; crypto_major avg `0.171` n `8`; equity avg `0.7259` n `107`; fx avg `-0.008` n `6`; index avg `0.1463` n `25`; metal avg `0.0641` n `20`; unknown avg `-0.0749` n `782`
- 4h: commodity avg `-0.4869` n `12`; crypto_alt avg `-0.0611` n `230`; crypto_major avg `0.1029` n `8`; equity avg `1.3766` n `107`; fx avg `-0.0096` n `6`; index avg `0.3323` n `25`; metal avg `0.2649` n `20`; unknown avg `-0.3204` n `781`
- 24h: commodity avg `-1.171` n `12`; crypto_alt avg `-0.0035` n `230`; crypto_major avg `0.4322` n `8`; equity avg `4.3019` n `107`; fx avg `0.0598` n `6`; index avg `0.8061` n `25`; metal avg `1.1017` n `20`; unknown avg `0.4682` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1723`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1423`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
