# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T16:07:44.327156+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.8216` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0301` n `12`; crypto_alt avg `0.0552` n `230`; crypto_major avg `0.0066` n `8`; equity avg `0.0758` n `103`; fx avg `0.0018` n `6`; index avg `0.0165` n `25`; metal avg `-0.0363` n `20`; unknown avg `0.0052` n `784`
- 1h: commodity avg `0.0561` n `12`; crypto_alt avg `0.1194` n `230`; crypto_major avg `0.1525` n `8`; equity avg `0.1053` n `103`; fx avg `0.027` n `6`; index avg `0.0182` n `25`; metal avg `0.0133` n `20`; unknown avg `-0.196` n `784`
- 4h: commodity avg `0.1558` n `12`; crypto_alt avg `1.0861` n `230`; crypto_major avg `1.6334` n `8`; equity avg `2.804` n `103`; fx avg `-0.0106` n `6`; index avg `0.2555` n `25`; metal avg `-0.1882` n `20`; unknown avg `0.2076` n `784`
- 24h: commodity avg `-0.2268` n `12`; crypto_alt avg `0.3367` n `230`; crypto_major avg `1.2457` n `8`; equity avg `1.5573` n `102`; fx avg `-0.1575` n `6`; index avg `-0.0009` n `25`; metal avg `-0.4571` n `20`; unknown avg `0.1336` n `766`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
