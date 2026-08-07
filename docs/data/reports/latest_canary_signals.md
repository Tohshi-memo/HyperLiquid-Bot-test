# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T08:09:57.240673+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0555` n `12`; crypto_alt avg `0.0307` n `230`; crypto_major avg `-0.0267` n `8`; equity avg `0.2527` n `112`; fx avg `-0.0044` n `6`; index avg `0.0505` n `25`; metal avg `0.0818` n `20`; unknown avg `0.0426` n `782`
- 1h: commodity avg `-0.0825` n `12`; crypto_alt avg `0.0371` n `230`; crypto_major avg `-0.0114` n `8`; equity avg `0.3079` n `112`; fx avg `0.0185` n `6`; index avg `0.0569` n `25`; metal avg `0.0892` n `20`; unknown avg `0.0298` n `782`
- 4h: commodity avg `-0.0255` n `12`; crypto_alt avg `0.3111` n `230`; crypto_major avg `0.0581` n `8`; equity avg `0.7519` n `112`; fx avg `-0.0232` n `6`; index avg `0.1578` n `25`; metal avg `0.325` n `20`; unknown avg `0.0022` n `766`
- 24h: commodity avg `0.4779` n `12`; crypto_alt avg `0.2421` n `230`; crypto_major avg `-0.8759` n `8`; equity avg `1.8016` n `109`; fx avg `-0.1004` n `6`; index avg `0.0587` n `25`; metal avg `0.3728` n `20`; unknown avg `110.7738` n `765`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0535`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.053`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0525`, n `668`, weak_sample_signal
