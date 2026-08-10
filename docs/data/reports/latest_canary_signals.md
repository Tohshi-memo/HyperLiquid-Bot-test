# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T16:22:25.585181+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5443` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.2821` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0377` n `12`; crypto_alt avg `-0.1714` n `230`; crypto_major avg `-0.2341` n `8`; equity avg `-0.107` n `113`; fx avg `-0.0031` n `6`; index avg `-0.0068` n `25`; metal avg `0.0027` n `20`; unknown avg `-0.0876` n `785`
- 1h: commodity avg `0.0277` n `12`; crypto_alt avg `0.0321` n `230`; crypto_major avg `-0.132` n `8`; equity avg `0.1293` n `113`; fx avg `-0.0029` n `6`; index avg `0.0209` n `25`; metal avg `0.1449` n `20`; unknown avg `-0.0588` n `784`
- 4h: commodity avg `0.4255` n `12`; crypto_alt avg `-0.828` n `230`; crypto_major avg `-1.2671` n `8`; equity avg `-0.3684` n `113`; fx avg `0.042` n `6`; index avg `0.015` n `25`; metal avg `0.2772` n `20`; unknown avg `1.6642` n `784`
- 24h: commodity avg `1.1075` n `12`; crypto_alt avg `-0.713` n `230`; crypto_major avg `-1.559` n `8`; equity avg `-1.129` n `113`; fx avg `0.2425` n `6`; index avg `-0.0211` n `25`; metal avg `0.0551` n `20`; unknown avg `103.4465` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1695`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1593`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1575`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.143`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
