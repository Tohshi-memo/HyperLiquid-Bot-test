# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T22:52:24.970686+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0307` n `12`; crypto_alt avg `-0.3101` n `230`; crypto_major avg `-0.1824` n `8`; equity avg `0.0235` n `112`; fx avg `0.0076` n `6`; index avg `0.007` n `25`; metal avg `0.0093` n `20`; unknown avg `0.1071` n `785`
- 1h: commodity avg `0.2082` n `12`; crypto_alt avg `-0.5016` n `230`; crypto_major avg `-0.5706` n `8`; equity avg `-0.251` n `112`; fx avg `0.0143` n `6`; index avg `-0.0486` n `25`; metal avg `-0.0828` n `20`; unknown avg `0.4336` n `785`
- 4h: commodity avg `0.3313` n `12`; crypto_alt avg `-0.2777` n `230`; crypto_major avg `-0.5119` n `8`; equity avg `-0.1782` n `112`; fx avg `0.0041` n `6`; index avg `-0.0571` n `25`; metal avg `-0.1383` n `20`; unknown avg `-0.0381` n `785`
- 24h: commodity avg `0.4294` n `12`; crypto_alt avg `0.9941` n `230`; crypto_major avg `-0.1633` n `8`; equity avg `-0.0435` n `112`; fx avg `0.0046` n `6`; index avg `-0.0156` n `25`; metal avg `-0.0615` n `20`; unknown avg `-0.3311` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1925`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
