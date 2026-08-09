# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T22:14:45.084728+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2552` n `12`; crypto_alt avg `0.2934` n `230`; crypto_major avg `0.2947` n `8`; equity avg `-0.1244` n `112`; fx avg `0.0106` n `6`; index avg `-0.0476` n `25`; metal avg `-0.0586` n `20`; unknown avg `0.0005` n `785`
- 1h: commodity avg `0.3626` n `12`; crypto_alt avg `0.3304` n `230`; crypto_major avg `0.3834` n `8`; equity avg `-0.1125` n `112`; fx avg `-0.0105` n `6`; index avg `-0.0472` n `25`; metal avg `-0.1382` n `20`; unknown avg `0.2374` n `785`
- 4h: commodity avg `0.4778` n `12`; crypto_alt avg `0.4032` n `230`; crypto_major avg `0.263` n `8`; equity avg `-0.0568` n `112`; fx avg `0.0026` n `6`; index avg `-0.041` n `25`; metal avg `-0.1099` n `20`; unknown avg `-0.4397` n `785`
- 24h: commodity avg `0.4544` n `12`; crypto_alt avg `1.7491` n `230`; crypto_major avg `0.5917` n `8`; equity avg `0.1082` n `112`; fx avg `0.0025` n `6`; index avg `-0.0102` n `25`; metal avg `-0.047` n `20`; unknown avg `-0.2229` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1724`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
