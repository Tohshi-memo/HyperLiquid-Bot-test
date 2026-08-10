# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T21:37:27.597268+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0082` n `12`; crypto_alt avg `0.1652` n `230`; crypto_major avg `0.1066` n `8`; equity avg `0.0456` n `113`; fx avg `-0.0069` n `6`; index avg `0.0025` n `25`; metal avg `0.0041` n `20`; unknown avg `-0.0626` n `785`
- 1h: commodity avg `0.0281` n `12`; crypto_alt avg `-0.2721` n `230`; crypto_major avg `-0.0835` n `8`; equity avg `-0.0663` n `113`; fx avg `-0.0119` n `6`; index avg `0.013` n `25`; metal avg `0.0301` n `20`; unknown avg `-0.0596` n `785`
- 4h: commodity avg `0.0719` n `12`; crypto_alt avg `-0.4192` n `230`; crypto_major avg `0.1434` n `8`; equity avg `-0.4446` n `113`; fx avg `0.0069` n `6`; index avg `-0.014` n `25`; metal avg `0.2101` n `20`; unknown avg `0.7528` n `785`
- 24h: commodity avg `1.0959` n `12`; crypto_alt avg `-1.2918` n `230`; crypto_major avg `-1.0736` n `8`; equity avg `-1.824` n `113`; fx avg `0.2594` n `6`; index avg `-0.086` n `25`; metal avg `0.28` n `20`; unknown avg `103.629` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1802`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1741`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1617`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1592`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
