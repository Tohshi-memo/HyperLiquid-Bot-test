# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T08:07:33.404102+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.071` n `12`; crypto_alt avg `0.0253` n `230`; crypto_major avg `-0.0169` n `8`; equity avg `0.2389` n `112`; fx avg `-0.0084` n `6`; index avg `0.0443` n `25`; metal avg `0.0791` n `20`; unknown avg `0.0145` n `782`
- 1h: commodity avg `-0.098` n `12`; crypto_alt avg `0.032` n `230`; crypto_major avg `-0.0016` n `8`; equity avg `0.294` n `112`; fx avg `0.0145` n `6`; index avg `0.0507` n `25`; metal avg `0.0864` n `20`; unknown avg `0.0017` n `782`
- 4h: commodity avg `-0.0408` n `12`; crypto_alt avg `0.3065` n `230`; crypto_major avg `0.068` n `8`; equity avg `0.7375` n `112`; fx avg `-0.0272` n `6`; index avg `0.1516` n `25`; metal avg `0.3221` n `20`; unknown avg `-0.0263` n `766`
- 24h: commodity avg `0.4619` n `12`; crypto_alt avg `0.24` n `230`; crypto_major avg `-0.8663` n `8`; equity avg `1.7718` n `109`; fx avg `-0.1044` n `6`; index avg `0.0525` n `25`; metal avg `0.3699` n `20`; unknown avg `110.745` n `765`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0534`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0528`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0525`, n `668`, weak_sample_signal
