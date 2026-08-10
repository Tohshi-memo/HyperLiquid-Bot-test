# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T03:07:27.285951+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0223` n `12`; crypto_alt avg `-0.116` n `230`; crypto_major avg `-0.1259` n `8`; equity avg `-0.0665` n `112`; fx avg `-0.0106` n `6`; index avg `-0.0175` n `25`; metal avg `-0.0412` n `20`; unknown avg `-0.0715` n `785`
- 1h: commodity avg `-0.0436` n `12`; crypto_alt avg `-0.1156` n `230`; crypto_major avg `-0.0682` n `8`; equity avg `-0.0577` n `112`; fx avg `-0.0192` n `6`; index avg `-0.0114` n `25`; metal avg `-0.0507` n `20`; unknown avg `-0.1918` n `785`
- 4h: commodity avg `0.0314` n `12`; crypto_alt avg `-0.1451` n `230`; crypto_major avg `-0.0903` n `8`; equity avg `-0.3359` n `112`; fx avg `0.0971` n `6`; index avg `0.0083` n `25`; metal avg `-0.1854` n `20`; unknown avg `-0.1995` n `785`
- 24h: commodity avg `0.3801` n `12`; crypto_alt avg `0.7234` n `230`; crypto_major avg `0.095` n `8`; equity avg `-0.3035` n `112`; fx avg `0.0975` n `6`; index avg `0.0154` n `25`; metal avg `-0.2313` n `20`; unknown avg `-0.2997` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1914`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1466`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
