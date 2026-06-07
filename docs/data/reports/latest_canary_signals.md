# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T00:37:20.468911+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0558` n `12`; crypto_alt avg `0.33` n `228`; crypto_major avg `0.3807` n `8`; equity avg `0.0213` n `74`; fx avg `-0.0039` n `6`; index avg `-0.0528` n `23`; metal avg `-0.0015` n `18`; unknown avg `-0.1037` n `516`
- 1h: commodity avg `0.0706` n `12`; crypto_alt avg `0.7112` n `228`; crypto_major avg `0.5694` n `8`; equity avg `0.145` n `74`; fx avg `-0.0027` n `6`; index avg `-0.0503` n `23`; metal avg `0.0703` n `18`; unknown avg `0.0628` n `515`
- 4h: commodity avg `0.1769` n `12`; crypto_alt avg `1.2714` n `228`; crypto_major avg `0.9188` n `8`; equity avg `0.2843` n `74`; fx avg `-0.0455` n `6`; index avg `0.0309` n `23`; metal avg `0.0831` n `18`; unknown avg `0.1476` n `515`
- 24h: commodity avg `0.0865` n `12`; crypto_alt avg `-1.205` n `228`; crypto_major avg `-1.469` n `8`; equity avg `-0.4468` n `74`; fx avg `0.0087` n `6`; index avg `-0.1632` n `23`; metal avg `-0.3501` n `18`; unknown avg `-0.4832` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
