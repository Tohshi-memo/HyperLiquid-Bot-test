# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T21:22:24.371944+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1188` n `12`; crypto_alt avg `0.0243` n `230`; crypto_major avg `-0.0004` n `8`; equity avg `-0.0141` n `112`; fx avg `-0.0191` n `6`; index avg `-0.0043` n `25`; metal avg `-0.0334` n `20`; unknown avg `-0.0622` n `785`
- 1h: commodity avg `0.1398` n `12`; crypto_alt avg `-0.0053` n `230`; crypto_major avg `-0.0036` n `8`; equity avg `0.021` n `112`; fx avg `-0.0159` n `6`; index avg `-0.003` n `25`; metal avg `-0.0366` n `20`; unknown avg `-0.2277` n `785`
- 4h: commodity avg `0.2412` n `12`; crypto_alt avg `0.1926` n `230`; crypto_major avg `-0.1857` n `8`; equity avg `0.0654` n `112`; fx avg `-0.0065` n `6`; index avg `0.0113` n `25`; metal avg `-0.007` n `20`; unknown avg `-0.3439` n `785`
- 24h: commodity avg `0.2317` n `12`; crypto_alt avg `1.3713` n `230`; crypto_major avg `0.0345` n `8`; equity avg `0.2188` n `112`; fx avg `-0.0048` n `6`; index avg `0.0197` n `25`; metal avg `0.06` n `20`; unknown avg `-0.3286` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1574`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
