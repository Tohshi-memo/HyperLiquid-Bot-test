# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T07:07:31.947690+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1522` n `12`; crypto_alt avg `0.0244` n `230`; crypto_major avg `0.1557` n `8`; equity avg `0.0634` n `112`; fx avg `0.0077` n `6`; index avg `0.0005` n `25`; metal avg `0.0385` n `20`; unknown avg `0.0513` n `785`
- 1h: commodity avg `0.1214` n `12`; crypto_alt avg `-0.0389` n `230`; crypto_major avg `0.0836` n `8`; equity avg `0.1473` n `112`; fx avg `0.0438` n `6`; index avg `0.0188` n `25`; metal avg `0.0356` n `20`; unknown avg `54.7477` n `785`
- 4h: commodity avg `0.0359` n `12`; crypto_alt avg `0.2851` n `230`; crypto_major avg `0.3052` n `8`; equity avg `0.1607` n `112`; fx avg `0.0867` n `6`; index avg `0.0279` n `25`; metal avg `0.2618` n `20`; unknown avg `57.1774` n `753`
- 24h: commodity avg `0.4` n `12`; crypto_alt avg `0.8531` n `230`; crypto_major avg `0.1612` n `8`; equity avg `-0.1642` n `112`; fx avg `0.2036` n `6`; index avg `0.0544` n `25`; metal avg `0.0325` n `20`; unknown avg `56.8562` n `753`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.192`, n `669`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1402`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1396`, n `669`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1324`, n `669`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1185`, n `669`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1182`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1161`, n `669`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1101`, n `669`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1014`, n `669`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0976`, n `669`, weak_sample_signal
