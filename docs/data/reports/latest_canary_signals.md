# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T11:22:34.034245+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0492` n `12`; crypto_alt avg `0.134` n `230`; crypto_major avg `0.1179` n `8`; equity avg `0.0269` n `113`; fx avg `-0.004` n `6`; index avg `-0.0022` n `25`; metal avg `0.0064` n `20`; unknown avg `-0.0049` n `784`
- 1h: commodity avg `0.1275` n `12`; crypto_alt avg `0.1073` n `230`; crypto_major avg `0.0452` n `8`; equity avg `-0.334` n `113`; fx avg `-0.0094` n `6`; index avg `-0.0552` n `25`; metal avg `-0.0599` n `20`; unknown avg `0.0078` n `784`
- 4h: commodity avg `0.1575` n `12`; crypto_alt avg `-0.0131` n `230`; crypto_major avg `-0.1976` n `8`; equity avg `-0.4285` n `113`; fx avg `0.0242` n `6`; index avg `-0.0602` n `25`; metal avg `-0.165` n `20`; unknown avg `-0.0032` n `784`
- 24h: commodity avg `0.4857` n `12`; crypto_alt avg `0.8904` n `230`; crypto_major avg `0.0173` n `8`; equity avg `-0.4479` n `113`; fx avg `0.2131` n `6`; index avg `0.0167` n `25`; metal avg `-0.1873` n `20`; unknown avg `57.0221` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1829`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.145`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1409`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
