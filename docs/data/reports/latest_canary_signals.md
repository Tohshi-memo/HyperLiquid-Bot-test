# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T13:37:23.500682+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.011` n `12`; crypto_alt avg `0.0315` n `230`; crypto_major avg `0.006` n `8`; equity avg `-0.0405` n `112`; fx avg `0.0006` n `6`; index avg `-0.003` n `25`; metal avg `-0.007` n `20`; unknown avg `-0.0886` n `784`
- 1h: commodity avg `0.0502` n `12`; crypto_alt avg `0.007` n `230`; crypto_major avg `0.0224` n `8`; equity avg `0.136` n `112`; fx avg `-0.0033` n `6`; index avg `0.0314` n `25`; metal avg `0.0094` n `20`; unknown avg `-0.1942` n `784`
- 4h: commodity avg `0.109` n `12`; crypto_alt avg `0.2517` n `230`; crypto_major avg `0.1476` n `8`; equity avg `0.2253` n `112`; fx avg `-0.0152` n `6`; index avg `0.047` n `25`; metal avg `-0.029` n `20`; unknown avg `-0.1269` n `784`
- 24h: commodity avg `0.0758` n `12`; crypto_alt avg `0.2496` n `230`; crypto_major avg `-0.0616` n `8`; equity avg `0.6275` n `112`; fx avg `0.0075` n `6`; index avg `-0.0173` n `25`; metal avg `-0.0809` n `20`; unknown avg `-0.1592` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0535`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0528`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.051`, n `668`, weak_sample_signal
