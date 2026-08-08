# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T20:37:24.583648+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0033` n `12`; crypto_alt avg `-0.0169` n `230`; crypto_major avg `0.0118` n `8`; equity avg `0.0429` n `112`; fx avg `0.0005` n `6`; index avg `0.0075` n `25`; metal avg `0.0055` n `20`; unknown avg `0.7196` n `784`
- 1h: commodity avg `0.016` n `12`; crypto_alt avg `0.0511` n `230`; crypto_major avg `0.105` n `8`; equity avg `-0.0472` n `112`; fx avg `-0.0101` n `6`; index avg `0.0094` n `25`; metal avg `-0.002` n `20`; unknown avg `0.5693` n `784`
- 4h: commodity avg `0.134` n `12`; crypto_alt avg `-0.0325` n `230`; crypto_major avg `-0.0216` n `8`; equity avg `0.2304` n `112`; fx avg `-0.0008` n `6`; index avg `0.0313` n `25`; metal avg `0.0151` n `20`; unknown avg `0.3429` n `784`
- 24h: commodity avg `0.1133` n `12`; crypto_alt avg `1.7508` n `230`; crypto_major avg `1.2984` n `8`; equity avg `0.6759` n `112`; fx avg `0.0139` n `6`; index avg `0.034` n `25`; metal avg `0.1381` n `20`; unknown avg `0.1733` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0523`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0462`, n `668`, weak_sample_signal
