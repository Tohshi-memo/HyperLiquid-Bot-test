# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T16:52:31.350676+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.6836` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0138` n `12`; crypto_alt avg `0.3333` n `234`; crypto_major avg `0.0535` n `8`; equity avg `-0.0288` n `140`; fx avg `0.0125` n `6`; index avg `0.0052` n `26`; metal avg `0.0095` n `20`; unknown avg `4.805` n `943`
- 1h: commodity avg `-0.0089` n `12`; crypto_alt avg `1.828` n `234`; crypto_major avg `1.148` n `8`; equity avg `0.141` n `140`; fx avg `0.0013` n `6`; index avg `0.0307` n `26`; metal avg `0.0295` n `20`; unknown avg `3.555` n `889`
- 4h: commodity avg `0.0025` n `12`; crypto_alt avg `2.4575` n `234`; crypto_major avg `1.7244` n `8`; equity avg `0.2832` n `140`; fx avg `0.0313` n `6`; index avg `0.0427` n `26`; metal avg `0.0408` n `20`; unknown avg `1.5211` n `889`
- 24h: commodity avg `0.4377` n `12`; crypto_alt avg `-0.122` n `234`; crypto_major avg `-0.8482` n `8`; equity avg `-0.0324` n `140`; fx avg `-0.0106` n `6`; index avg `-0.0293` n `26`; metal avg `0.0063` n `20`; unknown avg `153.1175` n `803`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1548`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1416`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
