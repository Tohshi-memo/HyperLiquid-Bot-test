# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T00:52:31.579239+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0255` n `12`; crypto_alt avg `0.0665` n `230`; crypto_major avg `0.0348` n `8`; equity avg `0.1355` n `113`; fx avg `-0.011` n `6`; index avg `0.0311` n `25`; metal avg `-0.0103` n `20`; unknown avg `-0.1134` n `785`
- 1h: commodity avg `0.0423` n `12`; crypto_alt avg `0.1976` n `230`; crypto_major avg `-0.0453` n `8`; equity avg `0.3337` n `113`; fx avg `-0.0476` n `6`; index avg `0.0504` n `25`; metal avg `0.0986` n `20`; unknown avg `-0.0942` n `785`
- 4h: commodity avg `-0.0091` n `12`; crypto_alt avg `-0.1297` n `230`; crypto_major avg `-0.4466` n `8`; equity avg `0.0096` n `113`; fx avg `-0.047` n `6`; index avg `0.0186` n `25`; metal avg `0.1133` n `20`; unknown avg `-0.1571` n `785`
- 24h: commodity avg `0.8292` n `12`; crypto_alt avg `-0.5128` n `230`; crypto_major avg `-0.7036` n `8`; equity avg `-1.4084` n `113`; fx avg `0.15` n `6`; index avg `-0.0396` n `25`; metal avg `0.5176` n `20`; unknown avg `103.7444` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.192`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1819`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1722`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1666`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1531`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
