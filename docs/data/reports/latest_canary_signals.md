# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T09:44:20.052916+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0588` n `12`; crypto_alt avg `-0.0933` n `230`; crypto_major avg `-0.1755` n `8`; equity avg `0.0526` n `112`; fx avg `-0.0091` n `6`; index avg `-0.013` n `25`; metal avg `-0.0214` n `20`; unknown avg `-0.0223` n `785`
- 1h: commodity avg `0.1027` n `12`; crypto_alt avg `-0.1951` n `230`; crypto_major avg `-0.2091` n `8`; equity avg `-0.0251` n `112`; fx avg `0.0079` n `6`; index avg `-0.0228` n `25`; metal avg `-0.0255` n `20`; unknown avg `0.0323` n `785`
- 4h: commodity avg `0.1974` n `12`; crypto_alt avg `0.1104` n `230`; crypto_major avg `0.0197` n `8`; equity avg `0.3182` n `112`; fx avg `0.0895` n `6`; index avg `0.024` n `25`; metal avg `-0.0801` n `20`; unknown avg `57.2677` n `753`
- 24h: commodity avg `0.4176` n `12`; crypto_alt avg `0.8937` n `230`; crypto_major avg `0.1144` n `8`; equity avg `0.0463` n `112`; fx avg `0.227` n `6`; index avg `0.0602` n `25`; metal avg `-0.1151` n `20`; unknown avg `56.9654` n `753`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1851`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
