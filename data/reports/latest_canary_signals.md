# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T10:37:31.225809+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0125` n `12`; crypto_alt avg `-0.0311` n `230`; crypto_major avg `0.0104` n `8`; equity avg `-0.0244` n `100`; fx avg `-0.0074` n `6`; index avg `-0.0003` n `25`; metal avg `0.0369` n `20`; unknown avg `-0.0459` n `775`
- 1h: commodity avg `0.0779` n `12`; crypto_alt avg `0.0603` n `230`; crypto_major avg `0.0677` n `8`; equity avg `0.0009` n `100`; fx avg `-0.0084` n `6`; index avg `-0.0125` n `25`; metal avg `0.0461` n `20`; unknown avg `-0.0143` n `775`
- 4h: commodity avg `-0.1861` n `12`; crypto_alt avg `-0.455` n `230`; crypto_major avg `-0.2828` n `8`; equity avg `0.2019` n `100`; fx avg `-0.0649` n `6`; index avg `0.0223` n `25`; metal avg `0.0866` n `20`; unknown avg `-0.1361` n `775`
- 24h: commodity avg `-0.6632` n `12`; crypto_alt avg `0.5292` n `230`; crypto_major avg `1.2693` n `8`; equity avg `1.3303` n `100`; fx avg `0.0911` n `6`; index avg `0.1439` n `25`; metal avg `0.4128` n `20`; unknown avg `-0.1518` n `759`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1935`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
