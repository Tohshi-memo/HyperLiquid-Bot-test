# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T03:07:27.736760+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.01` n `12`; crypto_alt avg `0.0178` n `230`; crypto_major avg `0.032` n `8`; equity avg `-0.0365` n `113`; fx avg `-0.004` n `6`; index avg `0.0031` n `25`; metal avg `0.0263` n `20`; unknown avg `0.2442` n `785`
- 1h: commodity avg `0.0053` n `12`; crypto_alt avg `-0.1998` n `230`; crypto_major avg `0.0088` n `8`; equity avg `0.117` n `113`; fx avg `-0.013` n `6`; index avg `0.0253` n `25`; metal avg `-0.0929` n `20`; unknown avg `0.082` n `785`
- 4h: commodity avg `0.0524` n `12`; crypto_alt avg `0.2651` n `230`; crypto_major avg `0.1641` n `8`; equity avg `0.5179` n `113`; fx avg `-0.0479` n `6`; index avg `0.1308` n `25`; metal avg `0.0522` n `20`; unknown avg `-0.1681` n `785`
- 24h: commodity avg `0.8544` n `12`; crypto_alt avg `-0.4861` n `230`; crypto_major avg `-0.5491` n `8`; equity avg `-1.0084` n `113`; fx avg `0.1115` n `6`; index avg `0.0342` n `25`; metal avg `0.5985` n `20`; unknown avg `103.8939` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1671`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1625`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1616`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1572`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1544`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
