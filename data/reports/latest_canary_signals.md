# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T02:22:28.775997+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0346` n `12`; crypto_alt avg `-0.2161` n `230`; crypto_major avg `-0.2446` n `8`; equity avg `-0.136` n `112`; fx avg `-0.0156` n `6`; index avg `-0.0166` n `25`; metal avg `0.0286` n `20`; unknown avg `0.0828` n `785`
- 1h: commodity avg `-0.0229` n `12`; crypto_alt avg `-0.1108` n `230`; crypto_major avg `-0.1091` n `8`; equity avg `-0.3189` n `112`; fx avg `0.0122` n `6`; index avg `-0.011` n `25`; metal avg `0.061` n `20`; unknown avg `0.4821` n `785`
- 4h: commodity avg `-0.0228` n `12`; crypto_alt avg `-1.0542` n `230`; crypto_major avg `-0.9185` n `8`; equity avg `-0.4256` n `112`; fx avg `0.1138` n `6`; index avg `0.0182` n `25`; metal avg `-0.0631` n `20`; unknown avg `0.9862` n `785`
- 24h: commodity avg `0.406` n `12`; crypto_alt avg `0.5746` n `230`; crypto_major avg `-0.2195` n `8`; equity avg `-0.3291` n `112`; fx avg `0.1088` n `6`; index avg `0.0121` n `25`; metal avg `-0.1473` n `20`; unknown avg `-0.3365` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1823`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
